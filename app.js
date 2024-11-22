const { PythonShell } = require('python-shell');
const path = require('path');

// Функція для прогнозу
function predict(data, callback) {
    const options = {
        scriptPath: path.join(__dirname, 'ml'),
        args: [JSON.stringify(data)]
    };

    PythonShell.run('predict.py', options, (err, results) => {
        if (err) throw err;
        callback(results[0]); // Результат обчислення
    });
}

// Маршрут для запиту прогнозу
app.post('/predict', (req, res) => {
    const marketData = req.body.data; // Дані від клієнта
    predict(marketData, (result) => {
        res.json({ prediction: result });
    });
});
