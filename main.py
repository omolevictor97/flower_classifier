import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from keras.preprocessing import image


model = tf.keras.models.load_model("model_new.keras")
class_indices_mapping = np.load("class_indices_mapping.npy", allow_pickle=True).item()

# def preprocess(image):
#     processed_image = image.resize((224, 224))
#     processed_image = image.img_to_array(processed_image)
#     processed_image = np.expand_dims(processed_image, axis=0)
#     processed_image /= 255.0
#     return processed_image

def make_predictions(model, image):
    predictions = model.predict(image)
    return predictions
def main():
    st.title("Flower Classifier")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        test_image = image.load_img(uploaded_image, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0
        print(test_image)
        result = make_predictions(model=model, image=test_image)
        prediction_indices = np.argmax(result, axis=1)
        prediction_labels = [class_indices_mapping[index] for index in prediction_indices]
        print(prediction_labels)
        st.write(f"The flower is {prediction_labels[0]}")

if __name__ == "__main__":

    main()
