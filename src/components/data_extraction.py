from src.logger import logging
from src.exception import CustomExceptionHandler
from zipfile import ZipFile
import os, sys

class Extraction:
    def __init__(self, filepath:str) -> None:
        self.filepath = filepath

    def file_extractor(self) -> str:
        logging.info("File Extraction is about to start")
        try:
            with ZipFile(self.filepath) as ZipObj:
                ZipObj.extractall()
                logging.info("File extraction completed")
                return os.path.join(os.getcwd(), "flowers")
        except Exception as e:
            logging.error(f"Error is: {e}")
            raise CustomExceptionHandler(e, sys)

