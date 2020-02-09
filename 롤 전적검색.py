from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.op.gg/')

driver.find_element_by_class_name("summoner-search-form__text _suggest").send_keys("호두밭의파수쿤")

driver.find_element_by_class_name("summoner-search-form__button").click()
