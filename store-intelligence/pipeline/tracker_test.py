from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = r"data\videos\CCTV Footage\CAM 3.mp4"

cap = cv2.VideoCapture(video_path)

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    annotated = results[0].plot()

    cv2.imshow("Tracking", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()