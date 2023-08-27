from flask import Flask, render_template, request, jsonify
import pickle


# Setup a Flask App
app = Flask(__name__)

# Load the model from the .pkl file
with open('linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Route to receive and send back predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the request
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    # Preprocess the input data and make predictions using the loaded model
    prediction = loaded_model.predict([[area, bedrooms, bathrooms]])

    # Return the predictions as a JSON response
    return jsonify({'prediction': prediction[0]})


# Route to show the form
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)