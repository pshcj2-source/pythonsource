# uv pip install matplotlib

import matplotlib.pyplot as plt

'''
# x, y에 0~10까지 넣어주기
x=[a for a in range(0,11)]
y=list(range(0,11))

print('x축',x)
print('y축',y)

# 출력
plt.plot(x,y)
plt.show()
'''

# 2차 함수 => f(x)=x^2
f=lambda x:x**2
x=[x for x in (-10,10)]
y=[f(y) for y in (-10,10)]

print('x축',x)
print('y축',y)

# 출력
plt.plot(x,y)
plt.show()