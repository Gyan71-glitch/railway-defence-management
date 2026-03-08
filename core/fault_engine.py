import random
from datetime import datetime

class FaultEngine:
    def detect_fault(self):
        chance = random.randint(1, 100)

        if chance < 85:
            return {
                "status": "TRACK OK",
                "severity": "NONE",
                "time": datetime.now()
            }

        return {
            "status": "FAULT DETECTED",
            "severity": random.choice(["LOW", "MEDIUM", "HIGH"]),
            "time": datetime.now()
        }

