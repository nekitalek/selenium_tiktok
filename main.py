import time
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=uc.Chrome()
driver.get('https://www.tiktok.com/foryou?lang=ru')
delay = 5
time.sleep(delay)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(delay)

element = driver.find_element(By.XPATH, '//*[@id="main-content-homepage_hot"]/div[1]/div[1]/div/div[1]/div[1]/a[2]')
element.click()
time.sleep(delay)