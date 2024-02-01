# flower_classifiication

---
***__Dependencies to install:__
* tensorflow
* flask
* flask-cors
* scikit-learn
* matplotlib
* seaborn
* pandas
* numpy
* tensorflow
* streamlit
* gunicorn
---

---
IDE Used: Visual Studio Code

---

> ### How to run program:
* > First, run this command in your terminal: python src/pipeline/training.py <br>
 This will trigger so many things, first access an archive zip file, unzips it, creates a new folder called ```flowers```, then moves on to create an ```artifacts``` folder and split images into ```train``` and ```validation``` sets with ```train having 700 images from 5 different folders which will be used as labels``` and the remaining images will be moved into the ```validation folder for testing```

 * > Second, the model is trained on a pre-trained inception_v3 CNN model, a dropout layer added to reduce overfitting

 ***__Second file to run__***
 After training the model the model and class_indices_mapping files are moved to the ```validation``` folder inside ```artifacts``` folder/directory, move both files and put them in the root directory, and run your trained model either using flaskAPI in your postman or using streamlit
 * To use FlaskAPI, run ```python app.py```, and open your post app, then run on the SEND request from the server ```127.0.0.1/2765``` and input your encoded image, boom you have your API running
 * To use Streamlit, run the command ```streamlit run main.py``` in your terminal, a UI will run in your local browser and, use the UI to upload a flower image and you will have your Image classified as a type of flower, prediction is about 82%-85% 
