# Store Intelligence Platform

## Overview

Store Intelligence Platform is an AI-powered retail analytics solution that transforms raw CCTV footage into structured business intelligence.

The system detects customers, tracks movement across frames, generates visitor events, stores analytics data, and exposes real-time APIs for operational insights.

The solution demonstrates an end-to-end pipeline combining computer vision, event generation, event storage, and analytics services.

---

## Features

### Computer Vision

* YOLOv8 person detection
* ByteTrack multi-object tracking
* Visitor identity persistence
* Entry event generation
* Billing event generation

### Event Processing

* Real-time event ingestion
* Structured JSONL event stream
* CSV event persistence
* Visitor activity logging

### Analytics APIs

* Health monitoring
* Visitor metrics
* Funnel analytics
* Traffic anomaly reporting

---

## System Architecture

CCTV Cameras

↓

YOLOv8 Detection

↓

ByteTrack Tracking

↓

Visitor Event Generation

↓

FastAPI Event Ingestion

↓

CSV + JSONL Storage

↓

Analytics APIs

↓

Business Intelligence Metrics

---

## Project Structure

```text
app/
├── main.py
├── models.py
├── event_store.py
└── db.py

pipeline/
├── entry_detector.py
└── billing_detector.py

data/
├── videos/
└── layouts/

events.csv
events.jsonl

README.mdwe have one folder output but nothing in it 

DESIGN.md
CHOICES.md
requirements.txt
```

---

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Start FastAPI:

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Running Entry Detection

```bash
python pipeline\entry_detector.py
```

This processes entry camera footage and generates ENTRY events.

---

## Running Billing Detection

```bash
python pipeline\billing_detector.py
```

This processes billing-area footage and generates BILLING events.

---

## Event Storage

### CSV Output

```text
events.csv
```

Stores structured event records for offline analysis.

### JSONL Output

```text
events.jsonl
```

Stores event streams in JSONL format suitable for downstream analytics systems.

Example:

```json
{
  "event_type": "entry",
  "id_token": "ID_12",
  "store_code": "store_1",
  "camera_id": "cam3",
  "event_timestamp": "2026-06-04T21:00:00"
}
```

---

## API Endpoints

### GET /health

Returns service health status.

### POST /events/ingest

Receives events from detection pipelines.

### GET /metrics

Returns:

* Total Events
* Total Visitors
* Total Entries
* Total Billings
* Total Exits

### GET /funnel

Returns:

* Visitors
* Purchasers
* Drop-off Count
* Conversion Rate

### GET /anomalies

Returns traffic anomaly indicators.

---

## Technologies Used

* Python
* YOLOv8
* ByteTrack
* OpenCV
* FastAPI
* Pydantic
* JSONL
* CSV

---

## Assumptions

* Each new tracking identity is treated as a visitor.
* Billing camera detections generate billing events.
* CCTV footage may contain occlusions and tracking noise.
* Staff exclusion is documented but not fully implemented.

---

## Current Limitations

* No cross-camera re-identification.
* No staff exclusion model.
* No age or gender estimation.
* No POS transaction integration.
* Limited multi-store aggregation.

---

## Future Improvements

* Staff exclusion system
* Cross-camera identity matching
* Zone analytics
* Heatmap generation
* Shelf interaction analytics
* POS integration
* Real-time dashboard
* Multi-store aggregation
* Advanced anomaly detection
