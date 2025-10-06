
import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/client/#/auth/login")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("helloharsh@ymail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("12345")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#Xpath using any text on webpage //button[@text()='save new password']

time.sleep(5)