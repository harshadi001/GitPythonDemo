import os.path
import sys
import time


from selenium import webdriver



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from pageObjects.shop import shopPage


# Page object should not have testData

def test_e2e(browserInstance):
    driver = browserInstance
    #driver.get("http://www.rahulshettyacademy.com/angularpractice/")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    driver.implicitly_wait(5)
    loginPage = LoginPage(driver)

    loginPage.login()
    shop_page = shopPage(driver)
    shop_page.shop_cart("Blackberry")
    shop_page.goToCart()

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    #alert = driver.switch_to.alert

    #alertText = alert.text
    #alert.accept()

    # Partial value xpath syntax
    # //tagname[contains(@href, 'shop')] -- Xpath syntax
    # Css -- a[href*='shop']  (Regular expression *)






    driver.close()