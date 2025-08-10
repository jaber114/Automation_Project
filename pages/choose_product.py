from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.test_data_login_users import  DROP_DOWN_CATEGORIES, NON_DROP_DOWN_CATEGORIES


class ChooseProduct(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

#   for product search test
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    LINKS =(By.TAG_NAME,'a')
    # For drop down categories
    DROPDOWN_LIST = (By.CSS_SELECTOR, ".dropdown > a")
    NON_DROPDOWN_LIST = (By.CSS_SELECTOR, ".collapse > ul > li > a")
    CATEGORY_DROP_DOWN_BUTTON=(By.CSS_SELECTOR,".see-all")
    CATEGORIES_TITLES =(By.CSS_SELECTOR,"#menu > div.collapse > ul > li > a")
    CATEGORY_SHOW_ALL_BUTTONS= (By.CSS_SELECTOR,".see-all")
    DROP_DOWN_LINKS = (By.CSS_SELECTOR,".collapse > ul > li > div > a")
    CATEGORY_NAME_ON_PAGE = (By.CSS_SELECTOR,"#content > h2")
    PRODUCTS_ON_PAGE =(By.CSS_SELECTOR,".caption > h4 > a")
    PRODUCT_TITLE=(By.CSS_SELECTOR,"#product-product > ul > li:nth-child(3) > a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,".btn-primary.btn-lg")
    CART_PAGE_BUTTON = (By.CSS_SELECTOR,"#cart > button")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR,".text-right > a:nth-child(1)")
    PRODUCTS_ON_CART = (By.CSS_SELECTOR,".text-left > a")
    DELETE_FROM_CART = (By.CSS_SELECTOR,".btn.btn-danger")
    # PRODUCT_LIST_IN_CART=(By.CSS_SELECTOR,".text-left > a")
    LISTS_OF_PRODUCT_ON_CART=(By.CSS_SELECTOR,".table-responsive > table >tbody > tr")
    PRODUCTS_lISTS_IN_CART = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr ")
    #
    PRODUCT_NAMES_IN_CART=(By.CSS_SELECTOR,".text-left >a")
    CART_PRODUCTS_LINKS = (By.TAG_NAME,'a')
    PRODUCT_REMOVE_LINKS_IN_CART = (By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > button.btn-danger")
    UPDATE_QUANTITY_SUCCESSFUL_MESSAGE=(By.CSS_SELECTOR,".alert.alert-success")
    # Quantity function
    QUANTITY_FIELD=(By.CSS_SELECTOR,"update_field")
    PRODUCT_AREAS=(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr ")
    PRODUCT_TITLES=(By.CSS_SELECTOR,".text-left >a")
    PRODUCT_UPDATE_FIELD=(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > .text-left:nth-child(4) > div > input")
    UPDATE_QUANTITY_BUTTON=(By.CSS_SELECTOR,By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > .btn.btn-primary")
    # Wishlist
    ADD_PRODUCT_TO_WISH_LIST_BUTTON=(By.CSS_SELECTOR,".btn-group >.btn.btn-default:nth-child(1)")
    WISH_LIST_BUTTON_PAGE= (By.CSS_SELECTOR,"#wishlist-total > span")
    # Review
    WRITE_REVIEW_BUTTON=(By.CSS_SELECTOR,".rating > p > a:nth-child(7)")
    REVIEW_NAME_FIELD = (By.CSS_SELECTOR,"#input-name")
    REVIEW_AREA_FIELD=(By.CSS_SELECTOR,"#input-review")
    RATING_FIELDS=(By.CSS_SELECTOR,".col-sm-12>[type=radio]")
    SUBMIT_REVIEW_BUTTON=(By.CSS_SELECTOR,"#button-review")
    REVIEW_SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert.alert-dismissible")
    WISH_LIST_PRODUCT_RECORDS=(By.CSS_SELECTOR,".table-responsive > table > tbody > tr")
    # Stock on product page
    AVAILABLE_STATUS=(By.CSS_SELECTOR,".col-sm-4 > ul:nth-child(3) > li:nth-child(3)")

    def product_search(self,product_name):
        self.delay(5)
        self.fill_text(self.SEARCH_FIELD,product_name)
        self.click(self.SEARCH_BUTTON)

    def validate_product_search(self,product_name):
        self.delay(4)
        product_names=self.find_elements(self.LINKS)
        target = product_name.strip().lower()
        for products in product_names:
            product_text =products.text.strip().lower()
            if target in product_text:
                return True
        return False

    def choose_category(self,category_name):
                if category_name in DROP_DOWN_CATEGORIES:
                    catogires_names=self.find_elements(self.DROPDOWN_LIST)
                    for category in catogires_names:
                        if category.text==category_name:
                            category.click()
                            self.delay(4)
                            show_all_links=self.find_element(self.DROP_DOWN_LINKS)
                            self.delay(4)
                            show_all_links.click()
                            break
                elif category_name in NON_DROP_DOWN_CATEGORIES:
                 categories_button_links = self.find_elements(self.NON_DROPDOWN_LIST)
                 for title_element in categories_button_links:
                   if title_element.text == category_name:
                         title_element.click()
                         break
                else:
                    self.driver.execute_script("alert('you choose categorie that is not exist');")

    def category_choose_validation(self,category_name):
        return category_name==self.get_text(self.CATEGORY_NAME_ON_PAGE)

    def choose_product(self,product_name):
       try:
         products=self.find_elements(self.PRODUCTS_ON_PAGE)
         for product in products:
             if product.text==product_name:
                 self.delay(5)
                 product.click()
                 # self.delay(20)
                 # return True
       except Exception:
           return False

    def product_validation(self,product):
        product_titles = self.get_text(self.PRODUCT_TITLE)
        return product_titles==product

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def navigate_to_cart(self):
        self.click(self.CART_PAGE_BUTTON)
        self.click(self.VIEW_CART_BUTTON)

    def product_in_cart_validation(self,product):
        product_in_cart=self.find_elements(self.PRODUCTS_ON_CART)
        for products in product_in_cart:
            if products.text==product:
                return True
        return False

    def delete_product_from_the_cart(self, product):
      try:
        product_area = self.driver.find_elements(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr ")
        # product_area=self.find_elements(self.PRODUCTS_lISTS_IN_CART)
        self.delay(5)
        for products in product_area:
            product_title=products.find_element(By.CSS_SELECTOR,".text-left >a")
            # product_title=products.find_element(self.PRODUCT_NAMES_IN_CART)
            self.delay(2)
            if  product_title.text==product:
                self.delay(5)
                delete_from_cart_button=products.find_element(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > button.btn-danger")
                # delete_from_cart_button=products.find_element(self.PRODUCT_REMOVE_LINKS_IN_CART)
                self.delay(4)
                delete_from_cart_button.click()
                self.delay(5)
      except Exception:
          print("no its not equal to that")

    def delete_all_from_cart_validation(self,product):
        products_links=self.find_elements(self.CART_PRODUCTS_LINKS)
        for name in products_links:
            if name.text!=product:
                self.delay(6)
                return True
        return False

    def update_product_quantity(self,product,quantity):
        self.delay(4)
        product_area = self.driver.find_elements(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr ")
        # product_area=self.find_elements(self.PRODUCT_AREAS)
        for products in product_area:
            product_title=products.find_element(By.CSS_SELECTOR,".text-left >a")
            # product_title=products.find_element(self.PRODUCT_TITLE)
            if product_title.text==product:
                update_field=products.find_element(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > .text-left:nth-child(4) > div > input")
                # update_field=products.find_element(self.PRODUCT_UPDATE_FIELD)
                self.delay(5)
                update_field.clear()
                self.delay(5)
                update_field.send_keys(quantity)
                # update_field.
                self.delay(5)
                update_product_button=products.find_element(By.CSS_SELECTOR,"#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > .btn.btn-primary")
                # update_product_button=products.find_element(self.UPDATE_QUANTITY_BUTTON)
                update_product_button.click()

    def update_quantity_validation(self):
        try:
            self.delay(5)
            quantity_message=self.find_element(self.UPDATE_QUANTITY_SUCCESSFUL_MESSAGE)
            return quantity_message.is_displayed()
        except Exception:
            return False
        # return quantity_message in self.driver.page_source
    def navigate_to_wish_list_page(self):
        self.click(self.WISH_LIST_BUTTON_PAGE)

    def add_product_to_wish_list(self):
        self.delay(5)
        self.click(self.ADD_PRODUCT_TO_WISH_LIST_BUTTON)
        self.delay(5)

    def product_in_wishlist(self,product):
        product_area = self.driver.find_elements(By.CSS_SELECTOR, "#content > form > div > table > tbody > tr ")
        # product_area=self.find_elements(self.PRODUCT_AREAS)
        for products in product_area:
            product_title = products.find_element(By.CSS_SELECTOR, ".text-left >a")
            # product_title=products.find_element(self.PRODUCT_TITLE)
            if product_title.text == product:
                return True
        return False

    def click_on_write_review_button(self):
        self.click(self.WRITE_REVIEW_BUTTON)

    def fill_review_form(self,name,review,rating):
        self.fill_text(self.REVIEW_NAME_FIELD,name)
        self.fill_text(self.REVIEW_AREA_FIELD,review)
        rating_options=self.find_elements(self.RATING_FIELDS)
        for rate in rating_options:
            rate_value = rate.get_attribute('value')
            if rate_value==rating:
                self.delay(4)
                rate.click()
        self.delay(4)
        self.click(self.SUBMIT_REVIEW_BUTTON)

    def review_validation(self):
     try:
        return self.get_text(self.REVIEW_SUCCESS_MESSAGE)=="Thank you for your review. It has been submitted to the webmaster for approval."
     except Exception:
        return False

    def delete_product_from_wishlist(self,product):
        products_in_wishlist=self.find_elements(self.WISH_LIST_PRODUCT_RECORDS)
        for products in products_in_wishlist:
            product_title=products.find_element(By.CSS_SELECTOR,".text-left > a")
            if product_title.text==product:
                delete_button=products.find_element(By.CSS_SELECTOR,".btn.btn-danger")
                self.delay(4)
                delete_button.click()
                self.delay(5)

    def delete_from_wish_list_validation(self):
        try:
            print(self.get_text(self.REVIEW_SUCCESS_MESSAGE))
            return "Success: You have modified your wish list!" in self.get_text(self.REVIEW_SUCCESS_MESSAGE)
        except Exception:
            return False

    def product_in_stock_status(self):
        in_stock_status=self.get_text(self.AVAILABLE_STATUS)
        if "Availability:Out Of Stock"  in self.driver.page_source:
            return False
        return True










































