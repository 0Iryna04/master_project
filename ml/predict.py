import numpy as np
import sys
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Завантаження моделі
model = load_model('ml/model.h5')

# Приймаємо вхідні дані
input_data = np.array(eval(sys.argv[1]))  # Дані у вигляді JSON-стрічки
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(input_data.reshape(-1, 1))

# Формуємо послідовність
X = np.array([scaled_data[-60:]])
X = X.reshape(X.shape[0], X.shape[1], 1)

# Прогноз
prediction = model.predict(X)
print(scaler.inverse_transform(prediction)[0][0])
