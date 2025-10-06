import json
import os.path
import sys
import time

import pytest
from selenium import webdriver



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from pageObjects.shop import shopPage


# Page object should not have testData
test_data_path = '../data/Scenario-test_e2eFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]



@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance):
    driver = browserInstance
    #driver.get("http://www.rahulshettyacademy.com/angularpractice/")

    driver.get("https://rahulshettyacademy.com/angularpractice/shop")

    driver.implicitly_wait(5)
    #loginPage = LoginPage(driver)

    #loginPage.login()
    shop_page = shopPage(driver)
    shop_page.shop_cart("Blackberry")
    #shop_page.goToCart()

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