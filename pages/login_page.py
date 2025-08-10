
import allure
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.config import ConfigReader
from pages.basepage import BasePage
class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    MY_ACCOUNT_DROP_DOWN = (By.CSS_SELECTOR,"a.dropdown-toggle > span.hidden-xs")
    ACCOUNT_DROP_DOWN_LOGIN_BUTTON = (By.CSS_SELECTOR,".dropdown.open  li:nth-child(2) > a")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    Login_BUTTON = (By.CSS_SELECTOR,"input.btn.btn-primary")
    LOG_OUT_BUTTON = (By.CSS_SELECTOR,"ul > li.dropdown.open > ul > li:nth-child(5) > a")
    ERROR_MESSAGE = (By.CSS_SELECTOR,".alert-danger > i")
    __SUCCESSFUL_LOGIN_URL = ConfigReader.read_config("Successful_login_URL", "url")



    def click_on_my_account_drop_down(self):
        self.click(self.MY_ACCOUNT_DROP_DOWN)

    def menu_login_button(self):
        self.click(self.ACCOUNT_DROP_DOWN_LOGIN_BUTTON)

    def login(self):
        self.click(self.Login_BUTTON)

    def logout(self):
        self.click(self.MY_ACCOUNT_DROP_DOWN)
        self.click(self.LOG_OUT_BUTTON)

    @allure.step("login with username: {email} and password : {password}")
    def fill_login_fields(self,email,password):
        self.fill_text(self.EMAIL_FIELD,email)
        self.fill_text(self.PASSWORD_FIELD,password)

    def login_error_message(self):
        return self.driver.current_url==self.__SUCCESSFUL_LOGIN_URL

