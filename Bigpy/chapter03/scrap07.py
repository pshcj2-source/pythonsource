import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse 

# 내 공인 IP주소를 알려주는 API
# 본래 행안부 사이트 https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012

API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"


# 딕셔너리
values={
    'ctxCd':'1012'
}
print('before',values)
params=urllib.parse.urlencode(values) # html -> text
print('after',params)

# 요청
url=API+"?"+params     # "?" 프론트앤드와 백앤드를 구별하는 식별자   API로 끌어올때 제이슨 형식으로 요청해야하는 방식이 많음
print("요청 url", url) # https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012

# 읽기
data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")
print(text)