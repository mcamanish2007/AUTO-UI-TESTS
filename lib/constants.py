# lib/constants.py
class CONSTANTS:
    """
    A class to store constant values used across the application.
    """
    TWITCH_TITLE = "Twitch"
    TWITCH_SEARCH_STARCRAFT_II = "StarCraft II"
    SCREENSHOT_NAME = "twitch_player"
    
class TIMEOUTS:
    """
    Timeout settings used for WebDriver waits.
    """
    DEFAULT = 20
    SHORT = 5
    MEDIUM = 15
    LONG = 30