import urllib.request as req
import os.path, random
# uv pip install simplejson
import simplejson as json 

#URL 요청
url="https://api.github.com/repositories"

#경로와 파일명
savename="repo.json"

#예외처리
if not os.path.exists(url):    #url 경로가 없다면
    req.urlretrieve(url, savename)

# 객체를 역직렬화(load)   # 받아온 것을 (이사짐을 푸는 것)
item=json.load(open(savename, 'r', encoding='utf-8'))
print('Type: ',type(item))

for i in item:
    print(i["full_name"]+" - "+i["owner"]["url"])

print('-'*50)
# 역직렬화 (loads) - s(String) / 데이터베이스에 이미 저장되어 있는 데이터 읽어오기
itms=json.loads(open(savename, 'r', encoding='utf-8').read())
print('Type: ', type(items))

for it in items:
    print(i["full_name"]+" - "+i["owner"]["url"])