from ultralytics import YOLO


class YOLODetector:
    def __init__(self):
        print("[INFO] Loading local YOLOv8n model...")
        self.model = YOLO("yolov8n.pt")
        print("[INFO] YOLO loaded successfully")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        if not results or len(results[0].boxes) == 0:
            return None

        # Take highest confidence detection
        boxes = results[0].boxes
        confidences = boxes.conf.tolist()
        classes = boxes.cls.tolist()

        max_index = confidences.index(max(confidences))

        return {
            "confidence": confidences[max_index],
            "class_id": int(classes[max_index])
        }
