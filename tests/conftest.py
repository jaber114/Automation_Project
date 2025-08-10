import os

import allure
import pytest
from pages.check_out_forms import CheckOutForms
from pages.choose_product import ChooseProduct
from pages.login_page import LoginPage
from pages.sign_up_page import SignUp
from pages.user_actions import UserActions
from utils.config import ConfigReader
from selenium import webdriver


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    browser_kind=browsertype()
    match browser_kind:
        case "Chrome":
          request.cls.driver = webdriver.Chrome()
        case "Edge":
          request.cls.driver = webdriver.Edge()
        case "Firefox":
          request.cls.driver=webdriver.Firefox()

    request.cls.driver.maximize_window()
    url = ConfigReader.read_config("general", "url")
    request.cls.driver.get(url)
    request.cls.login_page = LoginPage(request.cls.driver)  # Pass the driver correctly here
    request.cls.sign_up_page=SignUp(request.cls.driver)
    request.cls.user_actions=UserActions(request.cls.driver)
    request.cls.choose_product_page=ChooseProduct(request.cls.driver)
    request.cls.check_out_forms=CheckOutForms(request.cls.driver)
    yield
    request.cls.driver.quit()

def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

def pytest_sessionfinish() -> None:
    browser_type=browsertype()
    environment_properties = {
     'browser': browser_type,
     'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)

def browsertype():
    browser=ConfigReader.read_config("browser","browser_type")
    match browser:
     case "Chrome":
          return "Chrome"
     case "Firefox":
         return "Firefox"
     case "Edge":
         return "Edge"
     case "Opera":
         return "Opera"
     case "Safari":
         return "Safari"



