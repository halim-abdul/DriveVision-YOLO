from dataclasses import dataclass

@dataclass
class FusionConfig:
    depth_model: str = "depth-anything-v2-small"
    sign_confidence: float = 0.4
    depth_scale: float = 1.0
    min_depth_m: float = 0.1
    max_depth_m: float = 120.0
