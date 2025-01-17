from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.config.appConfig import getConfig

appConfig = getConfig()

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(appConfig['loginLocation'])
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()