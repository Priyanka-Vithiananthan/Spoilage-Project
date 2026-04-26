from flask import Flask, render_template, jsonify
import random, time

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
    temp = round(random.uniform(3,10),2)
    risk = get_risk(temp)

    return jsonify({
        "temp": temp,
        "risk": risk,
        "prediction": predict(temp),
        "loss": loss(risk)
    })

app.run(debug=True)