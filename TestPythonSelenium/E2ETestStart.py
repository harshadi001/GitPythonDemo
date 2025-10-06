import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)

# Partial value xpath syntax
#//tagname[contains(@href, 'shop')] -- Xpath syntax
#Css -- a[href*='shop']  (Regular expression *)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
   productName = product.find_element(By.XPATH, "div/h4/a").text
   if productName == "Blackberry":
       product.find_element(By.XPATH, "div/button")

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 9)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
success_msg = driver.find_element(By.CLASS_NAME, "alert-dismissible").text

assert "Success! Thank you!" in success_msg