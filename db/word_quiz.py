# csv 파일의 내용을 테이블에 insert 하기(단, 테이블이 비어 있는 경우만 삽입)

# 테이블의 내용을 읽어서 무작위로 추출 후 내기
# Question #1 : 'apple'의 뜻은?
# 1. 버스
# 2. 남편
# 3. 수줍은
# 4. 사과

# 결과 : 3 / 5 정답
# 결과를 테이블에 저장하기
# total, correct, regdate

import oracledb 
import random
import csv

conn = oracledb.connect(user="python_user", password="54321", dsn="localhost/xe") 
cursor = conn.cursor()


def load_words_from_csv(path="./words.csv"):
    '''csv 파일을 읽어서 튜플 리스트로 반환'''
    # [(wife,아내), (apple,사과)]

    pairs = []
    with open(path,"r",encoding="utf-8") as f:                
        reader = csv.DictReader(f)
        for row in reader:            
            pairs.append((row['word'].strip(), row.get('meaning').strip()))
    return pairs

def seed_words_if_empty():
    '''words 테이블이 비어 있으면 csv 파일 내용을 읽어서
    (load_words_from_csv()) 넣기'''

    cursor.execute("select count(*) from words")
    count = cursor.fetchone()[0]    

    if count > 0:
        return

    # [(wife,아내), (apple,사과)]
    pairs = load_words_from_csv()
    # insert
    sql = "insert into words(word,meaning) values(:1,:2)"
    cursor.executemany(sql, pairs)
    conn.commit()

    print(f'csv 단어 데이터 {cursor.rowcount}개를 등록했습니다\n')

def run_quiz():
    ''' 무작위 문제 추출 random.sample()
    1) all_words = words 테이블 읽기
    2) 무작위 5문제 추출 random.sample()
    3) all_words 문제를 제외한 내용을 섞은 후 거기서 틀린 meaning 추출(3개)
       문제출제 APPLE,사과 + MEANING => 보기출제. 정답의 번호는 랜덤으로
    4) 답변입력받은 후 정답 맞는지 확인
    5) 최종결과 입력
    '''
    cursor.execute("select word, meaning from words")
    all_words = cursor.fetchall()

    # 정답 개수
    correct = 0
    # 문제 개수
    total = 5

    questions = random.sample(all_words, total)

    for idx, (word,meaning) in enumerate(questions, start = 1):
        # enumerate : 리스트, 딕셔너리, 튜플 등에 인덱스를 부여하는 함수 (기본 0부터 시작)
        # distractors = []
        # for w, m in all_words:
        #     if w!=word:
        #         distractors.append(m)
        
        distractors = [m for w, m in all_words if w!=word]        
        random.shuffle(distractors)
        # 보기 생성
        choices = distractors[:3] + [meaning] 
        # 항상 같은 번호가 정답이 안되도록 섞기
        random.shuffle(choices)
        # choices = ['아내', '비행기', '사과', '자전거']

        #문제 출제
   
        print(f"Question #{idx} : {word}의 뜻은?")
        # 보기 출제
        for i, c in enumerate(choices, start=1):
            print(f' {i}, {c}')
        # 정답 입력받기 => 1 or 2 => 번호
        answer = input("정답 번호 입력 : ").strip()

        # 정답(지하철) 사용자가 입력한 답(1)과 비교
        try:
            selected = choices[int(answer)-1]   # index는 0부터 시작
        except:
            selected = None
        
        if selected == meaning:
            print("Pass!!\n")
            correct +=1
        else:
            print(f"Wrong!! 정답 : {meaning}\n")
    print(f'=== 최종 결과 : {correct} / {total} 정답/문제 === \n')

    # 결과를 테이블에 저장하기
    
    sql = "insert into quiz_records(total,correct,regdate) values(:1,:2,sysdate)"
    cursor.execute(sql,(total,correct))
    conn.commit()



if __name__== "__main__":
    try:        
        seed_words_if_empty()
        run_quiz()        

    finally:
        cursor.close()
        conn.close()