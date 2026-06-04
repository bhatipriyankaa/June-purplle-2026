import csv
import json

INPUT_CSV = "events.csv"
OUTPUT_JSONL = "events.jsonl"

with open(INPUT_CSV, "r", encoding="utf-8") as csvfile:

    reader = csv.DictReader(csvfile)

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as jsonlfile:

        for row in reader:

            event = {
                "event_type": row["event_type"].lower(),
                "id_token": f"ID_{row['visitor_id']}",
                "store_code": "store_1",
                "camera_id": row["camera_id"].lower(),
                "event_timestamp": row["timestamp"],
                "is_staff": False,
                "gender_pred": None,
                "age_pred": None,
                "age_bucket": None,
                "is_face_hidden": False,
                "group_id": None,
                "group_size": None
            }

            jsonlfile.write(
                json.dumps(event) + "\n"
            )

print("events.jsonl generated successfully")