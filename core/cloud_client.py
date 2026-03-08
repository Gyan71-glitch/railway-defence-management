import requests


class CloudClient:
    def __init__(self):
        self.url = "http://127.0.0.1:5050/api/alert"
        print("[INFO] Connected to real Flask cloud server")

    def send_alert(self, payload):
        try:
            response = requests.post(self.url, json=payload)
            data = response.json()

            print("☁ Cloud Response:", data)

            return data

        except Exception as e:
            print("❌ Cloud connection failed:", e)
            return {"status": "FAILED"}
