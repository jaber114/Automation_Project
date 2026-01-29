# import allure
# from allure_commons.types import Severity
# from tests.base_test import BaseTest
# from utils.test_data_login_users import username, password
#
# class Test_user_actions(BaseTest):
#
#     @allure.severity(Severity.CRITICAL)
#     @allure.title("Change password scenario")
#     @allure.description("Login and change user password")
#     def test_change_user_password(self):
#         with allure.step("Clicking on the drop down button"):
#             self.login_page.delay(2)
#             self.login_page.click_on_my_account_drop_down()
#         with allure.step("Clicking on Login button the main menu"):
#             self.login_page.delay(2)
#             self.login_page.menu_login_button()
#         with allure.step("Filling the email and password with the data above"):
#             self.login_page.delay(2)
#             self.login_page.fill_login_fields(username, password)
#         with allure.step("Logging into the website"):
#             self.login_page.delay(4)
#             self.login_page.login()
#         with allure.step("Navigate to user change password screen"):
#             self.user_actions.delay(4)
#             self.user_actions.my_account_page()
#             self.user_actions.delay(4)
#             self.user_actions.change_password_page()
#             self.user_actions.delay(3)
#         with allure.step("Change user password step"):
#             self.user_actions.delay(4)
#             self.user_actions.change_password("jaber", "jaber")
#             self.user_actions.delay(4)
#             if self.user_actions.change_password_validation():
#                 assert False, "Password not changed, please check passwords"
#             else:
#                 assert True
#
#     @allure.severity(Severity.MINOR)
#     @allure.title("Update user information")
#     @allure.description("Navigate to edit user info and update data")
#     def test_update_user_information(self):
#         with allure.step("Clicking on the drop down button"):
#             self.login_page.delay(2)
#             self.login_page.click_on_my_account
