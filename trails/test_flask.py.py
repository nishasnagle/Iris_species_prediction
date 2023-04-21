from flask import Flask, request
app = Flask(__name__)

import pandas as pd
import numpy as np
import pickle
import test

@app.route('/predict_species', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        SepalLengthCm = float(request.args.get('SepalLengthCm'))
        SepalWidthCm = float(request.args.get('SepalWidthCm'))
        PetalLengthCm = float(request.args.get('PetalLengthCm'))
        PetalWidthCm = float(request.args.get('PetalWidthCm'))
    elif request.method == 'POST':
        SepalLengthCm = float(request.form['SepalLengthCm'])
        SepalWidthCm = float(request.form['SepalWidthCm'])
        PetalLengthCm = float(request.form['PetalLengthCm'])
        PetalWidthCm = float(request.form['PetalWidthCm'])
    else:
        return 'Invalid Request Method'
    print('SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm:', SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    species = test.predict_species(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    return 'Predicted Species is {}'.format(species)


if __name__ == '__main__':
    print('Starting Python Flask Server For Iris Species Prediction.......')
    app.run(debug=True,port=5000)
    