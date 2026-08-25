import sys
import io
from bs4 import BeautifulSoup 

html="""
<html>
<body>
  <h1>Find VS Select 차이</h1>
  <p>CSS 선택자 사용 및 다중반환</p>
  <p>태그선택자 사용 및 단일반환</p>
</body>
</html>
"""

print('html -> ',html)
print('-'*37)
soup=BeautifulSoup(html, 'html.parser')
print('soup->',type(soup))
print(soup)
print('prettify',soup.prettify())   #prettify는 모든 태그와 들여쓰기/줄단위 간격을 맞춰서 보여줌

#---------------------------------------
h1=soup.html.body.h1
print("h1 ->",h1)
p1=soup.html.body.p
print("p1 ->", p1)
p2=p1.next_sibling.next_sibling    #next_sibling은 다음 줄인데 #p 는 문단이라서. 글 덩어리 다음 엔터 한번 더 치는거라서 next sibling을 두번 쳐야 다음 내용이 나옴. br(한 줄 엔터) 치는거랑 다름()
print('p2 ->', p2)
p3=p1.previous_sibling.previous_sibling    #previou_sibling은 이전 줄인데 #p 는 문단이라서. 글 덩어리 다음 엔터 한번 더 치는거라서 두번 쳐야 윗 문단 내용이 나옴.
print('p3 ->', p3)    