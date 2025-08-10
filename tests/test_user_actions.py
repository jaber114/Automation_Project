import allure
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_login_users import username,password

class Test_user_actions(BaseTest):

 @allure.severity(Severity.CRITICAL)
 @allure.title("Change password scenario")
 @allure.description("Login and change user password")
 def test_change_user_password(self):
    with allure.step("Clicking on the drop down button"):
     self.login_page.delay(2)
     self.login_page.click_on_my_account_drop_down()
    with allure.step("Clicking on Login button the maim menu"):
     self.login_page.delay(2)
     self.login_page.menu_login_button()
    with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username, password)
    with allure.step("Loging into the website"):
     self.login_page.delay(4)
     self.login_page.login()
    with allure.step("Navigate to user change password screen"):
        self.user_actions.delay(4)
        self.user_actions.my_account_page()
        self.user_actions.delay(4)
        self.user_actions.change_password_page()
        self.user_actions.delay(3)
    with allure.step("Change user password step"):
        self.user_actions.delay(4)
        self.user_actions.change_password("jaber","jaber")
        self.user_actions.delay(4)
        if self.user_actions.change_password_validation():
           assert False,"Password not changed,please check if both password and confirmed password are equals"
        else:
            assert True
#_________________________________________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Update user information ")
 @allure.description("logging in,Navigates to my account page,navigate to edit user info screen,and change user information")
 def test_update_user_information(self):
    with allure.step("Clicking on the drop down button"):
     self.login_page.delay(2)
     self.login_page.click_on_my_account_drop_down()
    with allure.step("Clicking on Login button the maim menu"):
     self.login_page.delay(2)
     self.login_page.menu_login_button()
    with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username, password)
    with allure.step("Loging into the website"):
     self.login_page.delay(4)
     self.login_page.login()
    with allure.step("Navigate to my account screen"):
        self.user_actions.delay(4)
        self.user_actions.my_account_page()
    with allure.step("Navigate to edit info page"):
        self.user_actions.delay(3)
        self.user_actions.edit_info_page()
    with allure.step("Change user first & last name,email,and phone"):
        self.user_actions.delay(10)
        self.user_actions.change_user_information(
        "jaber",
        "",
        "jaber@xsense.co",
        "055992545585")
        self.user_actions.delay(10)
        if self.user_actions.change_information_validation():
            assert True
        else:
            assert False,"Missing data,invalid format for one or more of the fields"
#__________________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Subscribe to newsletter Test-P03")
 @allure.description("logging in,Navigates to my account page,navigate to subscribe to newsletter  screen,and perform the subscribe action")
 def test_subscribe_to_newsletter(self):
    with allure.step("Clicking on the drop down button"):
     self.login_page.delay(2)
     self.login_page.click_on_my_account_drop_down()
    with allure.step("Clicking on Login button the maim menu"):
     self.login_page.delay(2)
     self.login_page.menu_login_button()
    with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username, password)
    with allure.step("Loging into the website"):
     self.login_page.delay(4)
     self.login_page.login()
    with allure.step("Navigate to my account screen"):
        self.user_actions.delay(4)
        self.user_actions.my_account_page()
    with allure.step("Navigate to unsubscribe/subscribe page"):
        self.user_actions.delay(5)
        self.user_actions.subscribe_to_newsletter()
        self.user_actions.delay(10)
        if self.user_actions.validate_subscription():
            assert True
        else:
            assert "Failed to subscribe/unsubscribe to the newsletter"
#________________________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Unsubscribe to newsletter Test-P03")
 @allure.description("logging in,Navigates to my account page,navigate to subscribe to newsletter  screen,and perform the unsubscribe action")
 def test_unsubscribe_to_newsletter(self):
    with allure.step("Clicking on the drop down button"):
     self.login_page.delay(2)
     self.login_page.click_on_my_account_drop_down()
    with allure.step("Clicking on Login button the maim menu"):
     self.login_page.delay(2)
     self.login_page.menu_login_button()
    with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username, password)
    with allure.step("Loging into the website"):
     self.login_page.delay(4)
     self.login_page.login()
    with allure.step("Navigate to my account screen"):
        self.user_actions.delay(4)
        self.user_actions.my_account_page()
    with allure.step("Navigate to unsubscribe/subscribe page"):
        self.user_actions.delay(5)
        self.user_actions.unsubscribe_to_newsletter_page()
        self.user_actions.delay(10)
        if self.user_actions.validate_subscription():
            assert True
        else:
            assert "Failed to subscribe/unsubscribe to the newsletter"
#_________________________________________________________________________________________________________________________________________________________________________________________________________________
 @allure.severity(Severity.MINOR)
 @allure.title("Add new Book Entries - Test P05")
 @allure.description("logging in,Navigates to my account page,navigate to Modify your address book entries  screen,and perform add new address book entries")
 def test_add_new_book_entries(self):
    with allure.step("Clicking on the drop down button"):
     self.login_page.delay(2)
     self.login_page.click_on_my_account_drop_down()
    with allure.step("Clicking on Login button the maim menu"):
     self.login_page.delay(2)
     self.login_page.menu_login_button()
    with allure.step("Filling the email and password with the data above"):
        self.login_page.delay(2)
        self.login_page.fill_login_fields(username, password)
    with allure.step("Loging into the website"):
     self.login_page.delay(4)
     self.login_page.login()
    with allure.step("Navigate to my account screen"):
        self.user_actions.delay(4)
        self.user_actions.my_account_page()
    with allure.step("Navigate to address book entries"):
        self.user_actions.delay(5)
        self.user_actions.address_entries_page()
    with allure.step("Click on edit address button"):
        self.user_actions.delay(3)
        self.user_actions.edit_address_button()
    with allure.step("Add new address book entries"):
        self.user_actions.delay(3)
        self.user_actions.add_address_book_entries(
            "jaber",
            "rammal",
            "Roghab street",
            "Yirka",
            "658963",
            "Israel",
            "Haifa")
        self.user_actions.delay(5)
        if self.user_actions.address_book_entries_validation():
            assert False,"One or more of the fields have invalid format"
        else:
            assert True





