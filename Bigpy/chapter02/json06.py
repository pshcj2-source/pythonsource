import simplejson as json 

# 빈 딕셔너리 생성 후 'people' 키에 빈 리스트 할당
data = {}
data['people'] = []
print("초기 데이터:", data)

# 첫 번째 데이터 추가 ('name' 앞의 중복된 따옴표 수정 완료)
data['people'].append({
    'name': 'kim',
    'website': 'naver.com',
    'from': 'Seoul',
    'grade': [95, 77, 89, 91]
})

# 두 번째 데이터 추가
data['people'].append({
    'name': 'park',
    'website': 'google.com',
    'from': 'Busan',
    'grade': [85, 88, 79, 81]
})

# 세 번째 데이터 추가
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [80, 85, 90, 96]
})

print("\n--- 최종 완성된 JSON 데이터 구조 ---")

# json 객체로 파일생성
with open('member.json','w') as outfile:   #직렬화
    json.dump(data, outfile)

with open('member.json','r') as infile:    #역직렬화
    r=json.load(infile)
    for p in r['people']:
        print('Name: '+p['name'])
        print('Website: '+p['website'])
        print('From: '+p['from'])
        t=p['grade']
        grade=""
        for g in t:
            grade=grade+' '+str(g) #grade 숫자를 string화
        print('Grade: '+grade.lstrip())  # lstrip 왼쪽 공백제거, rstrip 오른쪽 공백 제거
        print()