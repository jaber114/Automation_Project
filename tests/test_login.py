
import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_login_users import users

class Test_login(BaseTest):

    @allure.severity(Severity.CRITICAL)
    @allure.title("Login step scenarios")
    @allure.description("Login with different login scenarious")
    @pytest.mark.parametrize("username,password",users)
    def test_login(self,username,password):
       with allure.step("Clicking on the drop down button"):
        self.login_page.delay(2)
        self.login_page.click_on_my_account_drop_down()
       with allure.step("Clicking on Login button the maim menu"):
        self.login_page.delay(2)
        self.login_page.menu_login_button()
       with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username,password)
       with allure.step("Clicking on the login button"):
        self.login_page.delay(2)
        self.login_page.login()
        self.login_page.delay(2)
        if self.login_page.login_error_message():
            assert True
        else:
          assert False ,"Failed to login to the website"



