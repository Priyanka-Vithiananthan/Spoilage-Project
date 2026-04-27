from flask import Flask, render_template, jsonify
import random, time

current_temp = 6.0
current_humidity = 70

app = Flask(__name__)


def get_risk(temp):
    if temp > 8:
        return "HIGH RISK ⚠️"
    elif temp > 6:
        return "MEDIUM RISK"
    else:
        return "SAFE"

def predict(temp):
    if temp > 8:
        return "Spoilage in 2 hours"
    elif temp > 6:
        return "Spoilage in 5 hours"
    return "No risk"

def loss(risk):
    if "HIGH" in risk:
        return "₹10000"
    elif "MEDIUM" in risk:
        return "₹3000"
    return "₹0"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    temp = round(random.uniform(3, 10), 5)
    humidity = random.randint(50, 95)

    # Rule-based risk (reliable)
    if temp > 8 or humidity > 80:
        risk = "HIGH RISK ⚠️"
        prediction = "Spoilage likely"
        loss_val = "₹10000"
    elif temp > 6:
        risk = "MEDIUM RISK"
        prediction = "Monitor closely"
        loss_val = "₹3000"
    else:
        risk = "SAFE"
        prediction = "No spoilage expected"
        loss_val = "₹0"

    return jsonify({
        "temp": temp,
        "humidity": humidity,
        "risk": risk,
        "prediction": prediction,
        "loss": loss_val
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
