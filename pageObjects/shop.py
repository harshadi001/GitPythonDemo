from selenium.webdriver.common.by import By

from TestPythonSelenium.demo1 import driver
from pageObjects.checkout_confirmation import Checkout_Confirmation


class shopPage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def shop_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button")

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        #checkout_confirmation  = Checkout_Confirmation(self,driver)
        #return checkout_confirmation



