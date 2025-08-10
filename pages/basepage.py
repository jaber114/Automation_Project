import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.ie.webdriver import WebDriver



class BasePage:

    def __init__(self,driver):
        self.driver:WebDriver=driver

    def delay(self,milli_seconds):
        time.sleep(milli_seconds)

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def fill_text(self,locator,text):
        self.driver.find_element(*locator).clear()
        self.delay(4)
        self.driver.find_element(*locator).send_keys(*text)

    def click(self,locator):
        self.delay(3)
        self.driver.find_element(*locator).click()

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

