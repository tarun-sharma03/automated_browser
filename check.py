from selenium import webdriver
from time import sleep
for i in range(50):
    driver = webdriver.Chrome('C:\\Users\\my pc\\Downloads\\chromedriver_win32\\chromedriver')
    driver.get("http://bit.ly/10dayscb")
    sleep(10)
    driver.close()