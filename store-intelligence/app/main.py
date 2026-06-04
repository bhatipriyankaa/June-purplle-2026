from fastapi import FastAPI
from app.models import Event
from app.event_store import events
from app.db import save_event
import csv
app = FastAPI(title="Store Intelligence API")


@app.get("/")
def root():
    return {
        "message": "Store Intelligence Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/events/ingest")
def ingest(event: Event):

    events.append(event)

    save_event(event)

    return {
        "status": "success",
        "events_received": len(events)
    }

@app.get("/events")
def get_events():
    return events

@app.get("/metrics")
def metrics():

    total_visitors = len(
        set(
            event.visitor_id
            for event in events
        )
    )

    total_entries = len(
        [
            e for e in events
            if e.event_type.upper() == "ENTRY"
        ]
    )

    total_billings = len(
        [
            e for e in events
            if e.event_type.upper() == "BILLING"
        ]
    )

    total_exits = len(
        [
            e for e in events
            if e.event_type.upper() == "EXIT"
        ]
    )

    return {
        "total_events": len(events),
        "total_visitors": total_visitors,
        "total_entries": total_entries,
        "total_billings": total_billings,
        "total_exits": total_exits
    }

@app.get("/funnel")
def funnel():

    visitors = len(
        set(
            e.visitor_id
            for e in events
            if e.event_type == "ENTRY"
        )
    )

   

    purchasers = 0

    with open(
        "Brigade_Bangalore_10_April_26.csv",
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(f)

        purchasers = len(list(reader))
    dropoff = visitors - purchasers

    conversion_rate = 0

    if visitors > 0:
        conversion_rate = round(
            (purchasers / visitors) * 100,
            2
        )

    return {
        "visitors": visitors,
        "purchasers": purchasers,
        "dropoff": dropoff,
        "conversion_rate": conversion_rate
    }

@app.get("/anomalies")
def anomalies():

    if len(events) > 20:

        return {
            "status": "anomaly_detected",
            "reason": "High visitor traffic"
        }

    return {
        "status": "normal"
    }

@app.get("/sales")
def sales():

    import csv

    total_transactions = 0
    total_revenue = 0

    with open("Brigade_Bangalore_10_April_26.csv", "r", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            total_transactions += 1

            try:
                total_revenue += float(row["NMV"])
            except:
                pass

    return {
        "transactions": total_transactions,
        "revenue": round(total_revenue, 2)
    }

@app.get("/top-brands")
def top_brands():

    brands = {}

    with open(
        "Brigade_Bangalore_10_April_26.csv",
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            brand = row["brand_name"]

            try:
                revenue = float(row["NMV"])
            except:
                revenue = 0

            brands[brand] = brands.get(
                brand,
                0
            ) + revenue

    top5 = sorted(
        brands.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    return {
        "top_brands": top5
    }