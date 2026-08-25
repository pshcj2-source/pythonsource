import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse 

# 내 공인 IP주소를 알려주는 API
# 본래 행안부 사이트 https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012   ?:구분자. 프론트앤드?백앤드



url = "http://www.encar.com/"
# encar처럼 차단 봇이 있는 사이트는 기본 User-Agent로 요청하면 403/406 보안 에러가 발생하여 정상 페이지를 받지 못함

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }
)

mem = urllib.request.urlopen(req)
print(type(mem))
print("geturl : ", mem.geturl())
print("status : ", mem.status) #200

print("headers : ", mem.getheaders())
print("info : ", mem.info()) # header 정보를 행단위로 보여줌
print("getcode : ", mem.getcode()) # mem.status

# 서버가 사용하는 문자 인코딩, 없으면 utf-8로 해봐
encoding=mem.info().get_content_charset() or 'utf-8'   #사이트에 적용한 인코딩방법으로 인코딩 해주고 없으면 utf-8을 적용해주기                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

# 바이트를 500개만 자르면 멀티바이트(한글,한자,특문 등) 중간에 끊김 => 에러 발생가능
# unicodeDecodeError가 날 수 있으므로 errors='ignore' 처리
raw=mem.read(500)
print("read:", raw.decode(encoding,errors='ignore'))

print(urlparse('http://www.encar.co.kr?test=test').query)