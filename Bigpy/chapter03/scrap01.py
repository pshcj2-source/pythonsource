import sys
import io
import urllib.request as dw

imgUrl="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MTdfMTgw%2FMDAxNTk0OTYzOTUwOTYw.IKn6Jj8o-SoRTbZI3c9fWfqbRlXp8Kn6mm2mrUZj2Vcg.g-mWpamKt2jzpt0gw3B3jeC9z3ozWwsF3czu6h3XHK0g.PNG.ohj3437%2F2020-07-17_14%253B32%253B11_%25288%2529.png&type=sc960_832"
htmlURL="http://google.com"

# print('방법1')
# savePath1="C:/source/pythonsource/Bigpy/imgtest1.jpg"
# savePath2="C:/source/pythonsource/Bigpy/index.html"
# dw.urlretrieve(imgUrl, savePath1)
# dw.urlretrieve(htmlURL, savePath2)

print('방법2')
f1=dw.urlopen(imgUrl).read()
f2=dw.urlopen(imgUrl).read()

savePath1="C:/source/pythonsource/Bigpy/imgtest2.jpg"
savePath2="C:/source/pythonsource/Bigpy/index2.html"

saveFile1=open(savePath1, 'wb')
saveFile1.write(f1)
saveFile1.close()   #무조건 오픈하면 클로즈 해줘야함

print('방법3')
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f1)

print("save 완료")

