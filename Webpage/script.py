import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

sys.path.append("..")
from Scripts import Feature_Extraction

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pandas as pd

from flask import Flask
from flask import request
from flask import render_template
from joblib import load

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    pass

if __name__ == '__main__':

    model = load("../Raw Models/ANN.joblib")
    features = Feature_Extraction.ExtractFeatures("../Test.wav")
    df = pd.DataFrame(data = features).transpose()
    print(model.predict(df))
    #app.run()