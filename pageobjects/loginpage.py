# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginPage:
    """
    login and password details during login
    """
    USERNAME_ID_TEXT = (By.ID, "Email")
    PASSWORD_ID_TEXT = (By.ID, "Password")
    BUTTON_LOGIN = (By.XPATH, "//button[@class='button-1 login-button']")
    LINK_LOGOUT_TEXT = (By.LINK_TEXT, "Logout")

    # Initializing driver(Constructor)automatically invokes when obj created.
    def __init__(self, driver):  # driver comes from actual testcase
        self.driver = driver  # class variable

    def set_username(self, username):
        """
        method to enter the username details
        :param username: user login details
        :return: none
        """
        self.driver.find_element(*self.USERNAME_ID_TEXT).clear()  # using self
        self.driver.find_element(*self.USERNAME_ID_TEXT).send_keys(username)

    def set_password(self, password):
        """
        method to enter the user password details
        :param password: user password details
        :return: none
        """
        self.driver.find_element(*self.PASSWORD_ID_TEXT).clear()
        self.driver.find_element(*self.PASSWORD_ID_TEXT).send_keys(password)

    def clicklogin(self):
        """
        method to login into the website
        :return: none
        """
        self.driver.find_element(*self.BUTTON_LOGIN).click()

    def clicklogout(self):
        """
        method to logout of website
        :return: none
        """
        self.driver.find_element(*self.LINK_LOGOUT_TEXT).click()
