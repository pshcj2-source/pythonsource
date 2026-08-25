import pandas as pd
import sys
import io

# df1=pd.read_excel('excel_s1.xlsx', header=0)
# # print(df1)

# df1['State']=df1['State'].str.replace(' ','|')  #공백을 | 로 변환
# print(df1['State'])

# # 평균 컬럼 추가 axis=1
# # .round(2) 소수 2자리 반올림
# df1['Avg']=df1[['2018','2019','2020']].mean(axis=1).round(2)
# # print(df1)

# #합계
# df1['Max']=df1[['2018','2019','2020']].sum(axis=1)
# #print(df1)
# #최대값 컬럼 추가
# df1['Max']=df1[['2018','2019','2020']].max(axis=1)

# #최대값 열단위 추가
# max_values=df1[['2018','2019','2020']].max(axis=0)
# # print(max_values)
# #최소값 열단위 추가
# min_values=df1[['2018','2019','2020']].min(axis=0)
# print(min_values)

# #상세 분석 정보
# print(df1.describe())

# #엑셀쓰기
# df1.to_excel('result_s1.xlsx',index=False)

#컬럼 연산 추가
df2=pd.read_excel('excel_s2.xlsx', header=0)
df2[['Units','UnitCost']]=df2[['Units','UnitCost']].astype(int)  #숫자 데이터를 int로 변환
df2['Custom1']=df2['Units']*df2['UnitCost'] #컬럼끼리 곱해서 새로운 컬럼 생성
df2['Custom2']=df2['Total']*10
print(df2)

df2.to_excel('result_s22.xlsx', index=False)
print('완료')


