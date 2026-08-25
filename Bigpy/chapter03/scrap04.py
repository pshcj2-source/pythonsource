import sys
import io
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""



soup=BeautifulSoup(html, 'html.parser')
# print('prettify',soup.prettify())

# <a> 태그 중에서 찾기
a=soup.find_all("a", string="daum") #<a> 태그에 있는 내용 중에 문자열로 daum이 포함됨 것
b=soup.find_all("a", string=["daum","naver"])
c=soup.find_all("a", limit=2) # a 태그에 있는 내용 중에 위에서 두 번째 까지
d=soup.find("a") # = select_one
print('a', a)
print('b', b)
print('c', c)
print('d', d)
# daum과 google을 찾고 싶을때
links = soup.find_all('a')[1:3]
for e in links:
    print('e',e,end=', ')

for f in links:
    href=f.attrs['href']
    print('href ->', href)
    text=f.string # <a href="https://www.google.com">google</a>
    print('text ->', text)

# URL조인
baseUrl="http://test.com/html/a.html"

print(urljoin(baseUrl, "sub/c.html"))   # http://test.com/sub/c.html
print(urljoin(baseUrl, "../index.html"))   # http://test.com/index.html
print(urljoin(baseUrl, "../img/ho.png"))   # http://test.com/img/ho.png
print(urljoin(baseUrl, "../css/ho.css"))   # http://test.com/css/ho.css