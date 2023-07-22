import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    username = (By.ID,"user-name")
    password = (By.ID,"password")
    login = (By.ID,"login-button")



    def getusername(self):
        return self.driver.find_element(*LoginPage.username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)


    def Login(self):
        self.driver.find_element(*LoginPage.login).click()
