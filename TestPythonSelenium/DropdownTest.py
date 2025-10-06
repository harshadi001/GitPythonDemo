import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)
#countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

#assert print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "India"
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"