import base64
from src.logger import logging
from src.exception import CustomExceptionHandler
import sys

def decodeImage(imgName, fileName):
    try:
        imagedata = base64.b64decode(imgName)
        with open(fileName, "wb") as file:
            file.write(imagedata)
            #optional: file.close()
    except Exception as e:
        logging.error(f"Error has occured at decode Image function ")
        raise CustomExceptionHandler(e, sys)
    
def encodeImageIntoBase64(croppedImage):
    try:
        with open(croppedImage, "rb") as file:
            return base64.b64encode(file.read())
    except Exception as e:
        logging.error("Error occured at encode Image function")
        raise CustomExceptionHandler(e, sys)
