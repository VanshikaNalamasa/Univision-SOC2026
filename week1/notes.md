# Week 1 — Computational Thinking

## Core Concepts

- **Variable**: stores a value. Example: `frame_count = 0`
- **Condition**: chooses between paths. Example: if motion detected, capture frame
- **Loop**: repeats a step. Example: keep reading camera frames
- **Function**: reusable named operation. Example: `analyze_frame(image)`
- **List**: ordered items. Example: list of detections in one frame
- **Dictionary**: maps names to values. Example: `{"label": "person", "confidence": 0.91}`
- **State**: what the system remembers right now. Example: pipeline status = running
- **Event**: something that happens and triggers behavior. Example: motion detected
- **Pipeline**: sequence of steps where each transforms data

## Camera Alert Flowchart

START
  -> Is camera online?
      NO  -> Log error, retry after 5s, go to START
      YES -> Capture frame
  -> Is frame valid?
      NO  -> Discard frame, go to START
      YES -> Run motion detection
  -> Is motion detected?
      NO  -> Wait, go to START
      YES -> Send frame to analysis pipeline
  -> Analysis complete
  -> Store result
  -> Emit alert event
  -> END

## Reflection

The key insight from Week 1 is that an AI vision system is not one 
big model. It is a pipeline of small logical decisions. Each step 
transforms data and passes it forward. Understanding this before 
touching any model is essential.