import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

res=requests.get(url)
BeautifulSoup(res.text, "html.parser")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# 첫 번째 책 하나만 찾기  
# #
book = soup.find("article", class_="product_pod")
# book = soup.select("article.product_pod") # select를 활용한 문법
# book = soup.select("article.product_pod") # 오류나는 문법 (첫번째 인자값만 태그로 인지)


prices = soup.find("div", class_="product_pice")
songs = soup.find_all("#tb_list tr")

title = book.find("h3").find("a")["title"]  # 속성값 가져오기
price = book.find("p", class_="price_color").text

print("제목:", title)
print("가격:", price)
