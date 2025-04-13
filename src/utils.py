# src/utils.py

import json
import logging

def load_data(file_path):
    """
    Load data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Loaded data from the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data, file_path):
    """
    Save data to a JSON file.
    
    Args:
        data (dict): Data to save.
        file_path (str): Path to the JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def setup_logger(log_file):
    """
    Set up a logger for the application.
    
    Args:
        log_file (str): Path to the log file.
    
    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger("CareerAdvisorLogger")
    logger.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Create formatter and add it to the handler
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    
    # Add handler to the logger
    logger.addHandler(file_handler)
    
    return logger