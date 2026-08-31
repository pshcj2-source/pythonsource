# ## 문제 1 (난이도 하) — 정적 페이지 크롤링 & CSV 저장

# ### 학습 포인트

# - `requests` + `BeautifulSoup` 기본 사용
# - `select()` / `select_one()`으로 원하는 요소 찾기
# - CSV 저장 (`csv.DictWriter`)

# ### 요구사항

# 1. `https://books.toscrape.com/` 에서 첫 페이지에 있는 책 20권의 **제목, 가격, 별점**을 크롤링하세요.
# 2. 콘솔에 다음 형식으로 출력하세요.
    
#     ```
#     1. A Light in the Attic | £51.77 | 별점: Three2. Tipping the Velvet | £53.74 | 별점: One...
#     ```
    
# 3. 결과를 `books_top20.csv` 파일로 저장하세요. (컬럼: 순번, 제목, 가격, 별점)

# ### 힌트

# - 책 하나는 `<article class="product_pod">` 안에 들어있습니다.
# - 별점은 `<p class="star-rating Three">`처럼 class의 두 번째 값에 들어있습니다. (`tag['class']`로 리스트를 가져올 수 있음)

# ---

import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

res=requests.get(url)
BeautifulSoup(res.text, "html.parser")


headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 15; Pixel 9)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Edg/151.0.0.0 Mobile Safari/537.36"
            # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            # "AppleWebKit/537.36 (KHTML, like Gecko) "
            # "Chrome/124.0.0.0 Safari/537.36"
}


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

books = soup.select("article.product_pod") # select를 활용한 문법
# book = soup.select("article.product_pod") # 오류나는 문법 (첫번째 인자값만 태그로 인지)

# print(books)
count=1
top20=[]
for book in books:
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    rating = book.select_one("p.star-rating")["class"][1]

    
    if title and price and rating :
        print(f"제목 : {title}  | 가격 : {price} | 별점 : {rating}")
        top20.append({"순번" : count, "제목" : title, "가격" : price, "별점" : rating})
        count += 1
    if count > 20:
        break

    

csv_filename = "books_top20.csv"

with open(csv_filename, "w", encoding="utf-8-sig", newline="") as f:   #newline="" 비어있는 행 없도록하는 코드
    fieldnames = ["순번", "제목", "가격", "별점"]  
    # 엑셀 파일의 첫 번째 줄(헤더)에 들어갈 열 이름을 리스트 형태로 정의. 
    # 나중에 top20 리스트 안에 있는 딕셔너리의 Key 값과 정확히 일치해야 데이터를 올바른 위치에 짝지어 넣을 수 있음.
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()  # 헤더(컬럼명) 작성 / fieldnames 리스트의 값들(순번, 제목, 가격, 별점)을 파일의 맨 첫 줄에 콤마(,)로 구분하여 작성
    writer.writerows(top20)  # 20권 데이터 작성

print(f"\n[저장 완료] '{csv_filename}' 파일로 저장되었습니다.")