# Store Intelligence Platform

## Overview

The Store Intelligence Platform is an AI-powered retail analytics system that processes CCTV footage to generate real-time customer intelligence. The system detects visitors entering the store, tracks movement across camera streams, generates structured events, and exposes analytics through production-style APIs.

The solution was built using computer vision, event streaming concepts, and lightweight analytics services. It demonstrates how retail stores can transform raw CCTV footage into actionable business insights.

---

## System Architecture

CCTV Cameras

↓

YOLOv8 Person Detection

↓

ByteTrack Multi-Object Tracking

↓

Visitor Event Generation

↓

FastAPI Event Ingestion

↓

CSV + JSONL Event Storage

↓

Analytics APIs

↓

Business Intelligence Metrics

---

## Data Flow

1. CCTV footage is processed frame by frame using OpenCV.
2. YOLOv8 detects persons in each frame.
3. ByteTrack assigns persistent identities to detected visitors.
4. New visitor appearances generate structured events.
5. Events are sent to FastAPI through REST endpoints.
6. Events are stored in CSV and JSONL formats.
7. Analytics APIs compute metrics such as visitor counts and funnel statistics.
8. Results are exposed through Swagger documentation and API endpoints.

---

## Event Pipeline

The platform generates structured events representing customer activity.

Supported event types:

* ENTRY
* BILLING

Example Event:

```json
{
  "event_type": "entry",
  "id_token": "ID_23",
  "store_code": "store_1",
  "camera_id": "cam3",
  "event_timestamp": "2026-06-04T21:00:00"
}
```

Events are stored in JSONL format for downstream processing and analytics.

---

## Analytics APIs

### GET /health

Returns service health status.

### POST /events/ingest

Receives visitor events from detection pipelines.

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

Returns simple traffic anomaly indicators based on visitor activity.

---

## AI-Assisted Decisions

AI tools were used during development to accelerate implementation, debugging, API design, documentation generation, and architecture validation.

The following engineering decisions were AI-assisted and subsequently reviewed:

* YOLOv8 model selection
* ByteTrack integration strategy
* FastAPI endpoint design
* Event schema design
* JSONL event generation workflow
* Documentation structure

All generated code and design decisions were manually reviewed and validated before inclusion in the final solution.

---

## Tradeoffs

Several practical tradeoffs were made to ensure a working end-to-end prototype within the hackathon timeline.

* Lightweight event storage using CSV and JSONL instead of distributed databases.
* Single-camera visitor counting rather than full cross-camera re-identification.
* Simplified anomaly detection based on event counts.
* Billing events generated from billing camera detections rather than POS integration.

These decisions prioritize reliability and demonstration completeness.

---

## Limitations

Current limitations include:

* No cross-camera person re-identification.
* No staff exclusion model.
* No facial recognition.
* No age or gender prediction.
* No direct POS transaction integration.
* Limited multi-store aggregation.

---

## Future Improvements

Future enhancements include:

* Staff exclusion using appearance embeddings.
* Cross-camera identity matching.
* Zone-level heatmaps.
* Shelf interaction analytics.
* POS transaction integration.
* Real-time dashboard.
* Multi-store analytics aggregation.
* Advanced anomaly detection models.

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
