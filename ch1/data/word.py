# 영어타자 프로그램

import random
import time

# word.txt 읽어서 문제를 보여주는거
words = []
with open("./ch1/data/word.txt","r",encoding="utf-8") as f:    #모듈은 가상환경(.venv)에서 가동되서 ch1폴더를 지정해줘야함. 현재 경로는 C:\source\pythonsource> .ipynb확장자는 자동으로 찾아주는데 .py는 아니라서 폴더 상세하게 지정
    for word in f:
        words.append(word.strip())   # strip : 공백/엔터 제거


# start = time.time()
start = time.time()
# n : 반복횟수 카운트, corr_cnt : 정답개수 카운트
n, corr_cnt = 1, 0
# while  구문
# 섞는다. random.shuffle()
# 임의로 하나 추출 random.choice
while n <=5:
    random.shuffle(words)
    q=random.choice(words)
    print(f'Q{n}')
    print(q)
# input()    
    answer = input()
# input 결과에 따라 정답!! or 오타!!
    if answer.strip()==q.strip():
        print("정답!!")
        corr_cnt+=1
    else:
        print("오타!!")
# 문제개수 추가
    n +=1


# (5문제 출제)

# 끝난 시간
end = time.time()


# 문제 5문제 출제
# 정답 개수
# 

# 총 게임시간 출력
et = end-start
et=format(et,".3f")
# 출력문 => 게임시간 : 10초, 정답개수 : 3개

print(f'게임시간 : {et}초, 정답개수 : {corr_cnt}개')
# 최종적으로 3개 이상 정답인 경우 "합격" 메세지, 아닌경우 불합격

if corr_cnt >=3:
    print("합격")
else:
    print("불합격")

