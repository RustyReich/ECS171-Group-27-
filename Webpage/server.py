import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

sys.path.append("..")
from Scripts import Feature_Extraction

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import glob
import pandas as pd

from flask import jsonify
from flask import Flask
from flask import request
from flask import render_template
from joblib import load

model = load("../Raw Models/ANN.joblib")

app = Flask(__name__)

@app.route('/')
def my_form() -> None:

    return render_template("index.html")

@app.route("/receive", methods=['POST'])
def form() -> None:

    deleteExistingAudio()

    data = request.files.get('file').read()
    fileName = request.files.get('file').filename
    
    f = open("audio/" + fileName, "wb")
    f.write(data)

    prediction = MakePrediction()

    response = jsonify({"prediction": prediction})
    response.headers.add('Access-Control-Allow-Origin', '*')

    deleteExistingAudio()

    return response

def deleteExistingAudio() -> None:

    existingAudioFiles = glob.glob("audio/*")
    for file in existingAudioFiles:
        os.remove(file)

def MakePrediction() -> str:

    path = "audio/" + os.listdir("audio")[0]
    
    features = Feature_Extraction.ExtractFeatures(path)
    df = pd.DataFrame(data = features).transpose()
    return model.predict(df)[0]

if __name__ == '__main__':

    app.run(debug = True)
    