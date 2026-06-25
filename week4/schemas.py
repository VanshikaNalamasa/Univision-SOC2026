from pydantic import BaseModel, HttpUrl
from typing import Optional

class AnalyzeRequest(BaseModel):
    image_url: str
    confidence_threshold: float = 0.5
    model_name: str = "yolov8n"

class DetectionResult(BaseModel):
    label: str
    confidence: float
    box: list[int]

class AnalyzeResponse(BaseModel):
    status: str
    image_url: str
    detections: list[DetectionResult]
    processing_time_ms: float