# 롤 게임의 랭킹 순위와 값을 가져오는 크롤링
from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


driver = webdriver.Chrome('./chromedriver')

# 롤 전적 검색 사이트 입력
driver.get('https://www.op.gg/')

# xpath 를 통해서, 직관적으로 클래스를 끌어오기 / 검색 아이디 이름 : 호두밭의파수쿤
# https://wkdtjsgur100.github.io/selenium-xpath/ : xpath 관련 정보글

driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/input').send_keys("호두밭의파수쿤")

#전적검색을 위해서 버튼 누르기
driver.find_element_by_class_name("summoner-search-form__button").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')

lol_info = soup.select('#body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header')

image = '대표 아이콘: ' + 'http:' + str(lol_info.select_one('div.Face > img').attrs['src']).replace('//', '')
print(image)
ID = '아이디 : ' + lol_info.select_one('div.Profile > div.Information > span.Name').text
print(ID)
Rank = lol_info.select_one('div.Profile > div.Information > div > div > a').text
print(Rank)

lol_info_data = {
    'image' : image,
    'ID' : ID,
    'Rank' : Rank
}
print(lol_info_data)

#db.lol_info.insert_one(lol_info_data)
