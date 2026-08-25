import pandas as pd
import numpy as np
import openpyxl

# 첫번째 시트 읽어오기
df=pd.read_excel('excel_s1.xlsx', sheet_name=0, engine='openpyxl')
# print(df)
# print(df.head())  # 상위 5개
print(df.tail())   #하위 5개
print('-'*50)

df=pd.read_excel('excel_s1.xlsx', sheet_name=0, skiprows=[1])
print(df.head())   #상위 5개
print('-'*50)
df=pd.read_excel('excel_s1.xlsx', sheet_name=0, skiprows=[1], skipfooter=5)
print(df.tail())   #하위 5개
print('-'*50)

df=pd.read_excel('excel_s1.xlsx', header=0)
print(list(df))  # 헤더만 리스트로 출력
print(list(df.columns.values))

# 전처리 
# ^Unnamed: Unnamed로 시작하는 열
df=df.loc[:,~df.columns.str.contains('^Unnamed')]  # Unnamed 컬럼명 제거
# na_values='...' => null     # 값이 없는 것 제외

#6만 이상값만 표시하고 그 아래값은 None 처리
df=pd.read_excel('excel_s1.xlsx', header=0, na_values='...', converters={"2019":lambda w:w if w>60000 else None}) 