from selenium import webdriver
import time

count = 0
urls = ['https://audioconn.com/homeauth/']

while count < 100:
    for url in urls:
        driver = webdriver.Firefox()
        driver.get(url=url)
        time.sleep(5)
        try:
            driver.find_element_by_class_name('advs').click()
            time.sleep(10)
            driver.quit()
            count = count + 1
        except:
            time.sleep(5)
            driver.quit()
            count = count + 1
        

else:
    pass