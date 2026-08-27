import datetime #날짜 범위 설정
# uv pip install finance-datareader
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 깨짐 방지 (Windows 기준)
mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 조회 시작
start=datetime.datetime(2024,2,19)
# 조회 마감
end =datetime.datetime(2026,8,27)

# 구글 : google finance => https://ww.google.com/finance/?h1=ko
# 한국거래소 상장종목 전체
df_krx=fdr.StockListing('KRX') #KRX : Korea Exchange 한국거래소 (KOSPI, KOSDAQ, KONEX) 정보 요청
# 리스트 10개 출력
print(df_krx.head(10))
print(df_krx.index)
print(df_krx['Stocks'])
print(df_krx.iloc[0]) # 첫번째 종목의 정보
print(df_krx.describe())

# 미국거래소 상장종목 중 아마존 금융정보
df_amz=fdr.DataReader('AMZN',start,end)
print(df_amz.index)
print(df_amz.iloc[0])       
print(df_amz.loc['2026-08-26']) #iloc는 숫자를 받고 loc는 문자를 받는다.
print(df_amz.describe())

#
df_goog=fdr.DataReader('GOOG',start,end)
print(df_goog.index)
print(df_goog.iloc[0])  # 첫번째 종목의 정보  
print(df_goog.loc["2026-08-26"])  #iloc는 숫자를 받고 loc는 문자를 받는다.
print(df_goog.describe())



# 1) 아마존 vs 구글 종가 추이 비교 (하나의 그래프에)
plt.figure(figsize=(14, 6))
plt.plot(df_amz.index, df_amz["Close"], label="Amazon (AMZN)", color="orange")
plt.plot(df_goog.index, df_goog["Close"], label="Google (GOOG)", color="blue")
plt.title("아마존 vs 구글 종가 추이 (2023.02 ~ 2024.07)")
plt.xlabel("날짜")  #de_amz index
plt.ylabel("종가 (USD)")
plt.legend()
plt.grid(True, alpha=0.3)   #창 크기 넘어가면 잘라주기
plt.tight_layout()
plt.savefig("amz_goog_close_compare.png", dpi=150)
plt.show()

# 2) 아마존 캔들스틱 느낌 - 고가/저가/종가 밴드
plt.figure(figsize=(14, 6))
plt.fill_between(
    df_amz.index,
    df_amz["Low"],
    df_amz["High"],
    alpha=0.2,
    color="orange",
    label="고가-저가 범위",
)
plt.plot(df_amz.index, df_amz["Close"], color="darkorange", label="종가")
plt.title("Amazon (AMZN) 주가 변동 범위")
plt.xlabel("날짜")
plt.ylabel("가격 (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("amz_price_range.png", dpi=150)
plt.show()


# 3) 거래량 비교 (막대그래프)
fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
# 첫칸 막대 그래프(x축의 날짜별 y축 거래량)
axes[0].bar(df_amz.index, df_amz["Volume"], color="orange", width=1)
axes[0].set_title("Amazon 거래량")
axes[0].set_ylabel("거래량")

axes[1].bar(df_goog.index, df_goog["Volume"], color="blue", width=1)
axes[1].set_title("Google 거래량")
axes[1].set_ylabel("거래량")
axes[1].set_xlabel("날짜")

plt.tight_layout()
plt.savefig("amz_goog_volume.png", dpi=150)
plt.show()

# 4) 수익률(%) 비교 - 시작일 대비 등락률
# de_amz['Close'].iloc[0] : 첫 번째날 종가
# 모든 종가를 시작일 종가로 나눔 (시작가가 100달러 인데 오늘 종가가 120 (120/100=1.2) -1= 0.2*100)
amz_return = (df_amz["Close"] / df_amz["Close"].iloc[0] - 1) * 100
goog_return = (df_goog["Close"] / df_goog["Close"].iloc[0] - 1) * 100

plt.figure(figsize=(14, 6))
plt.plot(amz_return.index, amz_return, label="Amazon 수익률(%)", color="orange")
plt.plot(goog_return.index, goog_return, label="Google 수익률(%)", color="blue")
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.title("아마존 vs 구글 누적 수익률 비교 (시작일 대비 %)")
plt.xlabel("날짜")
plt.ylabel("수익률 (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("amz_goog_return_compare.png", dpi=150)
plt.show()

print("\n시각화 완료 - 이미지 4개 저장됨")