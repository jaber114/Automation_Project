
import allure
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_login_users import username,password
class Test_choose_product(BaseTest):

    @allure.severity(Severity.CRITICAL)
    @allure.title("Fill and submit contact us form - Test A02")
    @allure.description("logging in,Navigates to Contact us page,fill the form and send it")
    def test_contact_us_form(self):
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
        with allure.step("Navigates to contact us page"):
            self.check_out_forms.delay(5)
            self.check_out_forms.navigate_to_contact_us_page()
        with allure.step("Filling the form:name,email,enquiry"):
            self.check_out_forms.delay(5)
            self.check_out_forms.fill_contact_us_form("jaber","srks662@gmail.com","thisistheasdgdfgdgffsdhhdfsdfgdfgddfgd")
        with allure.step("Contact us form submit validation"):
            self.check_out_forms.delay(5)
            if self.check_out_forms.form_validation():
                assert True
            else:
                assert False,"Failed to submit the form"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Purchase product proccess")
    @allure.description("Purchase product proccess")
    def test_purchase_product(self):
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
            self.choose_product_page.choose_product("HTC Touch HD")
        with allure.step("Add product to the cart"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_to_cart()
        with allure.step("Navigate to cart screen"):
            self.choose_product_page.navigate_to_cart()
            self.choose_product_page.delay(5)
        with allure.step("Click on checkout button"):
            self.check_out_forms.delay(5)
            self.check_out_forms.check_out_button_click()
        with allure.step("Billing address page"):
            self.check_out_forms.delay(5)
            self.check_out_forms.billing_address_button()
        with allure.step("delivery address page"):
            self.check_out_forms.delay(2)
            self.check_out_forms.delivery_address_button()
        with allure.step("Delivery method page"):
            self.check_out_forms.delay(3)
            self.check_out_forms.delivery_method_page("commeneasdasda")
        with allure.step("Payment method page"):
            self.check_out_forms.delay(3)
            self.check_out_forms.payment_method_page("adsadsadsadasdsada")
        with allure.step("Confirm order validation"):
            self.check_out_forms.delay(3)
            self.check_out_forms.confirm_order()
            self.check_out_forms.delay(3)
            if self.check_out_forms.product_purchase_validation():
                assert True
            else:
                assert False,"Failed to purchase the product"




