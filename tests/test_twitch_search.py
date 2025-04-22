import pytest # Import pytest for testing framework
from selenium.webdriver.remote.webdriver import WebDriver  # Correct WebDriver import for type hinting
from driver.driver_setup import Driver  # Import the Driver class
from lib.url import TWITCH_URL     # Import the URL from lib.url
from lib.expectation_handler import ExpectationHandler  # Import the ExpectationHandler
from pages.home_page import HomePage  # Import the HomePage
from pages.common_page import CommonPage # Import the CommonPage
from lib.constants import CONSTANTS # Import the constants


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and yield a WebDriver instance,
    then close it after the test completes.
    """
    driver = Driver.get_driver(mobile=True)  # Enable mobile emulation
    yield driver
    Driver.close_driver(driver)
    
@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def common_page(driver):
    return CommonPage(driver)


def test_twitch_search_player(driver: WebDriver, home_page, common_page):
    """
    Test to verify Twitch search functionality.
    """
    # Navigate to the Twitch homepage
    home_page.load(TWITCH_URL)

    # Assert that the title contains "Twitch"
    ExpectationHandler.assert_title_contains(driver, CONSTANTS.TWITCH_TITLE)

    # Click on the 'Browse' button
    home_page.click_browse_button()

    # Enter the search text 'StarCraft II'
    home_page.enter_search_text(CONSTANTS.TWITCH_SEARCH_STARCRAFT_II)
    
    # Close any modal popup if present
    common_page.close_modal_popup() 

    # Scroll down twice to load more results
    for _ in range(2):  # Loop to scroll twice
        common_page.scroll_down(200)  # Scroll down 200 pixels each time

    # Click on the first Twitch image result
    home_page.click_twitch_image()

    # Wait for the video player to load
    home_page.wait_for_player_load()

    # Verify the video player is visible
    is_player_visible = home_page.is_player_visible()
    ExpectationHandler.assert_true(is_player_visible, "Twitch player is not visible")

    # Capture a screenshot of the player view
    common_page.screenshot(CONSTANTS.SCREENSHOT_NAME)