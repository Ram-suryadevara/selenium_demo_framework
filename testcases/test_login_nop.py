# import os
import pytest
# from datetime import datetime
from pageobjects.loginpage import LoginPage
# from configurations import config
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestLogin:
    """
    details of the Url, username & password
    """
    # base_URL = "http://admin-demo.nopcommerce.com"
    # useremail = "admin@yourstore.com"
    # password = "admin"

    base_URL = ReadConfig.get_applicationurl()
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_homepage(self, setup):
        """
         Test case to verify the website title before login.
        :param setup:
        :return:
        """
        self.logger.info("******** TestLogin *******")
        self.logger.info("******** Verifying home page title ********")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.base_URL)
        title_act = self.driver.title

        if title_act == "Your store. Login":
            self.logger.info("**** home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test is failed****")
            self.driver.save_screenshot(".\\Screenshots\\" +
                                        "test_homePage.png")
            # self.driver.get_screenshot_as_file("test_homePage.png")
            self.driver.close()
            assert False

    # @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        """
        Test case to verify the website title after login.
        :param setup:
        :return:
        """
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clicklogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            # filename = "test_homePage_.png"
            # filepath = os.path.join(os.path.dirname(__file__), "..",
            #                         "Screenshots", filename)
            # # file_path = os.path.join(os.getcwd())
            # self.driver.save_screenshot(r"D:\Documents\
            #                               Python&Selenium_Workspace\Selenium_tasks_Msys\Screenshots\test_homePage_"+str(datetime.now())+".png")
            # self.driver.save_screenshot(filepath)
            self.driver.save_screenshot(".\\Screenshots\\" +
                                        "test_login.png")
            self.driver.close()
            assert False
