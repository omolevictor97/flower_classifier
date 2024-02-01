import numpy as np
import joblib
from keras.preprocessing import image
from src.logger import logging
from src.exception import CustomExceptionHandler
import os, sys
from src.pipeline.training import model_trainer
from src.constant import *
from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        train_path, val_path = data_ingestion.initiate_data_ingestion()
        model_classifier = model_trainer(input_shape=IMAGE_SIZE, train_path=train_path, val_path=val_path)
        model_classifier.save("model2.keras")
        test_image = image.load_img(r"C:\Users\HP\Downloads\tulip.jpeg", target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model_classifier.predict(test_image)

        if result[0][0] == 1:
            prediction = 'daisy'
            print(prediction)
        elif result[0][1] == 2:
            prediction = 'dandelion'
            print(prediction)
        elif result[0][2] == 3:
            prediction = "rose"
        elif result[0][3] == 4:
            prediction = "sunflower"
        elif result[0][4] == 5:
            prediction = "tulip"
        else:
            print("Flower image not recognized by the model")
    except Exception as e:
        logging.error(str(e))
        raise CustomExceptionHandler(e, sys)
