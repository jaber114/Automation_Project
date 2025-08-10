import allure
import pytest
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_signup_users import  users


class Test_signup(BaseTest):

    @allure.severity(Severity.CRITICAL)
    @allure.title("Signup for new users test")
    @allure.description("signup for new users with more than scenario")
    @pytest.mark.parametrize("first_name,last_name,email,phone,password,password_confirm", users)
    def test_signup(self,first_name,last_name,email,phone,password,password_confirm):
      with allure.step("Navigate to signup page"):
        self.sign_up_page.visit_signup_page()
        self.sign_up_page.delay(5)
      with allure.step("Filling the signup form with data"):
        self.sign_up_page.fill_signup_form(
            first_name,
            last_name,
            email,
            phone,
            password,
            password_confirm
        )
        self.sign_up_page.delay(10)
      with allure.step("Clicking on privacy check button"):
        self.sign_up_page.privacy_check_button()
        self.sign_up_page.delay(4)
      with allure.step("Clicking on register button"):
        self.sign_up_page.register()
        self.sign_up_page.delay(5)
      with allure.step("validate if signup action is success or failed"):
          if self.sign_up_page.sign_up_validation():
              assert True
          else:
              assert False,"one of the fields is incorrect,or account already in the system"




