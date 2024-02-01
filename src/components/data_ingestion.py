from src.logger import logging
from src.exception import CustomExceptionHandler
from src.components.data_extraction import Extraction
from dataclasses import dataclass
import os, sys
from src.constant import *
import random
import shutil


@dataclass
class DataIngestionConfig:
    train_data:str = os.path.join("artifacts", "train")
    validation_data = os.path.join("artifacts", "validation")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Starts")
        try:
            # Created train and validation directory
            os.makedirs(os.path.join(os.getcwd(), self.ingestion_config.train_data), exist_ok=True)
            os.makedirs(os.path.join(os.getcwd(), self.ingestion_config.validation_data), exist_ok=True)

            #Collected their absolute paths
            train_path = os.path.abspath(self.ingestion_config.train_data)
            validation_path = os.path.abspath(self.ingestion_config.validation_data)
            #Started Extracting the zipped file, the zip file contains a folder
            extraction_obj = Extraction(filepath=ZIP_FILE_PATH)
            folder_path = extraction_obj.file_extractor()
            folder_paths = []

            #Looped through the extracted folder to return the subfolders in it
            for foldernames, subfolders, filenames in os.walk(folder_path):
                if not filenames:
                    folder_paths.append(subfolders)
            
            for names in folder_paths[0]:
                image_path = os.path.join(folder_path, names)
                images = [file for file in os.listdir(image_path) if file.lower().endswith((".jpeg", ".jpg", ".png"))] # check for all files which are images in the folder

                # move 700 of the each image in the subfolder to a new folder called train
                #that contains each folder
                for image in images[:700]:
                    os.chdir(train_path)
                    os.makedirs(names, exist_ok=True)
                    train_image_source_path = os.path.join(image_path, image)
                    train_image_destination_path = os.path.join(train_path, names, image)
                    shutil.move(src=train_image_source_path, dst=train_image_destination_path)
                    logging.info("Images successfully moved to the train directory")
                # move from the 700th image in the subfolder to a new folder called validation
                #that contains each folder
                for image in images[700:]:
                    os.chdir(validation_path)
                    os.makedirs(names, exist_ok=True)
                    validation_image_source_path = os.path.join(image_path, image)
                    validation_image_destination_path = os.path.join(validation_path, names, image)
                    shutil.move(validation_image_source_path, validation_image_destination_path)
                    logging.info("Images successfully moved to the validatory directory")
            print("Image Files successfully moved")
            return (train_path, validation_path)
        except Exception as e:
            logging.error("Error occured here at data ingestion stage")
            raise CustomExceptionHandler(e, sys)


