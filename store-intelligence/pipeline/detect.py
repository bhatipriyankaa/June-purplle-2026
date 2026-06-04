from ultralytics import YOLO
import cv2

print("Loading model...")
model = YOLO("yolov8n.pt")
video_path = r"data\videos\CCTV Footage\CAM 3.mp4"
print(f"Opening video: {video_path}")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Could not open video")
    exit()

print("Video opened successfully")

ret, frame = cap.read()

if not ret:
    print("ERROR: Could not read first frame")
    exit()

print("Frame shape:", frame.shape)

results = model(frame, verbose=False)

print("Detections found:", len(results[0].boxes))

annotated = results[0].plot()

cv2.imshow("Detection", annotated)

print("Press any key inside image window...")

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows() 