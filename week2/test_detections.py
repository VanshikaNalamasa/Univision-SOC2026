from detections import filter_detections, average_confidence

def test_filter_removes_low_confidence():
    detections = [
        {"label": "person", "confidence": 0.91, "box": [0,0,10,10]},
        {"label": "car",    "confidence": 0.30, "box": [0,0,10,10]},
    ]
    result = filter_detections(detections, 0.7)
    assert len(result) == 1
    assert result[0]["label"] == "person"

def test_filter_empty_list():
    assert filter_detections([], 0.5) == []

def test_average_confidence_normal():
    assert average_confidence([0.9, 0.8, 0.7]) == 0.8

def test_average_confidence_empty():
    assert average_confidence([]) == 0.0