from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class Detection:
    xyxy: Tuple[float, float, float, float]
    confidence: float
    class_id: int
    class_name: str

@dataclass
class DetectionBatch:
    frame_id: int
    detections: List[Detection]
    inference_ms: float
