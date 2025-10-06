
# Purpose of utils here is suppose getting title of page common for POM - shop, login and checkout
# so from here Inheritance concept will be used --
  # Utils is a parent class - And from here pom child classes will inherit

class BrowserUtils:

      def __init__(self,driver):
          self.driver = driver

      def getTitle(self):
          return self.driver.title

