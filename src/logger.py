import logging
import os
from datetime import datetime

# -------------------------------
# Create logs directory if it doesn't exist
# -------------------------------
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# -------------------------------
# Generate log file name with timestamp
# -------------------------------
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# -------------------------------
# Configure the logger
# -------------------------------
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # Change to DEBUG or ERROR based on your need
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    filemode="a"  # Append mode
)

# -------------------------------
# Get a custom logger
# -------------------------------
def get_logger(name: str = "project_logger") -> logging.Logger:
    """
    Returns a logger instance that can be used across modules.
    :param name: Name of the logger.
    :return: Configured logger object.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate logs if called multiple times
    if not logger.handlers:
        # Optional: Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    logging.info("logging info has started")