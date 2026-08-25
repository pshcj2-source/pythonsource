import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse 
from bs4 import BeautifulSoup

# 내 공인 IP주소를 알려주는 API
# 본래 행안부 사이트 https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012

url = "http://www.encar.com/"
# encar처럼 차단 봇이 있는 사이트는 기본 User-Agent로 요청하면 403/406 보안 에러가 발생하여 정상 페이지를 받지 못함


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
    }

req = urllib.request.Request(url, headers=headers)
mem = urllib.request.urlopen(req)


# #사이트에 적용한 인코딩방법으로 인코딩 해주고 없으면 utf-8을 적용해주기     
encoding=mem.info().get_content_charset() or 'utf-8'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
html = mem.read().decode(encoding, errors='ignore')

soup=BeautifulSoup(html, 'html.parser')
print(soup)

# 1. title 태그에서 텍스트 가져오기
title = soup.select_one("title")
print('title: ', title)
print('title: ', title.text) # 자식 텍스트가 여러개일 경우 합침
print('title: ', title.string)  # 자식이 텍스트 하나일 경우 사용가능   # 내차팔기, 내차사기 | Null로 나오는 경우가 생김

# 2. 속성값을 활용하여 가져오기 (meta name="description")
description=soup.select_one('meta[name="description"]')
print("description : ",description.get("content") if description else "없음") #description 내용이 있으면 반영 없으면 "없음"

keywords = soup.select_one('meta[name="keywords"]')
print("keyword :", keywords.get("content") if keywords else "없음")

naver_verify = soup.select_one('meta[name="naver-site-verification"]')
print("naver-site-verification :", naver_verify.get("count") if naver_verify else "없음")
