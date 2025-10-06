
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Frames").click()
#windowopen = driver.window_handles

#driver.switch_to.window(windowopen[1])
driver.find_element(By.LINK_TEXT, "iFrame").click()

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Harsh automating iframes")


