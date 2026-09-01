# -*- coding: utf-8 -*-      
## -*- coding: utf-8 -*-는 단순한 주석이 아니라 파이썬 인터프리터에게 파일의 인코딩 방식을 알려주는 매우 중요한 기능
import pandas as pd
# pandas dataframe -> '엑셀 Cell'과 유사
# 딕셔너리 -> Datafram으로 변환(엑셀에서 열 제목이 딕셔너리에서는 key / 각 행에 들어가는 데이터는 원소)하는 작업에 쓰임

# key=컬럼명, value = 각 학생의 값 리스트

game_data = {
    "이름": ["김민준", "이서연", "박도윤", "최지우", "정하윤"],
    "게임종류": ["롤", "발로란트", "롤", "오버워치", "발로란트"],
    "최고점수": [2450, 1980, 3120, 2760, 2210],
    "플레이시간_시간": [120, 85, 200, 150, 95]
}

# 2. DataFrame 생성
df=pd.DataFrame(game_data)  #df : dataframe
print("=== 전체 데이터 ===")
print(df)


# 3. head() : 기본값은 5
print("\n === head(3) : 상위 3개만 보기 ===")
print(df.head(3))

# 4. info(): 컬럼별 분석(데이터 타입, 결측치 개수, 메모리 사용량)
print("\n === info() : 데이터 구조 보기 ===")
df.info()

# 5. describe(): 숫자 컬럼의 통계 요약(최대,최소,중간,평균,카운트 등)
print("\n === describe() : 숫자 컬럼의 통계 요약 ===")
print(df.describe())

# 6. 컬럼 하나만 뽑아보기 (Series 형태로 반환)
print("\n === '최고점수' 컬럼만 보기 ===")
print(df["최고점수"])
print("타입:", type(df["최고점수"]))

#df["최고점수"]: Series(데이터를 분석하기 위해 사용)
# df[["최고점수"]]: DataFrame(이중 리스트, 타입정도 확인하기 위해 사용) 