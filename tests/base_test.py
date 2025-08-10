from pages.check_out_forms import CheckOutForms
from pages.choose_product import ChooseProduct
from pages.login_page import LoginPage
from pages.sign_up_page import SignUp
from pages.user_actions import UserActions


class BaseTest:

 login_page : LoginPage
 sign_up_page : SignUp
 user_actions :UserActions
 choose_product_page :ChooseProduct
 check_out_forms : CheckOutForms