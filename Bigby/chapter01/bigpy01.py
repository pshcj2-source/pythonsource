import pickle
# pickle 모듈은 파이썬 객체를 파일로 저장하고 읽어들임
# 저장된 상태에서 프로그램이 종료되면 객체는 자동 소멸됨 [작업끝나면 객체(object)를 지워야하는데 객체를 강제로 안지워도 됨]

# 피클 사용하지 않는 일반적 사용법 예시
# f=open('setting.txt','wb')
# setting=[{'title':'python program'},{'author':'soldesk'}]
# pickle.dump(setting,f)
# f.close    #클로즈를 반드시 해주어야함


f=open('setting2.txt','wb')
try:
    setting=[{'title':'python program'},{'author':'soldesk'}]
    pickle.dump(setting,f)
except Exception as e:
    print(e)
finally:
    f.close()