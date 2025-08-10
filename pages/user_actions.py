
from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class UserActions(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    MY_ACCOUNT_DROP_DOWN = (By.CSS_SELECTOR,"a.dropdown-toggle > span.hidden-xs")
    MY_ACCOUNT_PAGE_BUTTON = (By.CSS_SELECTOR,".list-inline > .dropdown > a")
    # for subscribe/unsubscribe actions
    SUBSCRIBE_ACTION_BUTTON = (By.CSS_SELECTOR, "label:nth-child(1) > input[type=radio]")
    SUBSCRIBE_BUTTON =(By.CSS_SELECTOR,".pull-right > input")
    SUBSCRIBE_PAGE_BUTTON = (By.CSS_SELECTOR, "ul:nth-child(8) >li > a")
    UNSUBSCRIBE_ACTION_BUTTON = (By.CSS_SELECTOR,"label:nth-child(2) > input[type=radio]")
    # Change password fields
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR,".pull-right > input")
    CHANGE_PASSWORD_PAGE_BUTTON = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(2) > a")
    CHANGE_PASSWORD_SUCCESS_MSG=(By.CSS_SELECTOR,".fa.fa-check-circle")
    CONFIRM_PASS_INVALID_MESSAGE = (By.CSS_SELECTOR,".col-sm-10 > div ")
    PASSWORD_INVALID_MESSAGE = (By.CSS_SELECTOR,"div:nth-child(2) > div > div")
    EDIT_ACCOUNT_INFO_BUTTON = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(1) > a")
    # for update user information function:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    UPDATE_INFO_ERROR_MESSAGE= (By.CSS_SELECTOR,".col-sm-10>div")
    SUCCESS_MESSAGE =(By.CSS_SELECTOR,".alert-success")
    SUBSCRIPTION_MESSAGE = (By.CSS_SELECTOR, ".alert-success.alert-dismissible")
    ADDRESS_BOOK_PAGE = (By.CSS_SELECTOR,"#content > ul:nth-child(2) > li:nth-child(3) > a")
    ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    ADDRESS_LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    ADDRESS = (By.CSS_SELECTOR, "#input-address-1")
    ADDRESS_CITY = (By.CSS_SELECTOR, "#input-city")
    ADDRESS_POST_CODE = (By.CSS_SELECTOR, "#input-postcode")
    ADDRESS_COUNTRY = (By.CSS_SELECTOR, "#input-country")
    ADDRESS_REGION_FIELD = (By.CSS_SELECTOR, "#input-zone")
    NEW_ADDRESS_BUTTON = (By.CSS_SELECTOR,".buttons > div.pull-right > a")
    MODIFY_BOOK_SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")


    def subscribe_to_newsletter(self):
        self.click(self.SUBSCRIBE_PAGE_BUTTON)
        self.click(self.SUBSCRIBE_ACTION_BUTTON)
        # self.click(self.SUBSCRIBE_BUTTON)

    def unsubscribe_to_newsletter_page(self):
        self.click(self.SUBSCRIBE_PAGE_BUTTON)
        self.click(self.UNSUBSCRIBE_ACTION_BUTTON)
        # self.click(self.SUBSCRIBE_BUTTON)

    def my_account_page(self):
        self.click(self.MY_ACCOUNT_DROP_DOWN)
        self.click(self.MY_ACCOUNT_PAGE_BUTTON)

    def change_password_page(self):
        self.click(self.CHANGE_PASSWORD_PAGE_BUTTON)

    def change_password(self,password,confirm_password):
        self.fill_text(self.PASSWORD_FIELD,password)
        self.fill_text(self.PASSWORD_CONFIRM,confirm_password)
        self.click(self.CONTINUE_BUTTON)

    def change_password_validation(self):
        success_message=self.driver.current_url
        return success_message=="https://tutorialsninja.com/demo/index.php?route=account/password"

    def edit_info_page(self):
        self.click(self.EDIT_ACCOUNT_INFO_BUTTON)

    def change_user_information(self,first_name,last_name,email,phone):
        self.fill_text(self.FIRST_NAME_FIELD,first_name)
        self.fill_text(self.LAST_NAME_FIELD,last_name)
        self.fill_text(self.EMAIL_FIELD,email)
        self.fill_text(self.PHONE_FIELD,phone)
        self.click(self.CONTINUE_BUTTON)
        self.delay(6)

    def change_information_validation(self):
        try:
         element=self.find_element(self.SUCCESS_MESSAGE)
         return "Success: Your account has been successfully updated." in element.text
        except Exception:
            return False

    def validate_subscription(self):
        try:
            subscription_text = self.find_element(self.SUBSCRIPTION_MESSAGE)
            return subscription_text.is_displayed()
        except Exception:
            return False

    def address_entries_page(self):
        self.click(self.ADDRESS_BOOK_PAGE)

    def add_address_book_entries(self,
    first_name,
    last_name,
    address,
    city,
    post_code,
    country,
    region
    ):
      try:
        self.fill_text(self.ADDRESS_FIRST_NAME,first_name)
        self.fill_text(self.ADDRESS_LAST_NAME,last_name)
        self.fill_text(self.ADDRESS,address)
        self.fill_text(self.ADDRESS_CITY,city)
        self.fill_text(self.ADDRESS_POST_CODE,post_code)
        country_options=self.find_element(self.ADDRESS_COUNTRY)
        region_options=self.find_element(self.ADDRESS_REGION_FIELD)
        self.visible_text_selection(country_options,country)
        self.visible_text_selection(region_options,region)
        self.click(self.CONTINUE_BUTTON)
      except Exception:
          self.address_book_entries_validation()

    def address_book_entries_validation(self):
       return self.driver.current_url=="https://tutorialsninja.com/demo/index.php?route=account/address/add"

    def edit_address_button(self):
        self.click(self.NEW_ADDRESS_BUTTON)
















