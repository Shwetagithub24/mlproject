import sys  #Provides functions to manipulate different parts of python env
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    """
    This function generates an error message detailing the type of error and the specific details of the error.
    :param error: The type of error raised.
    :param error_detail: The detailed error message.
    :return: A formatted error message detailing the type of error and the specific details.
    """
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    
"""if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
"""         