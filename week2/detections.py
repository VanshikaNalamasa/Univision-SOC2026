# Week 2 - Python Foundations
# Detection filtering and confidence scoring

from typing import TypedDict

class Detection(TypedDict):
    label: str
    confidence: float
    box: list[int]  # [x1, y1, x2, y2]


def average_confidence(scores: list[float]) -> float:
    """Returns average confidence score from a list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_detections(detections: list[Detection], threshold: float) -> list[Detection]:
    """Returns only detections above the confidence threshold."""
    return [d for d in detections if d["confidence"] >= threshold]


if __name__ == "__main__":
    sample = [
        {"label": "person", "confidence": 0.91, "box": [10, 20, 100, 200]},
        {"label": "car",    "confidence": 0.45, "box": [50, 60, 300, 400]},
        {"label": "helmet", "confidence": 0.78, "box": [30, 10, 80, 60]},
    ]

    print("All detections:", sample)
    print("Filtered (>0.7):", filter_detections(sample, 0.7))
    print("Average confidence:", average_confidence([d["confidence"] for d in sample]))