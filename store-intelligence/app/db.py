import csv
import os
import json

CSV_FILE = "events.csv"
JSONL_FILE = "events.jsonl"


def save_event(event):

    file_exists = os.path.exists(CSV_FILE)

    # CSV
    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "event_id",
                "visitor_id",
                "camera_id",
                "event_type",
                "timestamp"
            ])

        writer.writerow([
            event.event_id,
            event.visitor_id,
            event.camera_id,
            event.event_type,
            event.timestamp
        ])

    # JSONL
    json_event = {
        "event_type": event.event_type.lower(),
        "id_token": f"ID_{event.visitor_id}",
        "store_code": "store_1",
        "camera_id": event.camera_id.lower(),
        "event_timestamp": str(event.timestamp),
        "is_staff": False,
        "gender_pred": None,
        "age_pred": None,
        "age_bucket": None,
        "is_face_hidden": False,
        "group_id": None,
        "group_size": None
    }

    with open(
        JSONL_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            json.dumps(json_event) + "\n"
        )