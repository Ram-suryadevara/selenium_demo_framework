import pytest
from pageobjects.loginpage import LoginPage
from pageobjects.addcustomerpage import AddCustomer
# from configurations import config
from selenium.webdriver.common.by import By
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import random
import string


class TestAddCustomer:
    """
    Test case to verify whether the customer details successfully added.
    """
    base_URL = ReadConfig.get_applicationurl()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self, setup):
        """
        method to Test the customer details added in the page.
        :param setup:
        :return: none
        """
        self.logger.info("**************TestAddCustomer*************")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clicklogin()
        self.logger.info("*********************Login Succesful**************")

        self.logger.info("************starting Add Customer Test*********")
        # Creating an object for AddCustomer which expects th driver to pass.
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersmenu()
        self.addcust.clickoncustomersmenuitem()
        self.addcust.clickonaddnew()

        self.email = rand_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        # self.addcust.setemail("sram@gmail.com")
        self.addcust.setpassword("test123")
        self.addcust.setmanagerofvendor("Vendor 2")
        self.addcust.setgender("Male")
        self.addcust.setfirstname("Ram")
        self.addcust.setlastname("suryadevara")
        self.addcust.setdob("05/24/1996")  # Format: mm/ dd / YYY
        self.addcust.setcompanyname("MSYS")
        self.addcust.setadmincontent("This is for testing.........")
        self.addcust.clickonsave()

        self.logger.info("***************saving customer info**********")
        self.logger.info("***********add customer validation************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            print("successful")
            self.logger.info("************test passed-add customer**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +
                                        "test_addCustomer_scr.png")
            print("Not added successfully")
            self.logger.error("*********test failed-add customer*****")
            assert False

        self.driver.close()
        self.logger.info("************ending add_customer test*****")


def rand_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))
