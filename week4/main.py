from fastapi import FastAPI, HTTPException
from schemas import AnalyzeRequest, AnalyzeResponse, DetectionResult
import time

app = FastAPI(title="Uni-Vision API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "uni-vision"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_image(request: AnalyzeRequest):
    if not request.image_url.startswith("http"):
        raise HTTPException(status_code=422, detail="Invalid image URL")

    start = time.time()

    # Simulated detections (replace with real model later)
    fake_detections = [
        DetectionResult(label="person", confidence=0.91, box=[10, 20, 100, 200]),
        DetectionResult(label="helmet", confidence=0.78, box=[30, 10, 80, 60]),
    ]

    filtered = [d for d in fake_detections if d.confidence >= request.confidence_threshold]
    elapsed = (time.time() - start) * 1000

    return AnalyzeResponse(
        status="success",
        image_url=request.image_url,
        detections=filtered,
        processing_time_ms=round(elapsed, 2)
    )