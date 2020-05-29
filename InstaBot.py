import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://www.instagram.com/')
time.sleep(2)

explore = browser.find_element_by_xpath('//a[@href= "/explore/"')
explore.click()
time.sleep(2)

search = browser.find_element_by_css_selector("input[placeholder='Search']")
search.send_keys('#inkart').send_keys(Keys.ENTER)
time.sleep(2)

time.sleep(5)

browser.close()
