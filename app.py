from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model from the pickle file
with open("lr_final.pickle", 'rb') as f:
    model = pickle.load(f)

# the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the prediction function
@app.route('/predict', methods=['POST'])
def predict_species():
    # Get the input values from the form
    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']

    if sepal_length and sepal_width and petal_length and petal_width:
        # model to make a prediction
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    
    
        if prediction == [0]:
            species = 'setosa'
        elif prediction == [1]:
            species = 'versicolor'
        else:
            species = 'virginica'
    
        # Render the template with the prediction result
        return render_template('index.html', prediction_text='Predicted species is {}'.format(species))
    else:
        return render_template('index.html', prediction_text='Enter valid details')

if __name__ == '__main__':
    app.run()

