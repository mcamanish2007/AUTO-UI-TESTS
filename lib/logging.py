import logging # This module provides a simple logging setup for an application.

def setup_logger(name="app_logger", log_file="app.log", level=logging.INFO):
    """
    Set up a logger that outputs to both the console and a file.

    :param name: The name of the logger.
    :param log_file: The file where the logs will be stored.
    :param level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    :return: A logger instance.
    """
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a formatter to structure the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a console handler and set the level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Create a file handler and set the level to INFO
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# You can also directly set up a default logger instance
default_logger = setup_logger()
