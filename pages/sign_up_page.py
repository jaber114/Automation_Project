import allure
from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class SignUp(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    MENU_BUTTON = (By.CSS_SELECTOR,"a.dropdown-toggle > span.hidden-xs")
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    REGISTER_BUTTON = (By.CSS_SELECTOR,".dropdown-menu > li:first-child > a")
    SIGNUP_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")
    PRIVACY_POLICY_BUTTON = (By.CSS_SELECTOR,"input[type=checkbox]:nth-child(2)")
    CONTINUE_BUTTON = (By.CSS_SELECTOR,".btn.btn-primary")

    def visit_signup_page(self):
        self.click(self.MENU_BUTTON)
        self.click(self.REGISTER_BUTTON)

    def register(self):
        self.click(self.CONTINUE_BUTTON)

    def privacy_check_button(self):
        self.click(self.PRIVACY_POLICY_BUTTON)

    @allure.step("""
    Sign up with:
        First Name: {first_name}
        Last Name: {last_name}
        Email: {email}
        Telephone: {telephone}
        Password: {password}
    """)
    def fill_signup_form(
    self,
    first_name,
    last_name,
    email,
    telephone,
    password,
    confirm_password
    ):
        self.fill_text(self.FIRST_NAME,first_name)
        self.fill_text(self.LAST_NAME, last_name)
        self.fill_text(self.EMAIL,email)
        self.fill_text(self.TELEPHONE, telephone)
        self.fill_text(self.PASSWORD,password)
        self.fill_text(self.PASSWORD_CONFIRM,confirm_password)

    def sign_up_validation(self):
        success_signup_text=self.get_text(self.SIGNUP_SUCCESS_MESSAGE)
        return success_signup_text=="Your Account Has Been Created!"









