import io
import sys
import time
from bs4 import BeautifulSoup
from io import BytesIO  # 이미지를 다운받으면 바이너리(바이트)로 들어오는데 파일로 바로 저장되지 않고 메모리에 바이트로 넣고 다룰 수 있게 함
from playwright.sync_api import sync_playwright
import urllib.request as req
import xlsxwriter

# 작업 목표
# 유튜브 영상 페이지에 Playwright로 접속해서 무한 스크롤로 모든 댓글을 로딩시킨 뒤,
# 각 댓글의 작성자·내용·좋아요 수·프로필 이미지를 추출해서 엑셀 파일로 저장

workbook = xlsxwriter.Workbook(
    "C:/source/pythonsource/Bigpy/Py_Scrap/data/you_crawl_result.xlsx"
)
worksheet = workbook.add_worksheet()

worksheet.write("A1", "작성자")
worksheet.write("B1", "댓글내용")
worksheet.write("C1", "좋아요")
worksheet.write("D1", "프로필이미지")


def main():
    with sync_playwright() as p:  # playwright 세션 활용
        browser = p.chromium.launch(
            headless=False,  # 화면 보이게
            # 소리 끄기, 리눅스 권한 문제 방지, 공유메모리 부족 방지, GPU 비활성화
            args=[
                "--mute-audio",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
            ],
        )
        page = browser.new_page(viewport={"width": 1920, "height": 1280})

        page.goto("https://www.youtube.com/watch?v=5ZnRDcuv9xU")
        page.wait_for_timeout(5000)

        # 키보드의 page Down키를 눌러서 스크롤 수행
        page.keyboard.press("PageDown")   # Playwright 키 이름 규격은 PageDown(D가 대문자)이거나 Pagedown입니다.
        page.wait_for_timeout(2000)

        scroll_pause_time = 4000
        last_height = page.evaluate("document.documentElement.scrollHeight")

        while True:
            page.evaluate(
                "window.scrollTo(0, document.documentElement.scrollHeight)"
            )
            page.wait_for_timeout(scroll_pause_time)

            new_height = page.evaluate("document.documentElement.scrollHeight")
            print(f"Last Height: {last_height}, Current Height: {new_height}")

            # 댓글이 한 화면 내에서 끝날 때
            if new_height == last_height:
                break

            last_height = new_height

        html_content = page.content()
        browser.close()

    soup = BeautifulSoup(html_content, "html.parser")

    comment = soup.select("ytd-comment-view-model#comment")  # 여러개
    print(f"\n총 댓글 수: {len(comment)}개\n")

    ins_cnt = 2

    for dom in comment:
        try:
            img_tag = dom.select_one("#img")
            img_src = img_tag.get("src") if img_tag else None

            author_tag = dom.select_one("#author-text > span")
            author = author_tag.text.strip() if author_tag else "작성자없음"

            content_tag = dom.select_one("#content-text")
            content = content_tag.text.strip() if content_tag else "내용없음"

            posi_tag = dom.select_one("#vote-count-middle")
            posi_cnt = posi_tag.text.strip() if posi_tag else "0"

            print(f"작성자: {author}")
            print(f"댓글: {content}")
            print(f"좋아요: {posi_cnt}")
            print(f"이미지: {img_src if img_src else 'None'}")
            print()

            worksheet.write(f"A{ins_cnt}", author)
            worksheet.write(f"B{ins_cnt}", content)
            worksheet.write(f"C{ins_cnt}", posi_cnt)

            # 이미지 다운로드 및 예외처리 구조
            if img_src and img_src.startswith("http"):
                try:
                    request = req.Request(
                        img_src,
                        headers={
                            "User-Agent": (
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            )
                        },
                    )
                    img_data = BytesIO(
                        req.urlopen(request, timeout=10).read()
                    )

                    worksheet.insert_image(
                        f"D{ins_cnt}",
                        author,
                        {
                            "image_data": img_data,
                            "x_scale": 0.5,
                            "y_scale": 0.5,
                        },
                    )
                except Exception as e:
                    print(f"이미지 다운로드 실패: {e}")
                    worksheet.write(f"D{ins_cnt}", img_src)
            else:
                worksheet.write(f"D{ins_cnt}", "None")

            ins_cnt += 1

        except Exception as e:
            print(f"댓글 파싱 오류: {e}")
            continue

    print(f"\n총 {ins_cnt - 2}개 댓글 저장 완료!")

    workbook.close()

    print("엑셀 저장 완료!")


if __name__ == "__main__":
    main()