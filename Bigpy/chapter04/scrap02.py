import requests, json

s=requests.Session()
url='http://httpbin.org/get' 
r = s.get("https://jsonplaceholder.typicode.com/posts/1")
print("1: ", r.text)
print("2: ", r.json())
print("3 : ", r.json().keys())
print("4 : ", r.json().values())
print("5 : ", r.encoding)
print("6 : ", r.content)
print("7 : ", r.raw)

print("-"*37)
# 세션 시작 
with requests.Session() as s:
    # Get으로 스트리밍 요청
    r=s.get('http://httpbin.org/stream/20', stream=True)
    if r.status_code==200:
        # 스트리밍된 응답의 각 라인을 반복구조로 로드함
        for line in r.iter_lines(): #내용 없을때까지 읽어오기
            # 라인을 디코드하고 출력
            if line:
                # json으로 파싱해서 사용 (파싱 : 구조를 만드는 것)
                data=json.loads(line.decode('utf-8'))
                print(data)
    else:
        print(f'요청을 실패하였습니다. 상태코드: {r.status_code}')