import requests
import pandas as pd


url = "https://api.exmo.com/v1.1/candles_history"
params = {
    "symbol": "BTC_USD",
    "resolution": "1D",  # Один день
    "from": 1633046400,  # Початок періоду (Unix час)
    "to": 1635724800     # Кінець періоду (Unix час)
}

response = requests.get(url, params=params)
if response.status_code == 200:
    print(response.json())  # Виводимо структуру відповіді
else:
    print("Помилка запиту:", response.status_code)

data = response.json()["candles"]
df = pd.DataFrame(data)
df.to_csv('ml/historical_data.csv', index=False)
