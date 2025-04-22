# Import the necessary modules and classes
from pages.base_page import BasePage  # Import the BasePage class from the correct location
from selenium.webdriver.common.by import By  # Locator strategy class for Selenium
from selenium.webdriver.common.keys import Keys  # Keys class for keyboard actions
from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Conditions for waiting
from selenium.common.exceptions import TimeoutException  # Exception for timeouts
from lib.constants import TIMEOUTS  # Importing TIMEOUTS from constants

class HomePage(BasePage):
    def __init__(self, driver):
        """
        Initialize the HomePage with the provided WebDriver instance.
        Inherits from BasePage for shared functionality.
        """
        super().__init__(driver)  # Call the parent constructor to initialize the driver

    def click_browse_button(self):
        """
        Click the 'Browse' button on the homepage.

        Waits for the button to be visible and then clicks it using the reusable method.
        """
        browse_button = (By.XPATH, "//div[text()='Browse']")  # Locator for 'Browse' button

        # Click the element
        self.click_element(browse_button)

    def enter_search_text(self, search_text):
        """
        Enter a search term into the search input field.

        Clears any pre-existing text and enters the provided search_text. 
        Then, presses the Enter key to initiate the search.
        """
        search_input = (By.CSS_SELECTOR, 'input[placeholder="Search"]')  # Locator for the search input field

        # Find the search input field and clear any existing value
        search_element = self.find_element(search_input[0], search_input[1])
        search_element.clear()

        # Enter the provided search text
        search_element.send_keys(search_text)

        # Press the Enter key to perform the search
        self.press_enter_key()

    def click_twitch_image(self):
        """
        Click on the first visible Twitch image found on the page.

        Waits for the image element to be visible and clicks the first one in the list.
        """
        # Get all the elements with the class 'tw-image'
        elements = self.get_all_elements(By.CLASS_NAME, "tw-image")
        if elements:
            self.click_element_with_js(elements[0])

    def wait_for_player_load(self):
        """
        Wait for the video player to load and become visible.

        This ensures that the player is fully loaded before interacting with it.
        """
        element = (By.CSS_SELECTOR, 'button[data-a-target="player-fullscreen-button"]')  # Locator for player button
        
         # Check if the element is displayed and raise an error if not found
        if not self.is_element_displayed(element):
            raise TimeoutException(f"Video player button not found within the timeout period.")

    def screenshot(self, screenshot_name):
        """
        Take a screenshot and save it with the given name.

        Calls the parent method from BasePage to handle screenshot taking.
        """
        self.take_screenshot(screenshot_name)

    def is_player_visible(self):
        """
        Check if the video player is visible on the page.

        Returns True if the player is visible, otherwise False.
        """
        element = (By.CSS_SELECTOR, 'button[data-a-target="player-fullscreen-button"]')  # Locator for player button
        return self.is_element_displayed(element)  # Return True if the element is displayed
    
