from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = r"data\videos\CCTV Footage\CAM 3.mp4"

cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    if frame_count % 30 != 0:
        continue

    results = model(frame, verbose=False)

    people = 0

    for box in results[0].boxes:

        cls = int(box.cls[0])

        if cls == 0:
            people += 1

    print(
        f"Frame {frame_count} | People Detected: {people}"
    )

cap.release()

print("Finished")