import sys
import logging
import traceback

# -------------------------------
# Setup logging configuration
# -------------------------------
logging.basicConfig(
    filename="logs/error.log",              # Error logs will be saved in this file
    level=logging.ERROR,                    # Log only ERROR level messages
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format with timestamp
)

# -------------------------------
# Custom Exception Class
# -------------------------------
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException with detailed error information.
        :param error_message: The error message from the original exception.
        :param error_detail: The sys module to extract traceback info.
        """
        super().__init__(error_message)
        self.error_message = self.get_detailed_error(error_message, error_detail)

    def get_detailed_error(self, error_message, error_detail):
        """
        Create a detailed error message with file name and line number.
        :param error_message: Message from the original exception.
        :param error_detail: sys object to get traceback info.
        :return: A string with detailed error information.
        """
        _, _, exc_tb = error_detail.exc_info()  # Get traceback info
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        return f"Error in '{file_name}' at line {line_number}: {error_message}"

    def __str__(self):
        """
        Return the error message when str() is called.
        """
        return self.error_message

# -------------------------------
# Example usage (for testing)
# -------------------------------
if __name__ == "__main__":
    try:
        # Simulate an error (division by zero)
        result = 10 / 0
    except Exception as e:
        # Log the exception using CustomException
        logging.error(CustomException(str(e), sys))
        print("An error occurred. Check logs/error.log for details.")
