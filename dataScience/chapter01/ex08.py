# -*- coding: utf-8 -*- 

import pandas as pd

"""
- groupby()로 "묶어서 요약"
- 여러 통계 함수(mean, max, count 등)를 동시에 적용하는 agg()
- groupby는 "반별로 나눈다 -> 나눈 그룹마다 계산한다 -> 다시 합친다(split-apply-combine)"
- agg()에 여러 함수를 리스트/딕셔너리로 넘기면 한 번에 여러 통계를 볼 수 있음
"""

df = pd.read_csv("c:/source/pythonsource/dataScience/data/class_scores.csv", encoding="utf-8-sig")
print("=== 원본 데이터 (상위 10개) ===")
print (df.head(100))


# 1. 반별 평균 점수
avg_by_class=df.groupby("반")["점수"].mean()
print("\n === 반별 평균 점수 ===")
print(avg_by_class)

# 2. (반 + 과목) 별 평균 점수(여러 컬럼을 그룹화)
avg_by_class_subject=df.groupby(["반","과목"])["점수"].mean()  #리스트로 묶어줌
print("\n ===반별 x 과목별 평균 점수 === ")
print(avg_by_class_subject)

# 3. agg() : 반별 점수에 대한 (평균, 최댓값, 최소값, 인원수)를 한번에
summary=df.groupby("반")["점수"].agg(["mean", "max", "min", "count"])
print("\n === 반별 평균 점수 ===")
print(summary)

# 4. 과목별로 어떤 반이 가장 잘했는지 확인(표 형태로 반환, unstack())
pivot_like=df.groupby(["과목","반"])["점수"].mean().unstack()
print("\n=== 과목별 x 반별 평균 점수표 ===")
print(pivot_like)

# 5. 그룹별 평균 최고점자 정보: sort_values + groupby => head
top_scores=df.sort_values("점수", ascending=False).groupby("반").head(1)
print("\n=== 반별 최고 득점자 점수표 ===")
print(top_scores)

student_mean = df.groupby(["반", "이름"])["점수"].mean().reset_index()
top_student = student_mean.sort_values("점수", ascending=False).head(1)
print("\n=== 전체 학생 중 평균 점수가 가장 높은 학생 ===")
print(top_student)

# 6. 반별 점수를 기준으로 순위(단, 동점자는 같은 순위)
df["반내순위"]=df.groupby("반")["점수"].rank(ascending=False, method="min")
top3_with_rank=df[df["반내순위"] <=3].sort_values(["반","반내순위"])
print(top3_with_rank)