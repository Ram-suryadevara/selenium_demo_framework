import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(browser):
    # service_obj = Service("D:\\Documents\\chrome driver\\chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)
    # driver.implicitly_wait(20)
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver = webdriver.Chrome()
    yield driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")
