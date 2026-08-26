from bs4 import BeautifulSoup
import urllib.request as req
import requests
import os
from playwright.sync_api import sync_playwright

# 주식 요청 url
url = "http://finance.naver.com/sise/"

# 요청
print(requests.get(url).encoding)  # euc-kr
res = req.urlopen(url).read().decode("euc-kr")
print("res", res)

soup = BeautifulSoup(res, "html.parser")
print(soup)

top10 = soup.select("#siselist_tab_0 > tr")

i = 1
print("오늘의 최고 상한가 종목")
for e in top10:
    if e.find("a"):
        print(i, e.select_one(".tltle").string)
        i += 1
print("---------------------------------------")