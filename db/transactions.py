import oracledb
from datetime import datetime
    

conn = oracledb.connect(user="python_user", password="54321", dsn="localhost/xe") 
cursor = conn.cursor()

def add_transaction():
    '''create'''
    # 할 일 내용을 입력하세요: 내용입력...
    tx_type = input('"수입" 또는 "지출"을 입력하세요').strip()
    if tx_type in ("수입", "지출"):
        pass
    else:
        print('잘못된 입력입니다. 순순히 "수입" 또는 "지출"을 입력한다면 유혈사태는 발생하지 않을 것입니다.')
        return    
    amount = int(input('금액을 입력하세요').strip())   
    memo = input('내역을 입력하세요').strip()
    reg_date = input('회계일자를 입력하세요 ex)YYYY-MM-DD, 엔터 시 오늘 날짜').strip()

    if not reg_date: #엔터친 경우 값이 없어서 false
        reg_date = datetime.now().strftime("%Y-%m-%d")

    # insert 구문 실행
    sql = "insert into transactions(tx_type,amount,memo,reg_date) values(:1,:2,:3,:4)"    
    cursor.execute(sql,(tx_type,amount,memo,reg_date))
    conn.commit()

    if cursor.rowcount>0:
        print("등록되었습니다.\n")


def list_transaction():
    '''reg_date 오름차순으로 조회'''
    # 번호 [지출] 300,000원 - 용돈(2026-08-18)
    pass
    sql = "select tx_id,tx_type,amount,memo,reg_date from transactions order by reg_date asc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f"")

    # 내용이 없는 경우

    if not row:
        print("등록된 가계부 목록은 없습니다.\n")
        return
    print("-"*50)
    for row in rows:       
        print(f"{row[0]}. [{row[1]}] {row[2]}원 - {row[3]}({row[4]})")
    print("-"*50)
    print()



def monthly_summary():

    month = input("조회할 년,월을 입력하세요 (YYYY-MM):").strip()

    sql = """
    SELECT tx_type, sum(amount) FROM TRANSACTIONS 
    WHERE reg_date LIKE :1 GROUP BY tx_type"""
    cursor.execute(sql,(month+'%',))
    rows = cursor.fetchall()
    for row in rows:
        print(f"")

    # 내용이 없는 경우

    if not row:
        print("요청하신 해당 월 가계부 내역은 없습니다.\n")
        return
    print("-"*50)
    for row in rows:       
        print(f"{row[0]} : {row[1]}원")
    print("-"*50)
    print()

def menu():
    # 1. 내역 추가 2. 전체 조회 3. 월별 합계 4. 종료
    while True:
        print("=== 가계부 ===")
        print("1. 내역 추가 2. 전체 조회 3. 월별 합계 4. 종료")

        choice = input("선택 : ")

        if choice == "1":
            add_transaction()

        elif choice =="2":
            list_transaction()
        elif choice =="3":
            monthly_summary()
        elif choice =="4":            
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