import time
from core.vision import RailwayVision
from core.alert_engine import AlertEngine


def main():
    print("🚆 Railway AI system started successfully")

    vision = RailwayVision(camera_index=0)
    alert_engine = AlertEngine()

    print("System initialized. Running inspection loop...\n")

    try:
        while True:
            severity = vision.run_single_frame()

            if severity:
                alert_engine.generate_alert(severity)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n🛑 System stopped safely")


if __name__ == "__main__":
    main()
