from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Track:
    track_id: int
    xyxy: Tuple[float,float,float,float]
    class_name: str
    confidence: float
    age: int = 1
    missed: int = 0
    history: List[Tuple[float,float]] = field(default_factory=list)
