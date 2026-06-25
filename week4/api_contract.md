# Week 4 — API Contract

## GET /health
**Response:**
```json
{"status": "ok", "service": "uni-vision"}
```

## POST /analyze
**Request:**
```json
{
  "image_url": "https://example.com/frame.jpg",
  "confidence_threshold": 0.5,
  "model_name": "yolov8n"
}
```
**Response:**
```json
{
  "status": "success",
  "image_url": "https://example.com/frame.jpg",
  "detections": [
    {"label": "person", "confidence": 0.91, "box": [10, 20, 100, 200]}
  ],
  "processing_time_ms": 12.4
}
```