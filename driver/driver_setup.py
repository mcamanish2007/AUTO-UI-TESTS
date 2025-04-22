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
            mobile_emulation = config.get("mobile_emulation", {})
            device_name = config.get("mobile_emulation", {}).get("deviceName", "Pixel 4")
            device_metrics = mobile_emulation.get("deviceMetrics", {
            "width": 393,
            "height": 830,
            "pixelRatio": 2.75
         })
            # Get folder paths from config file
            folders = config.get("folders", {})
            screenshot_dir = folders.get("screenshots", "screenshots")
            reports_dir = folders.get("reports", "reports")
            
            logger.info(f"Loaded config - Device: {device_name}, Device Metrics: {device_metrics}, Screenshots folder: {screenshot_dir}, Screenshots folder: {screenshot_dir}, Reports folder: {reports_dir}")
            return device_name, device_metrics, screenshot_dir, reports_dir
        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading config: {e}")
            return "Pixel 4", {"width": 411, "height": 731, "pixelRatio": 2.625}, "screenshots", "reports"
        
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
        device_name, device_metrics, screenshot_dir, reports_dir = Driver.load_config(config_path)
        
        # Clear the folder contents before starting the driver
        Driver.clear_folder(screenshot_dir)
        Driver.clear_folder(reports_dir)
        
        # Initialize ChromeOptions instance
        chrome_options = webdriver.ChromeOptions()
        
        if mobile:
              # Choose mobile emulation mode
            if device_metrics:
                # Use deviceMetrics and custom user agent (if desired)
                mobile_emulation = {
                    "deviceMetrics": device_metrics,
                    "userAgent":    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) "
                                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 "
                                    "Mobile/15E148 Safari/604.1"
                }
                logger.info(f"Using device metrics: {device_metrics}")
            else:
                # Fallback to device name
                mobile_emulation = {"deviceName": device_name}
                logger.info(f"Using device name: {device_name}")

            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = webdriver.Chrome(options=chrome_options)
            # Resize the window based on device metrics (to avoid extra white space)
            driver.set_window_size(device_metrics["width"], device_metrics["height"])
            logger.info("Driver initialized with mobile emulation for device {}: {}".format(device_name, json.dumps(mobile_emulation, indent=2)))
        else:
            # Initialize the Chrome WebDriver without mobile emulation
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()  # Maximize the window for better visibility
            logger.info("Driver initialized with chrome browser.")

        return driver # Returns the WebDriver instance

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
