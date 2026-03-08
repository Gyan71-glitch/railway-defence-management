import time

class GPSModule:
    def __init__(self):
        # Fixed demo GPS location (Pune)
        self.latitude = 18.5204
        self.longitude = 73.8567

        # Simulated speed state
        self.speed = 0
        self.start_time = time.time()

    def get_location(self):
        return {
            "lat": self.latitude,
            "lon": self.longitude
        }

    def get_speed(self):
        """
        Simulates train speed over time:
        0–5 sec   → 0 km/h
        5–15 sec  → 120 km/h
        >15 sec   → 90 km/h
        """
        elapsed = time.time() - self.start_time

        if elapsed < 5:
            self.speed = 0
        elif elapsed < 15:
            self.speed = 120
        else:
            self.speed = 90

        return self.speed
