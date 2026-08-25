import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# class="product_pod"인 article 태그 전체 선택
books = soup.select("article.product_pod")



count=0
for book in books:
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    rating = book.select_one("p.star-rating")["class"][1]  # 두번째 class가 별점(One, Two, Three...)

    if count < 10:
        print(f"{title} | {price} | 별점: {rating}")
        count+=1
    if count >= 10:
        break
   