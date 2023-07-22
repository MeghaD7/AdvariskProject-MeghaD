import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver


    checkout = (By.ID,"checkout")
    firstname= (By.ID,"first-name")
    lastname= (By.NAME,"lastName")
    zipcode= (By.XPATH,"//input[@id='postal-code']")
    submit = (By.XPATH,"//input[@type='submit']")
    finishbutton =(By.NAME,"finish")
    message = (By.CSS_SELECTOR,".complete-header")


    def Checkout(self):
        self.driver.find_element(*CheckoutPage.checkout).click()

    def getFirstname(self):
        return self.driver.find_element(*CheckoutPage.firstname)

    def getLastname(self):
        return self.driver.find_element(*CheckoutPage.lastname)

    def getZipcode(self):
        return self.driver.find_element(*CheckoutPage.zipcode)

    def Submit(self):
        self.driver.find_element(*CheckoutPage.submit).click()


    def Finish(self):
        self.driver.find_element(*CheckoutPage.finishbutton).click()

    def getSuccessMessage(self):
        return self.driver.find_element(*CheckoutPage.message)




