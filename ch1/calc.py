# 사용자 정의 모듈
# 함수 2개 정의
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)
    
# 만들어진 모듈이 잘 돌아가는지 테스트
if __name__ == "__main__": # 모듈 테스트한 코드들과 결과값이 임포트한 모듈에도 출력되는 것을 방지 하는 코드.  일일이 #을 붙이기 힘들떄
    print(add(9,5))      #ctrl + / 누르면 한번에 # 주석 처리 및 취소 가능
    print(sub(9,5))
    print(mul(9,5))
    m=Math()
    print(m.solv(6))

