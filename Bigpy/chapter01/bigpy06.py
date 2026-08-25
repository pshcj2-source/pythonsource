# numpy: 고성능의 수치계산 지원(C언어로 구성) 배열, 삼각함수, 통계공식 등 지원
import numpy as np

# 수치 계산용 배열 np.array
arr=np.array([1,2,3])
print(arr)
print(type(arr))

print('----------')
matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)

print('----------')
A=[1,2]
B=[1,1]
C=A+B
print(C)
# [1, 2, 1, 1]

print('----------')
A=np.array([[1,2],[3,4]])
B=np.array([[1,1],[1,1]])
C=A+B
print(C)
# [[2 3]
# [4 5]]

print('----------')
AA=np.array([[1,2],[3,4]])
k=10
Ak=k*AA
print(Ak)
# [[10 20]
# [30 40]]
