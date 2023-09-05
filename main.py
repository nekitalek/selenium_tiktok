import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get('https://www.tiktok.com/foryou?lang=ru')
time.sleep(10)

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(10)

element = driver.find_element(By.XPATH, '//*[@id="main-content-homepage_hot"]/div[1]/div[1]/div/div[1]/div[1]/a[2]')
element.click()
time.sleep(10)