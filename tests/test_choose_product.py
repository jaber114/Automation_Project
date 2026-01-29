import allure
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_login_users import username,password
class Test_choose_product(BaseTest):

  
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Update product quantity in card")
    @allure.description("Choose product from a category and add it to the cart,then remove it from the cart")
    def test_update_product_page_quantity(self):
        with allure.step("Clicking on the drop down button"):
            self.login_page.delay(2)
            self.login_page.click_on_my_account_drop_down()
        with allure.step("Clicking on Login button the maim menu"):
            self.login_page.delay(2)
            self.login_page.menu_login_button()
        with allure.step("Filling the email and password with the data above"):
            self.login_page.delay(2)
            self.login_page.fill_login_fields(username, password)
        with allure.step("Clicking on the login button"):
            self.login_page.delay(2)
            self.login_page.login()
            self.login_page.delay(2)
        with allure.step("Choose product_page category"):
            self.choose_product_page.delay(5)
            self.choose_product_page.choose_category("Desktops")
            self.choose_product_page.delay(5)
        with allure.step("Navigate to product page and choose product"):
            self.choose_product_page.delay(5)
            self.choose_product_page.choose_product("Samsung SyncMaster 941BW")
        with allure.step("Add product to the cart"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_to_cart()
        with allure.step("Navigate to cart screen"):
            self.choose_product_page.navigate_to_cart()
            self.choose_product_page.delay(5)
        with allure.step("Update product quantity"):
            self.choose_product_page.delay(6)
            self.choose_product_page.update_product_quantity("Samsung SyncMaster 941BW",2)
            self.choose_product_page.delay(7)
            if self.choose_product_page.update_quantity_validation():
                assert True
            else:
                assert False,"Failed to update quantity"

















