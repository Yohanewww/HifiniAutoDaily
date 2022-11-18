import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import random

options = Options()
# driver = webdriver.Chrome(options=options)

# try:
#     driver.find_element_by_xpath("")

def sign_in():
    driver = webdriver.Chrome()
    url = 'https://hifini.com/user-login.htm'
    driver.get(url)
    # driver.maximize_window()
    time.sleep(5)
    usernameElement = driver.find_element(By.XPATH, '//*[@id="email"]')
    usernameElement.click()
    time.sleep(random.uniform(1,3))
    usernameElement.send_keys('')
    pwElement = driver.find_element(By.XPATH, '//*[@id="password"]')
    pwElement.click()
    time.sleep(random.uniform(1,3))
    pwElement.send_keys('')
    captchaElement = driver.find_element(By.XPATH, '//*[@id="captcha"]')
    captchaElement.click()
    time.sleep(10)




# confirmElement.click()

sign_in()
