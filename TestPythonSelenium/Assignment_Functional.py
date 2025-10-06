
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

ExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(4)

vegresults = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(vegresults)
assert count >0

# assignmment list from app and actual list comparison and print
for vegresult in vegresults:
    actualList.append(vegresult.find_element(By.XPATH, "h4").text)
    vegresult.find_element(By.XPATH, "div/button").click()

assert ExpectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

    # Xpath locator using text on button

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

