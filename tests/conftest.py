import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.check_out_forms import CheckOutForms
from pages.choose_product import ChooseProduct
from pages.login_page import LoginPage
from pages.sign_up_page import SignUp
from pages.user_actions import UserActions
from utils.config import ConfigReader


def browsertype():
    return os.getenv(
        "BROWSER",
        ConfigReader.read_config("browser", "browser_type")
    ).strip().lower()


def build_driver(browser_kind: str):
    headless = os.getenv("HEADLESS", "1").lower() in ("1", "true", "yes")

    if browser_kind == "chrome":
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
            opts.add_argument("--window-size=1920,1080")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--no-sandbox")
            opts.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=opts)

    if browser_kind == "edge":
        opts = EdgeOptions()

        # 🔥 CRITICAL FIX FOR JENKINS / SYSTEM
        tmp_profile = os.path.join(
            os.environ.get("TEMP", r"C:\Windows\Temp"),
            "edge_selenium_profile"
        )
        opts.add_argument(f"--user-data-dir={tmp_profile}")

        if headless:
            opts.add_argument("--headless=new")
            opts.add_argument("--window-size=1920,1080")

        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")

        return webdriver.Edge(options=opts)

    if browser_kind == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        return webdriver.Firefox(options=opts)

    raise ValueError(f"Unsupported browser_type: {browser_kind}")


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    browser_kind = browsertype()
    driver = build_driver(browser_kind)

    try:
        driver.set_window_size(1920, 1080)
    except Exception:
        pass

    url = ConfigReader.read_config("general", "url")
    driver.get(url)

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.sign_up_page = SignUp(driver)
    request.cls.user_actions = UserActions(driver)
    request.cls.choose_product_page = ChooseProduct(driver)
    request.cls.check_out_forms = CheckOutForms(driver)

    yield

    driver.quit()
