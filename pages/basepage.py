from selenium.webdriver.support.select import Select
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
import time
import random
import string

class BasePage:

    def __init__(self,driver):
        self.driver:WebDriver=driver

    @staticmethod
    def generate_random_email(domain="gmail.com", length=8):
        username_chars = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(username_chars) for _ in range(length))
        return f"{username}@{domain}"

    def delay(self,milli_seconds):
        time.sleep(milli_seconds)

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()

    def fill_text(self,locator,text):
        self.driver.find_element(*locator).clear()
        self.delay(4)
        self.driver.find_element(*locator).send_keys(*text)

    
    def click(self, locator, timeout=15):
        #print("DEBUG: new BasePage.click() is running:", locator)
        #print("URL:", self.driver.current_url)
        #print("Title:", self.driver.title)
        #print("Count:", len(self.driver.find_elements(*locator)))
        wait = WebDriverWait(self.driver, timeout)
        el = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        time.sleep(0.2)

        el = wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.driver.execute_script("arguments[0].click();", el)

    #def click(self, locator, timeout=15):
        #wait = WebDriverWait(self.driver, timeout)
    
        # wait element exists + visible
        #el = wait.until(EC.visibility_of_element_located(*locator))
    
        # scroll to center
       # self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
       # time.sleep(0.2)
    
        # wait clickable (not just visible)
       # el = wait.until(EC.element_to_be_clickable(*locator))
    
       # try:
        #    el.click()
       # except (ElementClickInterceptedException, ElementNotInteractableException):
            # last resort: JS click (useful when something overlays but click still possible)
         #   self.driver.execute_script("arguments[0].click();", el)
    

    def get_text(self, locator) -> str:
        self.delay(4)
        return self.driver.find_element(*locator).text

    def is_displayed(self,text):
        return self.driver.find_element(*text).is_displayed()

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def visible_text_selection(self,locator,select_value):
        option_select=Select(locator)
        self.delay(6)
        return option_select.select_by_visible_text(select_value)

    def highlight_element(self, locator, color: str):
        """
        Highlights (briefly) a web element by changing its background color.

        :param driver: The Selenium WebDriver instance.
        :param locator: The locator for the element to be highlighted.
        :param color: The color to highlight the element with (e.g., 'red', 'green').
        """
        # Find the element
        element = self.driver.find_element(*locator)
        # Store the original style (to revert after 300 mills)
        original_style = element.get_attribute("style")

        # Create the new style with the given color
        new_style = f"background-color: {color}; {original_style}"

        # Apply the new style
        self.driver.execute_script("""
                      var element = arguments[0];
                      var new_style = arguments[1];
                      setTimeout(function() {
                          element.setAttribute('style', new_style);
                      }, 0);
                  """, element, new_style)

        # Revert to the original style after a short 300 mills
        self.driver.execute_script("""
              var element = arguments[0];
              var originalStyle = arguments[1];
              setTimeout(function() {
                  element.setAttribute('style', originalStyle);
              }, 300);
          """, element, original_style)

