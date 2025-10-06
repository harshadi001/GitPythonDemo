import time

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select


#service_obj = Service(r"C:\Users\harsh\OneDrive\Documents\chromedriver-win64\chromedriver-win64.exe")
#driver = webdriver.Chrome(service = service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Xpath syntax to handle 2nd checkbox , or index (//input[@type='checkbox'])[2]

Radiobtn = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(Radiobtn))

for Radio in Radiobtn:
    if Radio.get_attribute("value") == "radio2":
        Radio.click()
        assert Radio.is_selected()
        break
