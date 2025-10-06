import re
import time
from email import message
from pydoc import text

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
#action = ActionChains(driver)
#action.click()
#action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowopen = driver.window_handles

driver.switch_to.window(windowopen[1])
print(driver.find_element(By.XPATH, "//p[@class='im-para red']").text)
email = re.search(r'[\w\.-]+@[\w\.-]+', text)
if email:
    print(email.group())
print(email)

driver.find_element(By.ID, "username").send_keys(email)
