# === Todo 관리 ===
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 1
# 할 일 내용을 입력하세요: 내용입력...
# 등록되었습니다.
# === Todo 관리 ===
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 2
# --------------------------------------
# 1. [미완료] 강아지 목욕(2026-08-20 12:38:07)
# === Todo 관리 ===
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 3
# 완료 처리할 일 번호를 입력하세요: 1 입력시 완료
# 완료 처리되었습니다.
# === Todo 관리 ===
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 4
# 삭제 처리할 일 번호를 입력하세요: 1 입력시 삭제
# 삭제 처리되었습니다.

# 데이터베이스 테이블 구조
# todo_id 자동증가, PK설정
# title not null
# is_done number(1) default 0
# created_at 작성일자 sysdate

# 데이터베이스 연결

import oracledb
conn = oracledb.connect(user="python_user", password="54321", dsn="localhost/xe") 
cursor = conn.cursor()

# 테이블 생성 => 클래스 생성

Base = declarative_base() 

    cursor.execute(sql)               
except oracledb.DatabaseError as e:    
    (error_obj,) = e.args
    if error_obj.code == 955:
        print(error_obj.message)        
    else:
        raise


# todo 추가

def add_todo():
    '''create'''
    # 할 일 내용을 입력하세요: 내용입력...
    title = input('할 일 내용을 입력하세요').strip()
    # insert 구문 실행
    sql = "insert into todos(title,created_at) values(:1,sysdate)"
    cursor.execute(sql,(title,))
    conn.commit()
    if cursor.rowcount > 0:
        print("등록되었습니다.\n")

def list_todos():
    ''' select '''
    sql = "select * from todos order by todo_id"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f"")

    # todo 내용이 없는 경우

    if not row:
        print("등록된 할 일 목록은 없습니다.\n")
        return
    print("-"*50)
    for row in rows:
        status = "완료" if row[2] == 1 else "미완료"    #1은 완료 2는 미완료
        print(f"{row[0]}. [{status}] {row[1]}({row[3]})")
    print("-"*50)
    print()

        

def update_todo():
    '''완료처리 - update'''
    # 목록 보여주기
    list_todos()
    todo_id = input("완료 처리할 일 번호를 입력하세요: ").strip()
    sql = "update todos set is_done = 1 where todo_id = :1"
    cursor.execute(sql,(todo_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("해당 번호가 없습니다.")
    else:
        print("완료 처리되었습니다.\n")


def delete_todo():
    '''삭제처리 - delete'''
    
    # 목록 보여주기
    list_todos()
    todo_id = input("삭제 처리할 일 번호를 입력하세요: ").strip()
    sql = "delete from todos where todo_id = :1"
    cursor.execute(sql,(todo_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("해당 번호가 없습니다.")
    else:
        print("삭제 처리되었습니다.\n")


def menu():
    while True:
        print("=== Todo")
        print("1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료")

        choice = input("선택 : ")

        if choice == "1":
            add_todo()

        elif choice =="2":
            list_todos()
        elif choice =="3":
            update_todo()
        elif choice =="4":
            delete_todo()
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("번호를 확인해 주세요")    


if __name__== "__main__":
    try:
        menu()
    finally:
        cursor.close()
        conn.close()
