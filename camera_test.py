import cv2

# Open default camera
cap = cv2.VideoCapture(1)

print("Camera starting... Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not working")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
