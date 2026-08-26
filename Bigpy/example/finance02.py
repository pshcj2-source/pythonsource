# 크롤링 차단되어있는 사이트 Fake-user를 생성하여 자료 끌고 오는 방법
'''
BeautifulSoup: 수집한 HTML 코드를 파싱(분석)하여 원하는 데이터를 쉽게 추출할 수 있게 도와주는 라이브러리입니다.
urllib.request as req: 파이썬 내장 라이브러리로, 웹 페이지에 접속해서 HTML 문서를 다운로드(요청)할 때 사용합니다.
sys, io: 시스템 관련 설정이나 입출력 인코딩 처리를 할 때 주로 함께 쓰입니다.
json: 수집한 데이터를 JSON 형식으로 저장하거나 다룰 때 사용합니다.
fake_useragent (UserAgent): 접속할 때마다 랜덤한 가짜 브라우저 정보(User-Agent)를 생성해 주는 라이브러리입니다. 
(주석에 있는 # uv pip install fake-useragent 명령어로 설치할 수 있습니다.)'''


from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import json
# uv pip install fake-useragent
from fake_useragent import UserAgent

# Fake Headers 정보
ua = UserAgent()

# 헤더정보
headers = {
    "User-Agent": ua.random,  # 가짜 브라우저
    "referer": "http://finance.daum.net/",
}
'''
ua.random: 스크래핑을 차단하는 사이트들은 똑같은 프로그램(스크립트)이 계속 접속하면 차단해 버립니다. 
이를 피하기 위해 크롬, 사파리, 엣지 등 다양한 브라우저의 접속 정보를 
랜덤하게 바꿔서 마치 실제 사람이 브라우저로 접속하는 것처럼 속입니다.
referer: "어떤 경로를 통해 이 웹사이트에 접속했는지"를 알려주는 주소입니다. 
서버에 "이전 페이지(여기서는 다음 금융)에서 링크를 타고 넘어왔다"고 신호를 주어, 
외부 프로그램의 직접 접근 의심을 줄여주는 역할을 합니다.'''

# 주식요청 url
url="http://finance.daum.net/api/serch/ranks?limit=10"
# 요청
res=req.urlopen(req.Request(url, headers=headers)).read().decode('utf- 8')
#print('res: ',res)
rank_json=json.loads(res)['data']


# 중간확인
# print("중간확인: ", rank_json, '\n')

for elm in rank_json:
    print(
        "순위:{}, 금액:{}, 회사명:{}".format(
            elm["rank"], elm["tradePrice"], elm["name"]
        )
    )