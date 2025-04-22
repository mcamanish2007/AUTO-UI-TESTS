# Import the necessary modules and classes
from pages.base_page import BasePage  # Import the BasePage class from the correct location
from selenium.webdriver.common.keys import Keys  # Keys class for keyboard actions
from selenium.webdriver.common.action_chains import ActionChains  # Action chains for complex user interactions

class CommonPage(BasePage):
    def __init__(self, driver):
        """
        Initialize the HomePage with the provided WebDriver instance.
        Inherits from BasePage for shared functionality.
        """
        super().__init__(driver)  # Call the parent constructor to initialize the driver

    def scroll_down(self, pixels):
        """
        Scroll down the page by a specified number of pixels.

        This method is a wrapper around the base method to scroll vertically.
        """
        self.scroll_vertical(pixels)  # Scrolls down the page by the given pixel value
        
    def screenshot(self, screenshot_name):
        """
        Take a screenshot and save it with the given name.

        Calls the parent method from BasePage to handle screenshot taking.
        """
        self.take_screenshot(screenshot_name)

    def close_modal_popup(self):
        """
        Uses BasePage's modal detection. If modal found, dismiss it via ESC.
        """
        if self.is_modal_present():
            print("Modal detected. Sending ESC to dismiss it.")
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        else:
            print("No modal detected. Continuing.")