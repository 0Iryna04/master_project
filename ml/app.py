from flask import Flask, request, jsonify, render_template  # Add render_template here
import tensorflow as tf
import pandas as pd

app = Flask(__name__)
model = tf.keras.models.load_model('model.h5')

def get_last_prices():
    data = pd.read_csv('historical_data.csv')
    return data['price'].tail(5).tolist()  # Adjust 'price' column name

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/predict', methods=['POST'])
def predict():
    input_data = get_last_prices()
    prediction = model.predict([input_data])
    return jsonify({'prediction': prediction[0][0]})

if __name__ == '__main__':
    app.run(debug=True)
