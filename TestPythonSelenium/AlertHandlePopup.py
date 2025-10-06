
import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Harsh"

driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept()

