# Import the necessary modules and classes
from pages.base_page import BasePage  # Import the BasePage class from the correct location
from selenium.webdriver.common.by import By  # Locator strategy class for Selenium
from selenium.webdriver.common.keys import Keys  # Keys class for keyboard actions
from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Conditions for waiting

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

    
        """
        Check if the video player is visible on the page.

        Returns True if the player is visible, otherwise False.
        """
        element = (By.CSS_SELECTOR, 'button[data-a-target="player-fullscreen-button"]')  # Locator for player button
        return self.is_element_displayed(element)  # Return True if the element is displayed
