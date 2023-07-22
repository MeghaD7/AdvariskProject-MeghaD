import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class ProductPage:

    def __init__(self,driver):
        self.driver = driver

    addtocart = (By.ID,"add-to-cart-sauce-labs-backpack")
    shoppinglink = (By.XPATH,"//a[@class='shopping_cart_link']")



    def Addtocart(self):
        self.driver.find_element(*ProductPage.addtocart).click()

    def Shoppinglink(self):
        self.driver.find_element(*ProductPage.shoppinglink).click()



