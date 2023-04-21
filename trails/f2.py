from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('lr_final.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictSpecies():
    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PetalLengthCm = float(request.form['PetalLengthCm'])
    PetalWidthCm = float(request.form['PetalWidthCm'])
    species = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    if species == 0:
        return 'The predicted species is Setosa'
    elif species == 1:
        return 'The predicted species is Versicolor'
    else:
        return 'The predicted species is Virginica'

if __name__ == '__main__':
    app.run(debug=True)
