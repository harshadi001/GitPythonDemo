import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)













time.sleep(3)