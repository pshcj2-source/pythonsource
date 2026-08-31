# ## 문제 2 (난이도 하) — 공개 API 크롤링 (인증 없음)

# ### 학습 포인트

# - `requests`로 REST API 호출
# - JSON 응답 파싱 (중첩 딕셔너리/리스트 접근)
# - JSON 파일로 저장

# ### 요구사항

# 1. `https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,JPY,EUR` 를 이용해 달러 기준 원화, 엔화, 유로 환율을 가져오세요.
# 2. 콘솔에 통화별로 출력하세요.
    
#     ```
#     1 USD = 1385.20 KRW 1 USD = 147.32 JPY1 USD = 0.92 EUR
#     ```
    
# 3. 결과를 `exchange_today.json` 파일로 저장하세요. (조회일자 포함)

# ### 힌트

# - 인증키가 필요 없는 API입니다.
# - 응답 구조에서 `rates` 키 안에 통화별 값이 들어있습니다.



import requests
import csv
from datetime import datetime, timedelta

def get_exchange_rate_trend():
    end_date=datetime.now().strftime('%Y-%m-%d')
    start_date=(datetime.now()-timedelta(days=30)).strftime('%Y-%m-%d')

    # ({start_date}, {end_date})를 사용해 변수에 들어 있는 실제 값(날짜 문자열)을 
    # 문자열 내부에 쏙 집어넣어 동적으로 URL을 완성
    url = f"https://api.frankfurter.dev/v1/{start_date}..{end_date}"
    params = {
        "base": "USD",   # 기준 통화
        "symbols": "KRW, JPY, EUR"
    }

    res=requests.get(url,params=params)
    res.raise_for_status()   # 파이썬의 requests 라이브러리에서 웹 요청(HTTP 요청)이 성공했는지 확인하고, 실패했을 경우 에러를 발생시키는 역할
    data=res.json() 
    # data = res.json()은 서버로부터 받아온 응답(Response) 데이터가 JSON 형식일 때, 
    # 이를 파이썬에서 다루기 편한 딕셔너리(Dictionary)나 리스트(List) 형태의 데이터로 변환해 주는 역할    
    # print(data)
    rates=data['rates'] #{"2026-07-28":{'KRW':1459.45}}   

#     # 날짜순 정렬
    sorted_dates=sorted(rates.keys())

    results=[]
    for date in sorted_dates:
        krw=rates[date]['KRW']
        jpy=rates[date]["JPY"]
        eur=rates[date]["EUR"]
        
        print(f'{date}: {krw:,.2f}원, {jpy:,.2f}엔, {eur:,.2f}유로')
        results.append({"기준날짜" : date, "통화", "환율" : krw})
    print()

    # CSV 저장   
    csv_path = "usd_90days.csv"
    
    with open(csv_path, 'w', newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["날짜" , "통화", "환율"])
        writer.writeheader() # 컬럼 이름 자동으로 씀
        writer.writerows(results) # 최종 저장


    print()
    print(f"CSV 저장 완료: {csv_path}")

if __name__=='__main__':
    get_exchange_rate_trend()