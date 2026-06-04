from ultralytics import YOLO
import cv2
import requests
from datetime import datetime

# =====================================
# CONFIG
# =====================================
# =====================================
# CONFIG
# =====================================

STORE_CODE = "store_1"
VIDEO_PATH = r"data\videos\Store 1-20260602T101818Z-3-001ec38db8\Store 1\CAM 5 - billing.mp4"

CAMERA_ID = "CAM5"

MODEL_PATH = "yolov8n.pt"
# =====================================
# API HELPER
# =====================================

def send_entry_event(visitor_id):

    payload = {
        "event_id": f"evt_{visitor_id}_{int(datetime.now().timestamp())}",
        "visitor_id": int(visitor_id),
        "camera_id": CAMERA_ID,
        "event_type": "BILLING",
        "timestamp": datetime.now().isoformat()
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/events/ingest",
            json=payload,
            timeout=5
        )

        print(
            f"BILLING SENT -> Visitor {visitor_id} | "
            f"Status={response.status_code}"
        )

    except Exception as e:

        print("API ERROR:", e)

# =====================================
# LOAD MODEL
# =====================================

print("Loading model...")

model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():

    print("Cannot open video")
    exit()

# =====================================
# STATE
# =====================================

frame_no = 0

sent_entry_ids = set()

# =====================================
# MAIN LOOP
# =====================================

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    frame_no += 1

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=[0],
        conf=0.5,
        verbose=False
    )
    annotated = results[0].plot()

    if results[0].boxes.id is not None:

        track_ids = (
            results[0]
            .boxes
            .id
            .cpu()
            .numpy()
            .astype(int)
        )

        for track_id in track_ids:

            # =====================================
            # NEW VISITOR DETECTED
            # =====================================

            if track_id not in sent_entry_ids:

                sent_entry_ids.add(track_id)

                print(
                    f"NEW VISITOR DETECTED: "
                    f"{track_id}"
                )

                send_entry_event(track_id)

    cv2.imshow(
        "Store Intelligence Tracking",
        annotated
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# =====================================
# CLEANUP
# =====================================

cap.release()
cv2.destroyAllWindows()

# =====================================
# FINAL REPORT
# =====================================

print("\n" + "=" * 60)

print(
    f"TOTAL UNIQUE VISITORS DETECTED: "
    f"{len(sent_entry_ids)}"
)

print("=" * 60)