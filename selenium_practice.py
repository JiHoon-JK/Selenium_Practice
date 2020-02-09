from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
# 크롬을 연다.
driver.implicitly_wait(3)
# 드라이버를 여는데, 3초 정도 기다린다.

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# 조건을 검색해야하는 사이트를 들어간다.
driver.find_element_by_id("id").send_keys("naver_id")
driver.find_element_by_id("pw").send_keys("psd123")
# 조건을 입력해야하는 태그에 대한, ID 값을 찾아서 Send_keys 값으로 입력.
driver.find_element_by_id("log.login").click()
# 로그인 버튼을 클릭한다.

# Naver 페이 들어가기

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')
#
# driver.page_source
