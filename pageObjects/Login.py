from selenium.webdriver.common.by import By

from pageObjects.shop import shopPage
from utils.browserutils import BrowserUtils


#POM
# if class instance at global
class LoginPage(BrowserUtils):
    def __init__(self, driver):   # constructor
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.XPATH, "//input[@id='password']")
        self.sign_InBtn = (By.ID, "signInBtn")


  # Action methods
    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.sign_InBtn).click()
        #shop_page = shopPage(self.driver)
        #return shop_page
