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
explore = browser.find_element_by_xpath('//a[@href= "/explore/"]')
explore.click()
time.sleep(2)

for tag in hashtags:
    #find the search box and type in the tag
    search = browser.find_element_by_css_selector("input[placeholder='Search']")
    search.send_keys(tag)
    time.sleep(2)

    #open the first suggestion
    suggestion1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    suggestion1.click()
    time.sleep(4)

    #open the first image in recent section
    image = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')
    image.click()
    time.sleep(1)

    for _ in range(25):
        #like the picture
        try:
            like = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]')
            like.click()
            time.sleep(1)
        except:
            next = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            next.click()
            time.sleep(1)
            continue

        #go to the next pic
        next = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        next.click()
        time.sleep(1)

    close = browser.find_element_by_xpath('/html/body/div[4]/div[3]/button')
    close.click()

time.sleep(5)
browser.close()
