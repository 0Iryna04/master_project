document.getElementById('predict-btn').addEventListener('click', () => {
    const data = getMarketData(); // Функція отримує останні дані з графіку
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data })
    })
        .then((response) => response.json())
        .then((result) => {
            alert(`Прогнозована ціна: ${result.prediction}`);
        })
        .catch((error) => console.error('Помилка:', error));
});
