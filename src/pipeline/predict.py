import numpy as np
import joblib
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from src.logger import logging
from src.exception import CustomExceptionHandler
import os, sys
from src.pipeline.training import model_trainer
from src.constant import *
from src.components.data_ingestion import DataIngestion
from keras.models import load_model

class flower:
    def __init__(self, file) :
        self.file = file
    

    def predict(self):
        try:
            model = load_model("model_new.keras")
            class_indices_mapping = np.load("class_indices_mapping.npy", allow_pickle=True).item()
            imagename = self.file
            test_image = image.load_img(imagename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = test_image/255.0
            result = model.predict(test_image)

            prediction_indices = np.argmax(result, axis = 1)
            prediction_label = [class_indices_mapping[index] for index in prediction_indices]
            return [{"Image is: ": prediction_label[0]}]
        except Exception as e:
            logging.info(str(e))
            raise CustomExceptionHandler(e, sys)
