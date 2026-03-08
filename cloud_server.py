from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random

app = Flask(__name__)

# In-memory alert storage
alerts = []


@app.route("/")
def home():
    return "🚆 Railway AI Cloud Server Running"


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", alerts=alerts)


@app.route("/api/alert", methods=["POST"])
def receive_alert():
    data = request.json

    ticket_id = f"TKT-{random.randint(1000,9999)}"

    alert_record = {
        "ticket_id": ticket_id,
        "time": data.get("time"),
        "station": data.get("station"),
        "severity": data.get("severity"),
        "action": data.get("action"),
        "speed": data.get("current_speed")
    }

    alerts.append(alert_record)

    print("\n📡 ALERT RECEIVED BY CLOUD")
    print(alert_record)

    return jsonify({
        "status": "SUCCESS",
        "ticket_id": ticket_id,
        "message": "Station notified successfully"
    })


if __name__ == "__main__":
    print("🚀 Starting Railway Cloud Server...")
    app.run(host="0.0.0.0", port=5050, debug=True)
