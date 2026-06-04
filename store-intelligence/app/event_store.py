import csv
import os
from types import SimpleNamespace

events = []

CSV_FILE = "events.csv"

if os.path.exists(CSV_FILE):

    with open(
        CSV_FILE,
        "r",
        newline=""
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            events.append(
                SimpleNamespace(
                    event_id=row["event_id"],
                    visitor_id=int(row["visitor_id"]),
                    camera_id=row["camera_id"],
                    event_type=row["event_type"],
                    timestamp=row["timestamp"]
                )
            )

print(
    f"Loaded {len(events)} events "
    f"from CSV"
)