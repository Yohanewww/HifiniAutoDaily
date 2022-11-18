import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os


options = Options()
# driver = webdriver.Chrome(options=options)

# try:
#     driver.find_element_by_xpath("")

def sign_in():
    driver = webdriver.Chrome()
    url = 'https://www.youtube.com/?gl=TW&hl=zh-tw'
    driver.get(url)
    # driver.maximize_window()
    time.sleep(5)
    usernameElement = driver.find_element(By.XPATH, '//*[@id="email"]')
    pwElement = driver.find_element(By.XPATH, '//*[@id="password"]')

# confirmElement.click()

# sign_in()
