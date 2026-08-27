from bs4 import BeautifulSoup
import requests


# with requests.Session() as s:
#     # 게시글 가져오기
#     post_one = s.get("https://bbs.ruliweb.com/market/board/1020/read/37546")
    
#     post_one.raise_for_status
#     print(post_one)
#     print("-"*37)
#     print()
#     soup=BeautifulSoup(post_one.text, 'html.parser')
#     print(soup.prettify)
#     print("-"*37)
#     # 문서 출력
#     article = soup.select(
#     "#board_read > div > div.board_main > div.board_main_view > div.view_content > article > div > p")
#     print(article)
#     print()
#     print("---------------------------------------")
#     # string 처리
#     for i in article:
#         if i.string is not None and i.img == None:
#             print(i.string)




with requests.Session() as s:
    # 게시글 가져오기
    post_one = s.get("https://bbs.ruliweb.com/market/board/1020/read/37546")
    
    post_one.raise_for_status
    print(post_one)
    print("-"*37)
    print()
    soup=BeautifulSoup(post_one.text, 'html.parser')
    print(soup.prettify)
    print("-"*37)
    # 문서 출력
    article = soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > p") 
    print(article)
    print()
    print("---------------------------------------")
    # string 처리
    for i in article:
        if i.string is not None and i.img == None:
            print(i.string)

    