import allure
from allure_commons.types import Severity
from tests.base_test import BaseTest
from utils.test_data_login_users import username,password
class Test_choose_product(BaseTest):

    @allure.severity(Severity.CRITICAL)
    @allure.title("Search product scenario")
    @allure.description("Search for custom product")
    def test_product_search(self):
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
        with allure.step("Navigates to product page & earch for product"):
            self.choose_product_page.delay(5)
            self.choose_product_page.product_search("stam")
            self.choose_product_page.delay(4)
            if self.choose_product_page.validate_product_search("Mac"):
                assert True
            else:
                assert False, "Specific product not found"
#________________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Add product to cart")
    @allure.description("Search for custom product")
    def test_choose_product_category(self):
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
            if self.choose_product_page.category_choose_validation("Desktops"):
                assert True
            else:
                assert False,"Category not exist in the website"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Choose product ")
    @allure.description("Choose product from a category")
    def test_choose_product(self):
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
            if self.choose_product_page.product_validation("HTC Touch HDaaa"):
                assert True
            else:
                assert False,"the product you typed is not in this category"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Choose product and add it to the cart ")
    @allure.description("Choose product from a category and add it to the cart")
    def test_choose_product_add_to_cart(self):
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
        with allure.step("Product in cart validation"):
            if self.choose_product_page.product_in_cart_validation("HTC Touch HDaaa"):
                assert True
            else:
                assert False,"Product not added to the cart"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Remove product from the cart")
    @allure.description("Choose product from a category and add it to the cart,then remove it from the cart")
    def test_choose_product_delete_from_cart(self):
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
            self.choose_product_page.choose_category("Cameras")
            self.choose_product_page.delay(5)
        with allure.step("Navigate to product page and choose product"):
            self.choose_product_page.delay(5)
            self.choose_product_page.choose_product("Nikon D300")
        with allure.step("Add product to the cart"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_to_cart()
        with allure.step("Navigate to cart screen"):
            self.choose_product_page.navigate_to_cart()
            self.choose_product_page.delay(5)
        with allure.step("Remove product from the cart"):
            self.choose_product_page.delete_product_from_the_cart("Nikon D300")
            self.choose_product_page.delay(5)
        with allure.step("Remove product from cart validation"):
            self.choose_product_page.delay(5)
            if self.choose_product_page.delete_all_from_cart_validation("Nikon D300"):
               assert True,"Product removed from the cart without problems"
            else:
                assert False,"Failed to remove the product from the cart"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Validate product_page status stock/out of stock")
    @allure.description("logging in,choosing product_page category,choosing product_page then adding it to the cart,and check the product_page status")
    def test_product_available_quantity(self):
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
            self.choose_product_page.choose_category("Tablets")
            self.choose_product_page.delay(5)
        with allure.step("Navigate to product page and choose product"):
            self.choose_product_page.delay(5)
            self.choose_product_page.choose_product("Samsung Galaxy Tab 10.1")
        with allure.step("Check product_page availability status(In stock/Out of stock"):
            self.choose_product_page.delay(5)
            if self.choose_product_page.product_in_stock_status():
                assert True
            else:
                assert False,"Product quantity is so low"

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
            self.choose_product_page.choose_product("HP LP3065")
        with allure.step("Add product to the cart"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_to_cart()
        with allure.step("Navigate to cart screen"):
            self.choose_product_page.navigate_to_cart()
            self.choose_product_page.delay(5)
        with allure.step("Update product quantity"):
            self.choose_product_page.delay(6)
            self.choose_product_page.update_product_quantity("HP LP3065",5)
            self.choose_product_page.delay(7)
            if self.choose_product_page.update_quantity_validation():
                assert True
            else:
                assert False,"Failed to update quantity"
#_______________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Add product to the wishlist")
    @allure.description("Choose product from a category and add it to the wishlist")
    def test_add_product_to_wish_list(self):
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
            self.choose_product_page.choose_product("HP LP3065")
        with allure.step("Add product_page to wishlist"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_product_to_wish_list()
        with allure.step("Navigate to wishlist page"):
            self.choose_product_page.delay(5)
            self.choose_product_page.navigate_to_wish_list_page()
        with allure.step("add product to the wish list"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_product_to_wish_list()
        with allure.step("Product validation on wishlist page"):
            self.choose_product_page.delay(5)
            if self.choose_product_page.product_in_wishlist("HP LP3065"):
                assert True
            else:
                assert False,"Failed to add the product to the wishlist"
#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Remove product from wishlist")
    @allure.description("Choose product from a category and remove it from the wishlist")
    def test_remove_product_from_wish_list(self):
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
            self.choose_product_page.choose_product("HP LP3065")
        with allure.step("Add product_page to wishlist"):
            self.choose_product_page.delay(5)
            self.choose_product_page.add_product_to_wish_list()
        with allure.step("Navigate to wishlist page"):
            self.choose_product_page.delay(5)
            self.choose_product_page.navigate_to_wish_list_page()
        with allure.step("Remove product from wishlist"):
            self.choose_product_page.delay(5)
            self.choose_product_page.delete_product_from_wishlist("HP LP3065")
            self.choose_product_page.delay(5)
        with allure.step("Product remove validation on wishlist page"):
            self.choose_product_page.delay(5)
            if self.choose_product_page.delete_from_wish_list_validation():
                assert True
            else:
                assert False, "Failed to remove the product from the wishlist"

#_______________________________________________________________________________________________________________________
    @allure.severity(Severity.CRITICAL)
    @allure.title("Write product_page review")
    @allure.description("Choose product from a category and add a review to this product")
    def test_add_product_review(self):
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
            self.choose_product_page.choose_product("HP LP3065")
        with allure.step("Click on write review button"):
            self.choose_product_page.delay(5)
            self.choose_product_page.click_on_write_review_button()
        with allure.step("Filling review fields Name & Review and Rate"):
            self.choose_product_page.delay(5)
            self.choose_product_page.fill_review_form("name","Reviewnumberoneisthebesteverforallthword","2")
            self.choose_product_page.delay(5)
        with allure.step("Validate submitting review form"):
            self.choose_product_page.delay(5)
            if self.choose_product_page.review_validation():
                assert True
            else:
                assert False,"Failed to submit the review form"
#_______________________________________________________________________________________________________________________

















