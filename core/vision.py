import cv2
import time
from ultralytics import YOLO


class RailwayVision:
    def __init__(self, camera_index=0):
        print("[INFO] Initializing camera...")
        self.cap = cv2.VideoCapture(camera_index)

        print("[INFO] Loading YOLOv8 model...")
        self.model = YOLO("yolov8n.pt")  # using pretrained model
        print("[INFO] YOLO loaded successfully")

        if not self.cap.isOpened():
            raise RuntimeError("Camera not accessible")

        print("[INFO] Camera opened successfully")

        self.prev_time = 0

    def run_single_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        frame = cv2.resize(frame, (640, 480))

        # FPS Calculation
        current_time = time.time()
        if self.prev_time == 0:
            fps = 0
        else:
            fps = 1 / (current_time - self.prev_time)
        self.prev_time = current_time

        # YOLO Detection
        results = self.model(frame)

        severity = "LOW"

        if results and len(results[0].boxes) > 0:
            annotated_frame = results[0].plot()

            # Take highest confidence box
            confidences = results[0].boxes.conf.tolist()
            max_conf = max(confidences)

            if max_conf > 0.7:
                severity = "HIGH"
            elif max_conf > 0.4:
                severity = "MEDIUM"
            else:
                severity = "LOW"

            frame = annotated_frame

        # Show FPS
        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow("Railway AI Vision", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()

        return severity
