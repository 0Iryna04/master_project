rsiSettings = {
    "analysisLength"    : 14,  //кількість свічок для аналізу
    "shortTimeFrame"    : 15,  //довжина короткотривалого аналізу
    "longTimeFrame"     : 60,  //довжина довготривалого аналізу
    "highLevel"         : 70,  //верхня межа сигналу
    "lowLevel"          : 30,  //нижня межа сигналу
}

// rsiS.js
async function calculateRSI(prices) {
    // Логіка для обчислення RSI
    return rsi_value;  // Повертає значення RSI
}

// Використання результатів машинного навчання з RSI
async function makeDecision(prices) {
    const rsiValue = await calculateRSI(prices);
    const predictedPrice = await predictPrice(model, prices);  // Прогнозування ціни
    
    if (predictedPrice > prices[prices.length - 1] && rsiValue < 30) {
        console.log("Покупка за прогнозом та RSI!");
        // Виконати операцію покупки
    } else if (predictedPrice < prices[prices.length - 1] && rsiValue > 70) {
        console.log("Продаж за прогнозом та RSI!");
        // Виконати операцію продажу
    }
};
