import cv2

class Camera:
    def __init__(self):
        # Try camera index 0 first, then 1
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.cap = cv2.VideoCapture(1)

        if not self.cap.isOpened():
            raise RuntimeError("Camera could not be opened (0 or 1)")

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
