
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Programcreek.com/python/example/selenium.webdriver
chrom_opt = webdriver.ChromeOptions()
chrom_opt.add_argument("headless")
chrom_opt.add_argument("--start-maximized")
chrom_opt.add_argument("--ignore--certificate--errors") #for wenseites SSL error - Advanced to proceed to website

#Run test in Headless mode means chrome browser will not invoke but all the script will run in backend
# driver = webdriver.Chrome( executable_path="C:\\chromedriver.exe", options=chrom_opt)
driver = webdriver.Chrome(options=chrom_opt)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)