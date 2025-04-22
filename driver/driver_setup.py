import json # Importing the json module to handle JSON files
from selenium import webdriver # Importing the webdriver module from Selenium to control web browsers
import os  # Importing the os module to interact with the operating system
from lib.logging import setup_logger # Importing a custom logging setup function

# Set up the logger
logger = setup_logger(name="driver_logger")

class Driver:
    @staticmethod
    def load_config(config_path="config.json"):
        """Loads the mobile emulation configuration and folder paths from the provided JSON file."""
        try:
            # Use the relative path to the config file in the root directory
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            
            # Get the deviceName from the config, fall back to "Pixel 4" if not found
            device_name = config.get("mobile_emulation", {}).get("deviceName", "Pixel 4")
            
            # Get folder paths from config file
            screenshot_dir = config.get("folders", {}).get("screenshots", "screenshots")
            reports_dir = config.get("folders", {}).get("reports", "reports")
            
            logger.info(f"Loaded config - Device: {device_name}, Screenshots folder: {screenshot_dir}, Reports folder: {reports_dir}")
            
            return device_name, screenshot_dir, reports_dir
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return "Pixel 4", "screenshots", "reports"  # Fallback to default values if there's an error
        
    @staticmethod
    def clear_folder(folder_path):
        """
        Clears all files in the specified folder and creates the folder if it doesn't exist.
        
        :param folder_path: Path to the folder to clear.
        """
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    logger.info(f"Deleted file: {file_path}")
            logger.info(f"All files have been deleted from {folder_path}.")
        else:
            os.makedirs(folder_path)  # Create the folder if it doesn't exist
            logger.info(f"Folder {folder_path} created.")

    @staticmethod
    def get_driver(mobile=False, config_path="config.json"):
        """
        Initializes and returns a WebDriver instance with mobile emulation for Chrome.

        Args:
            mobile (bool): If True, enables mobile emulation on Chrome.
            config_path (str): Path to the config file (defaults to "config.json").

        Returns:
            WebDriver: A Selenium WebDriver instance for the specified setup.
        """
        # Load device name and folder paths from config
        device_name, screenshot_dir, reports_dir = Driver.load_config(config_path)
        
        # Clear the folder contents before starting the driver
        Driver.clear_folder(screenshot_dir)
        Driver.clear_folder(reports_dir)
        
        if mobile:
            # Define the mobile emulation for a specific device
            mobile_emulation = {"deviceName": device_name}
            
            # Create ChromeOptions instance
            chrome_options = webdriver.ChromeOptions()

            # Add mobile emulation configuration
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

            # Initialize the Chrome WebDriver with mobile emulation
            driver = webdriver.Chrome(options=chrome_options)
            logger.info(f"Driver initialized with mobile emulation for {device_name}")
        else:
            # Initialize the Chrome WebDriver without mobile emulation
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()  # Maximize the window for better visibility
            logger.info("Driver initialized without mobile emulation")

        return driver

    @staticmethod
    def close_driver(driver):
        """
        Closes the given WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to close.
        """
        if driver:
            driver.quit()
            logger.info("Driver has been closed.")
