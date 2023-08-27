# Starter Kit to Serve Machine Learning Model Results via APIs

This starter kit with minimal boilerplate - helps you serve your Python based Machine Learning Model results via a Flask API.

The model used for demonstation purposes here is one that naively predicts house prices based on the number of square footage, bedrooms and bathrooms using Linear Regression.

## Manual Installation

Clone the repo:

```bash
git clone https://github.com/rashmi-carol-dsouza/flask-ml-api-starter.git
cd flask-ml-api-starter
```

Install the dependencies:

```bash
pip3 install -r requirements.txt
```

Configure Virtual Environment:

```bash
pip install virtualenv
virtualenv --python python3 venv
source venv/local/bin/activate
```

Start the Server:

```bash
python3 app.py
```

## Project Structure

```
templates\                      # Jina2 templates folder
 |--index.html                  # Static html
flask_app.py                    # App entry point
house-prices.csv                # Example Property Details Dataset
linear_regression_model.pkl     # Serialised model for demo
Prediction Model.ipynb          # Notebook to test the model before porting to Flask
requirements.txt                # frozen min requirements needed for the application
```

### API Endpoints

List of available routes:

`POST /predict` - Predict House Prices\
`GET /` - Basic user form to enter property details


## License

[MIT](LICENSE)
