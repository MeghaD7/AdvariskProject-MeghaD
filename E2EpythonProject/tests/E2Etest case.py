import time

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.getusername().send_keys("standard_user")
        loginpage.getpassword().send_keys("secret_sauce")
        loginpage.Login()
        time.sleep(5)

    def test_addtoCart(self):
        productpage = ProductPage(self.driver)
        productpage.Addtocart()
        productpage.Shoppinglink()
        time.sleep(5)

    def test_check(self):
        checkoutpage = CheckoutPage(self.driver)
        checkoutpage.Checkout()
        time.sleep(5)
        checkoutpage.getFirstname().send_keys("Megha")
        checkoutpage.getLastname().send_keys("DD")
        checkoutpage.getZipcode().send_keys("422210")
        checkoutpage.Submit()
        checkoutpage.Finish()
        alertText = checkoutpage.getSuccessMessage().text
        print(alertText)

        assert ("Thank you" in alertText)
        time.sleep(5)

