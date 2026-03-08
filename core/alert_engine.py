from datetime import datetime
import time
from core.gps import GPSModule
from core.database import log_alert
from core.cloud_client import CloudClient


class AlertEngine:
    def __init__(self):
        self.gps = GPSModule()
        self.cloud = CloudClient()

        self.last_severity = None
        self.last_alert_time = 0
        self.cooldown_seconds = 5

        self.stations = [
            {"name": "Pune Junction", "lat": 18.5286, "lon": 73.8745},
            {"name": "Shivajinagar", "lat": 18.5308, "lon": 73.8475},
            {"name": "Hadapsar", "lat": 18.5089, "lon": 73.9260},
        ]

    def _nearest_station(self, lat, lon):
        return self.stations[0]["name"]

    def generate_alert(self, severity):
        current_time = time.time()

        # Prevent spam
        if severity == self.last_severity and (current_time - self.last_alert_time) < self.cooldown_seconds:
            return

        self.last_severity = severity
        self.last_alert_time = current_time

        location = self.gps.get_location()
        current_speed = self.gps.get_speed()
        station = self._nearest_station(location["lat"], location["lon"])

        if severity == "HIGH":
            recommended_speed = 0
            action = "STOP train & notify station"
        elif severity == "MEDIUM":
            recommended_speed = 70
            action = "Reduce speed"
        else:
            recommended_speed = current_speed
            action = "Continue monitoring"

        alert_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n🚨 RAILWAY SAFETY ALERT 🚨")
        print(f"Time           : {alert_time_str}")
        print(f"Location       : {location['lat']}, {location['lon']}")
        print(f"Nearest Station: {station}")
        print(f"Current Speed  : {current_speed} km/h")
        print(f"Recommended    : {recommended_speed} km/h")
        print(f"Action         : {action}")

        log_alert(
            time=alert_time_str,
            severity=severity,
            action=action,
            source="AI Camera",
            status="SENT"
        )

        payload = {
            "time": alert_time_str,
            "severity": severity,
            "station": station,
            "action": action
        }

        # Send to cloud (printing handled inside cloud_client.py)
        self.cloud.send_alert(payload)
