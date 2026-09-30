from dataclasses import dataclass

@dataclass
class DetectorConfig:
    weights: str = "yolo11n.pt"
    confidence: float = 0.25
    iou: float = 0.45
    imgsz: int = 640
    device: str = "auto"
    half: bool = False
    max_det: int = 300
