import time
from selenium import webdriver

browser = webdriver.Edge()
browser.get('https://www.instagram.com/')

time.sleep(5)

browser.close()