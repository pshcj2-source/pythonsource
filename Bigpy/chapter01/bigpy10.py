import matplotlib.pyplot as plt

# 계절별 서울/부산 지역 온도 데이터 정의
temperatures = [3.3,34.5,14.2,-10]
x=list(range(4))
x_lables = ['Spring','Summer','Fall','Winter']

# bar 차트
plt.title("Bar chart")
plt.bar(x, temperatures)
plt.xticks(x, x_lables)  
plt.yticks(sorted(temperatures))  #y값 정렬
plt.xlabel("seasons") #x축 제목
plt.ylabel("temperatures") #y축 제목
plt.show() 