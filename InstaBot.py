import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hashtags = []
with open('tags.txt', 'r') as file:
    for line in file:
        hashtags.append(line.rstrip())


#open browser to the url
browser = webdriver.Edge()
browser.get('https://www.instagram.com/')
time.sleep(2)

#click on the explore button
explore = browser.find_element_by_xpath('//a[@href= "/explore/"')
explore.click()
time.sleep(2)
        
#find the search box and type in the tag
search = browser.find_element_by_css_selector("input[placeholder='Search']")
search.send_keys('#inkart')
time.sleep(2)

#open the first suggestion
suggestion1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
suggestion1.click()
time.sleep(2)

time.sleep(5)

browser.close()
