from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


# https://googlechromelabs.github.io/chrome-for-testing/ 여기 사이트에서 현재 구글 버전에 맞는 드라이버를 다운 받아서 압축풀고 아래 경로에 붙여넣기
chrome_options=Options()
s=Service("C:/source/pythonsource/Bigpy/Py_Scrap/chromedriver/chromedriver.exe")

driver=webdriver.Chrome(service=s, options=chrome_options)

driver.set_window_size(1920,1080) #화면크기
driver.get('https://m.ruliweb.com/')
time.sleep(3) # 로드시간 3초 
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_Scrap/img/website33.png")

driver.set_window_size(1920,1080) # 화면크기
driver.get('https://daum.net')
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_Scrap/img/website22.png")

driver.quit()

print('스크린샷 성공')