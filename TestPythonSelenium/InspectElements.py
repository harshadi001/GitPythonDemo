import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Harsh Adi")  #CSS_Selector
driver.find_element(By.NAME, "email").send_keys("cool@hotmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
# xpath syntax = //tagname[@attribute='value'] = //input[@type='submit']
# CSSselector syntax = tagName[attribute=value] = ., #id, .classname

#Dropdown

dropdwn = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdwn.select_by_visible_text("Female")
time.sleep(3)
dropdwn.select_by_index(0)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)

#driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Third index bro")
driver.find_element(By.CSS_SELECTOR, ".ng-untouched").send_keys("Third index bro")

assert "Succes" in msg
time.sleep(5)