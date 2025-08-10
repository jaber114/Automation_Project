from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class CheckOutForms(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    CONTACT_US_PAGE_BUTTON =(By.CSS_SELECTOR,"#top-links > ul > li:nth-child(1) > a")
    NAME_FIELD=(By.CSS_SELECTOR,"#input-name")
    EMAIL_FIELD=(By.CSS_SELECTOR,"#input-email")
    ENQUIRY_FIELD=(By.CSS_SELECTOR,"#input-enquiry")
    FORM_SUBMIT_BUTTON=(By.CSS_SELECTOR,".pull-right > input")
    FORM_VALIDATION_TEXT = (By.CSS_SELECTOR,"#content > h1")
    #
    CHECK_OUT_BUTTON=(By.CSS_SELECTOR,".pull-right > a")
    BILLING_CONTINUE_BUTTON = (By.CSS_SELECTOR,"#button-payment-address")
    DELIVERY_CONTINUE_BUTTON=(By.CSS_SELECTOR,"#button-shipping-address")
    PAYMENT_TERMS_CHECKBOX=(By.CSS_SELECTOR," div > input[type=checkbox]:nth-child(2)")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR,"#button-confirm")
    PRODUCT_ORDER_SUCCESS_MESSAGE=(By.CSS_SELECTOR,"#content > h1")
    DELIVERY_METH0D_COMMENT_FIELD=(By.CSS_SELECTOR,".panel-body > p > textarea")
    DELIVERY_METH0D_CONTINUE_BUTTON=(By.CSS_SELECTOR,"#button-shipping-method")
    PAYMENT_METHOD_COMMENT_FIELD=(By.CSS_SELECTOR,".panel-body > p:nth-child(4) > textarea")
    PAYMENT_METHOD_CONTINUE_BUTTON=(By.CSS_SELECTOR,"#button-payment-method")

    def navigate_to_contact_us_page(self):
        self.click(self.CONTACT_US_PAGE_BUTTON)

    def fill_contact_us_form(self,name,email,enquiry):
        self.fill_text(self.NAME_FIELD,name)
        self.fill_text(self.EMAIL_FIELD,email)
        self.fill_text(self.ENQUIRY_FIELD,enquiry)
        self.click(self.FORM_SUBMIT_BUTTON)

    def form_validation(self):
        try:
            return self.driver.current_url=="https://tutorialsninja.com/demo/index.php?route=information/contact/success"
        except Exception:
            return False

    def check_out_button_click(self):
        self.click(self.CHECK_OUT_BUTTON)

    def billing_address_button(self):
        self.click(self.BILLING_CONTINUE_BUTTON)

    def delivery_address_button(self):
        self.click(self.DELIVERY_CONTINUE_BUTTON)

    def delivery_method_page(self,delivery_method):
        self.fill_text(self.DELIVERY_METH0D_COMMENT_FIELD,delivery_method)
        self.click(self.DELIVERY_METH0D_CONTINUE_BUTTON)

    def payment_method_page(self,payment_comment):
        self.fill_text(self.PAYMENT_METHOD_COMMENT_FIELD,payment_comment)
        self.click(self.PAYMENT_TERMS_CHECKBOX)
        self.click(self.PAYMENT_METHOD_CONTINUE_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    def product_purchase_validation(self):
     try:
        return "Your order has been placed!" in self.get_text(self.PRODUCT_ORDER_SUCCESS_MESSAGE)
     except Exception:
         return False





