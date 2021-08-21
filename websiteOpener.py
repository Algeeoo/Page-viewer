from selenium import webdriver
import time

count = 0
urls = ['https://audioconn.com/homeauth/','https://audioconn.com/profileauth/','https://audioconn.com/search/']

while count < 100:
    for url in urls:
        driver = webdriver.Firefox()
        driver.get(url=url)
        time.sleep(25)
        driver.quit()
        count = count + 1
        

else:
    pass

