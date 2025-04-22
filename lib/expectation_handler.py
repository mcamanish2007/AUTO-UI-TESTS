from selenium.webdriver.remote.webdriver import WebDriver  # WebDriver import
from pages.base_page import BasePage  # Import the BasePage class

# This module provides a set of assertion methods for validating conditions in Selenium tests.
class ExpectationHandler:
    def __init__(self, driver: WebDriver):
        """Initialize the expectation handler with a WebDriver instance."""
        self.driver = driver
        self.base_page = BasePage(driver)  # Initialize BasePage instance

    @staticmethod
    def assert_equal(self, actual, expected, message="Values are not equal"):
        """Asserts that actual value equals the expected value."""
        try:
            assert actual == expected, f"{message}: Expected {expected}, but got {actual}"
        except AssertionError:
            # Take screenshot from BasePage
            self.base_page.take_screenshot("assert_equal_failure")
            raise

    @staticmethod
    def assert_true(self, condition, message="Condition is not true"):
        """Asserts that the condition is true."""
        try:
            assert condition, f"{message}: Condition is False"
        except AssertionError:
            # Take screenshot from BasePage
            self.base_page.take_screenshot("assert_true_failure")
            raise

    @staticmethod
    def assert_in(
            self,
            item,
            container,
            message="Item not found in container"):
        """Asserts that the item is found within the container."""
        try:
            assert item in container, f"{message}: Expected '{item}' in '{container}'"
        except AssertionError:
            # Take screenshot from BasePage
            self.base_page.take_screenshot("assert_in_failure")
            raise

    @staticmethod
    def assert_contains_text(
            self,
            element,
            text,
            message="Text not found in element"):
        """Asserts that an element contains the specified text."""
        try:
            actual_text = element.text
            assert text in actual_text, f"{message}: Expected '{text}', but got '{actual_text}'"
        except AssertionError:
            # Take screenshot from BasePage
            self.base_page.take_screenshot("assert_contains_text_failure")
            raise

    @staticmethod
    def assert_title_contains(driver, expected_title):
        """Ensure the page title contains the expected text."""
        try:
            assert expected_title in driver.title, f"Title does not contain '{expected_title}'"
        except AssertionError:
            # Take a screenshot on failure
            # Create instance to call take_screenshot
            base_page = BasePage(driver)
            base_page.take_screenshot("assert_title_contains_failure")
            raise
