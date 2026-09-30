from dataclasses import dataclass

@dataclass(frozen=True)
class DrivingEvent:
    frame_id:int
    timestamp_s:float
    event_type:str
    severity:str
    message:str
    object_id:int|None=None
