import requests

# param가 필수로 들어가야 요청이 성공하는 API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 37.5665,
    "longitude": 126.9780,
    "hourly": "temperature_2m",
    "timezone": "Asia/Seoul",
}

# API 요청 보내기
res = requests.get(url, params=params)
data=res.json

res=requests.get(url, params=params)
print(res)
data=res.json()
print('-'*37)
print(data)

times=data["hourly"]['time']
temps=data["hourly"]['temperature_2m']

for t, temp in zip(times, temps):
    print(f'{t}:{temp} degree C')

print("최고 기온 :", max(temps))
print("최저 기온 :", min(temps))