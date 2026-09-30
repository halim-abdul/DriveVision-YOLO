from dataclasses import dataclass,field
from typing import Any,Dict,List

@dataclass
class SceneState:
    frame_id:int
    timestamp_s:float
    objects:List[Any]=field(default_factory=list)
    lanes:Dict[str,Any]=field(default_factory=dict)
    signs:List[Any]=field(default_factory=list)
    metrics:Dict[str,float]=field(default_factory=dict)
