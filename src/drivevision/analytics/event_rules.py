from .events import DrivingEvent

def proximity_event(frame_id,timestamp,obj,near_m=8.0):
    distance=getattr(obj,"distance_m",float("inf"))
    if distance<near_m:
        return DrivingEvent(frame_id,timestamp,"proximity","warning",f"{obj.class_name} within {distance:.1f} m",getattr(obj,"track_id",None))
    return None
