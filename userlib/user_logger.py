import logging
import os
from datetime import date



logger = None  # Global variable to store the logger instance

def setup_logger(directory_name):
    """
    Sets up a logger that writes to a date-specific log file,
    and supports a custom 'caller' field to identify the log source.
    The log format includes the timestamp, caller, process name, process ID, and message.
    """
    global logger
    if logger is not None:
        # If the logger is already set up, return it
        return logger

    current_date = date.today()
    filename = f"log/{directory_name}_{current_date}.log"

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set up logging configuration
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)
    
    # Create a file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.INFO)

    # Create a logging format that includes custom 'caller', process name, and process ID
    formatter = logging.Formatter('%(asctime)s - %(caller)s - %(processName)s - %(process)d - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

def log_message(message, caller="Default", printinfo=False):
    """
    Logs the provided message with the caller information, including process name and ID.
    """
    # Current directory name
    current_dir = os.getcwd()
    directory_name = os.path.basename(current_dir)
    
    # Set up logger if not already set up
    logger = setup_logger(directory_name)
    # Use the 'extra' argument to provide the 'caller' field
    logger.info(message, extra={'caller': caller})
    if printinfo:
        print(message)
