import sys
from src.logger import logging

# Writing a custom exception handler...................

def error_message_details(error, error_details:sys) -> str:
    _,_,exc_tb = error_details.exc_info()

    error_line_no = exc_tb.tb_lineno
    error_file_name = exc_tb.tb_frame.f_code.co_filename

    error = f"""Error Occured In Python Script name {error_file_name}, 
    at line_number {error_line_no}, with error message \n 
    {error}... """

    return error

class CustomExceptionHandler(Exception):

    def __init__(self, error_message, error_details:sys.exc_info()):
        super().__init__(error_message)

        self.error_message = error_message_details(error=error_message, error_details=error_details)

    def __str__(self) -> str:
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error(f"Error is \n {str(e)}")
        raise CustomExceptionHandler(e, sys)
