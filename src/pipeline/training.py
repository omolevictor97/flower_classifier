from src.logger import logging
import os, sys
from typing import List
from src.exception import CustomExceptionHandler
from src.constant import *
from src.components.data_ingestion import DataIngestion
from glob import glob
import numpy as np
from tensorflow.keras.layers import Dense, Flatten, Lambda, Input, Dropout
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.preprocessing import image
from datetime import datetime


def model_trainer(input_shape:List[int], train_path:str, val_path:str):
    try:
        start_time = datetime.now().strftime("%H_%M_%S")
        logging.info("Model has started training")
        logging.info("Model started training at %s", start_time)
        inception = InceptionV3(input_shape=input_shape, weights="imagenet", include_top = False) #intisalizing pretrained model
        for layer in inception.layers:
            layer.trainable = False #deactivate the parameters from the layers from learning new weights
        
        folders = glob(f"{train_path}/*")
        #Add Flattened layer to flatten the pretrained model 
        X = Dropout(0.5)(inception.output)
        X = Flatten()(X)

        predictions = Dense(len(folders), activation="softmax")(X) #A fully connected layer
        model = Model(inputs=inception.input, outputs=predictions) #an instance of Model is created
        model.summary() #Summarize Model and get parameters

        model.compile(
            loss = "categorical_crossentropy",
            metrics = ["accuracy"],
            optimizer = "adam"
        )

        #DATA AUGMENTATION
        train_data_inception = ImageDataGenerator(
            rescale = 1./255,
            shear_range = 0.2,
            zoom_range = 0.2,
            horizontal_flip = 20,
            width_shift_range = 0.2,
            height_shift_range = 0.2,
            fill_mode = "nearest",
            brightness_range = [0.2, 1.2]
        )

        validation_data_inception = ImageDataGenerator(
            rescale = 1./255
        )

        train_set = train_data_inception.flow_from_directory(
            train_path,
            class_mode = "categorical",
            batch_size = BATCH_SIZE,
            target_size = (224, 224)
        )

        validation_set = validation_data_inception.flow_from_directory(
            val_path,
            class_mode = "categorical",
            batch_size = BATCH_SIZE,
            target_size = (224, 224)
        )

        model.fit_generator(
            train_set,
            validation_data = validation_set,
            epochs = 10,
            steps_per_epoch = len(train_set) // BATCH_SIZE,
            validation_steps = len(validation_set) // BATCH_SIZE
        )
        end_time = datetime.now().strftime("%H_%M_%S")
        logging.info("Model already completed at %s", end_time)


        #To get class labels
        class_label = list(train_set.class_indices.keys())
        class_indices_mapping = {index:label for index, label in enumerate(class_label)}
        model.save("model_new.keras")
        np.save("class_indices_mapping.npy", class_indices_mapping)
        return model, class_label
    except Exception as e:
        logging.info(str(e))
        raise CustomExceptionHandler(e, sys)
    
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_path, val_path = data_ingestion.initiate_data_ingestion()
    model_classifier, class_labels = model_trainer(input_shape=IMAGE_SIZE, train_path=train_path, val_path=val_path)
