import sys
import io
# uv pip install beautifulsoup4
from bs4 import BeautifulSoup 

'''
<html>
<body>
<ul id="cars">
  <li id="ge">Genesis</li>
  <li id="av">Avante</li>
  <li id="so">Sonata</li>
  <li id="gr">Grandeur</li>
  <li id="tu">Tucson</li>
</ul>
</body>
</html>
'''

fp=open("C:/source/pythonsource/Bigpy/Py_Scrap/cars.html", encoding='utf=8')

soup=BeautifulSoup(fp,'html.parser')
print(soup)

# 함수  (수행문이 길 경우 define(함수) 사용)
def car_func(select):
    print("car_func:",soup.select_one(select).string) # string : 태그 빼고 text만 가져오기

# 메인 (아래 모두 동일한 결과)
car_func("#gr")   # # : id 통한 찾기, 가장 단순
car_func("li#gr")  # li이면서 아이디가 gr
car_func("ul>#gr")  # > : ul의 직계자식 중 id가 gr
car_func("#cars #gr") # 띄어쓰기 : 아이디가 #cars이면서 그 아래 어딘가에(후손) 아이디가 #gr
car_func("#cars>#gr") # 아이디가 #cars의 직계자식 중 id가 gr
car_func("li[id='gr']")   # 잘 못찾겠을때.  F12 눌러서 element에서 크롤링하고 싶은 줄에서 우클릭 한다음 copy-> copyXpath
print("-"*37)

# 람다식 (매개변수:q) 수행문이 짧은 경우 람다 많이 사용
car_lambda=lambda q: print("car_func: ", soup.select_oue(q).string)

# 메인
car_func("#gr")   
car_func("li#gr") 
car_func("ul>#gr")  #많이 사용
car_func("#cars #gr") #많이 사용
car_func("#cars>#gr") 
car_func("li[id='gr']")   


print("-"*37)
print("car_func:",soup.select("li")[3].string)   #li 세번째 자식 가지고 와라. select는 select_one만 있고 all은 없다. select만 쓰는게 전체 가지고 오라는 것
print("car_func:",soup.find_all("li")[3].string)  # find는 기본이 한가지 엘리먼트만 가지고 오라는 뜻 내포. find_all이 전체 가지고 오라는 것