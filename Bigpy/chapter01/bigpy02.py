import pickle
# pickle 모듈은 파이썬 객체를 파일로 저장하고 읽어들임
# 저장된 상태에서 프로그램이 종료되면 객체는 자동 소멸됨 [작업끝나면 객체(object)를 지워야하는데 객체를 강제로 안지워도 됨]

# 피클 사용하지 않는 일반적 사용법 예시
f=open('setting.txt','rb')   #read binary 
setting=pickle.load(f, encoding='utf-8')   # load : 파일 읽어올떄

f.close()   

print(setting)