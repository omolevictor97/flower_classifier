from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.utils import decodeImage
from src.pipeline.predict import flower

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

#@cross_origin
class ClientApp:
    def __init__(self):
        self.filename = r"C:\Users\HP\Downloads\rose.jpg"
        self.classifier = flower(file=self.filename)


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictroute():
    image = request.json["Image"]
    decodeImage(image, clAPP.filename)
    result = clAPP.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clAPP = ClientApp()
    app.run(host='127.0.0.1', port=2765, debug=True)
