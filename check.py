from selenium import webdriver
from time import sleep
for i in range(50):
    driver = webdriver.Chrome('C:\\Users\\my pc\\Downloads\\chromedriver_win32\\chromedriver') #use the name of browser and location of driver
    driver.get("http://google.com")    #the link that you want to open 
    sleep(10)
    driver.close()
