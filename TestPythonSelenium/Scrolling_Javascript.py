
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrom_opt = webdriver.ChromeOptions()
chrom_opt.add_argument("headless")

#Run test in Headless mode means chrome browser will not invoke but all the script will run in backend
driver = webdriver.Chrome(options=chrom_opt)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot_web.png")




