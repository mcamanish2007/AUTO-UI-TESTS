from selenium.webdriver.common.by import By  # Locator strategy class for Selenium
from selenium.common.exceptions import TimeoutException  # Exception for timeouts
from selenium.webdriver.common.keys import Keys  # Keys class for keyboard actions
from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for waits
import os  # OS module for file and directory handling
from datetime import datetime  # Date and time utilities
from lib.constants import TIMEOUTS  # Importing TIMEOUTS from constants

class BasePage:
    def __init__(self, driver):
        """
        Initialize the BasePage with the provided WebDriver instance.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def load(self, url):
        """
        Navigate to the specified URL using the WebDriver.

        :param url: The URL to be loaded in the browser.
        """
        self.driver.get(url)

    def find_element(self, by, value):
        """
        Find an element by the provided locator.

        Waits for the element to be present before interacting with it.

        :param by: Locator strategy (e.g., By.XPATH, By.CSS_SELECTOR).
        :param value: Locator value for the element.
        :return: The WebElement.
        """
        return WebDriverWait(self.driver, TIMEOUTS.DEFAULT).until(
            EC.presence_of_element_located((by, value))
        )

    def click_element(self, locator):
        """
        Click an element located by the given locator.

        :param locator: A tuple (By, locator_value) to identify the element.
        """
        # Unpack the locator tuple into 'by' and 'value'
        by, value = locator

        # Wait for the element to be clickable before clicking
        element = WebDriverWait(self.driver, TIMEOUTS.DEFAULT).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def send_keys(self, by, value, keys):
        """
        Find an element, clear it, and send the provided keys.

        :param by: Locator strategy (e.g., By.XPATH, By.CSS_SELECTOR).
        :param value: Locator value for the element.
        :param keys: Keys to send to the element (e.g., text or Keys.ENTER).
        """
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(keys)

    def press_enter_key(self):
        """
        Press the Enter key on the currently active element.
        """
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.ENTER)

    def click_element_with_js(self, target):
        """
        Click an element using JavaScript, identified by a (By, value) tuple.
        """
        if isinstance(target, tuple):
            by, value = target
            element = self.find_element(by, value)
        else:
            element = target

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_vertical(self, pixels):
        """
        Scroll the page vertically by the specified number of pixels.

        :param pixels: Number of pixels to scroll vertically.
        """
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def get_all_elements(self, by, value):
        """
        Get all elements matching the locator.

        :param by: Locator strategy (e.g., By.XPATH, By.CSS_SELECTOR).
        :param value: Locator value for the elements.
        :return: List of WebElements.
        """
        WebDriverWait(self.driver, TIMEOUTS.DEFAULT).until(
        EC.presence_of_element_located((by, value))
        )
        elements = self.driver.find_elements(by, value)

        print(f"[INFO] Found {len(elements)} elements using locator ({by}, '{value}')")
        for index, el in enumerate(elements):
            print(f"  [{index}] tag: {el.tag_name}, alt: {el.get_attribute('alt')}, src: {el.get_attribute('src')}")

        return elements

    def take_screenshot(self, screenshot_name="screenshot"):
        """
        Take a screenshot and save it with the specified name.

        :param screenshot_name: The base name for the screenshot file (default is "screenshot").
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Timestamp for uniqueness
        screenshot_filename = f"{screenshot_name}_{timestamp}.png"
        screenshot_dir = "screenshots"  # Directory to store screenshots

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)  # Create directory if it doesn't exist

        # Save the screenshot
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    def is_element_displayed(self, element, timeout=TIMEOUTS.DEFAULT):
        """
        Check if an element is visible on the page within the specified timeout.

        :param element: Locator tuple (By, locator_value) for the element.
        :param timeout: Timeout in seconds to wait for the element to become visible (default is TIMEOUTS.DEFAULT seconds).
        :return: True if the element is visible, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False  # Return False if the element is not visible within the timeout
