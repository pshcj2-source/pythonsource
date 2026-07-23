# calc.py 모듈 사용
# import calc

# print(calc.add(7,5))
# print(calc.sub(7,5))

from calc import add, sub, Math
print(add(7,5))
print(sub(7,5))

math=Math()  #클래스는 사용전 객체 선언부터 해야함
print(math.solv(5))
math = Math()
print(math.solv(5))
from calc import *
print(mul(7,5))



from mod3 import *   
from mod2 import *   # 여러 모듈에서 * 로 불러왔을때 정의된 모듈 용어가 같은 경우 최신으로 import한 용어로 정의된 명령대로 실행시킨다.
print(max(7))