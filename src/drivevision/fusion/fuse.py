from dataclasses import dataclass
from .depth_stats import robust_box_depth

@dataclass
class FusedObject:
    class_name:str
    confidence:float
    xyxy:tuple
    distance_m:float

def fuse_detections(detections,depth_map):
    return [FusedObject(d.class_name,d.confidence,d.xyxy,robust_box_depth(depth_map,d.xyxy)) for d in detections]
