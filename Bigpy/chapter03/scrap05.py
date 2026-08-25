import sys
import io
from bs4 import BeautifulSoup 

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 최고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html, 'html.parser')
# print('prettify',soup.prettify())
h1=soup.select_one("div#main > h1").string  # 스트링만 추출
print('h1: ', h1)
li_list=soup.select("div#main > ul.lecs > li")
print('li_list:', type(li_list))  # 배열이라서 줄이 여러개라 string만 추출이 안되서 아래처럼 for문으로 추출

for li in li_list:
    print('li -> ', li)
    print('li -> ', li.string)

