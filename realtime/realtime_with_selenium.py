from selenium import webdriver
# Keys 패키지는 클릭과 같은 동작을 python이 인식할 수 있게끔 해주는 패키지
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://www.naver.com'

# 크롬드라이버(chromedriver)가 있는 장소를 괄호 안에 기입
driver = webdriver.Chrome('./chromedriver')
# webdriver은 chrome크롬과 같은 웹브라우저 제어함.
driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

# 여기서 더보기 버튼을 왜..? 더보기 버튼이 뭐지
# more_button = driver.find_elements_by_class_name('_moreBtn')

# for _ in range(3):
#    more_button.click()
#    sleep(2)

###########

realtimes = driver.find_elements_by_css_selector(
    '#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul')

print(realtimes)
texts = [realtime.text for realtime in realtimes]

with open('realtime.txt', 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text + '\n')

driver.quit()
print(texts)
