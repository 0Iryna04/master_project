import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# Завантаження даних
def load_data(file_path):
    data = pd.read_csv(file_path)
    print(f"Data size: {len(data)}")  # Check the number of rows in the dataset
    print(data.columns)  # Check column names
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['l'].values.reshape(-1, 1))
    return scaled_data, scaler

# Формування послідовностей для LSTM
def prepare_data(data, lookback=5):  # Try reducing lookback to a smaller value
    X, y = [], []
    for i in range(lookback, len(data)):
        print(f"i = {i}, data[i-lookback:i] = {data[i-lookback:i, 0]}")  # Debug print to check data sequence
        X.append(data[i-lookback:i, 0])
        y.append(data[i, 0])
    print(f"Data size: {len(X)}")  # Should show how many sequences were created
    return np.array(X), np.array(y)



# Створення моделі
def build_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

if __name__ == "__main__":
    # Підготовка даних
    data, scaler = load_data('ml/historical_data.csv')  # Історичні дані
    X, y = prepare_data(data)

    print(X.shape, y.shape)

    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Навчання моделі
    model = build_model((X.shape[1], 1))
    model.fit(X, y, batch_size=32, epochs=10)
    model.save('my_model.keras')

