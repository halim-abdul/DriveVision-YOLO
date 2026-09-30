from dataclasses import dataclass

@dataclass
class TrackerConfig:
    high_conf: float = 0.5
    low_conf: float = 0.1
    match_iou: float = 0.3
    max_age: int = 30
    min_hits: int = 3
    fps: float = 30.0
