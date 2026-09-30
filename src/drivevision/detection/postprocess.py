from .types import Detection

def filter_classes(detections, allowed):
    allowed = set(allowed)
    return [d for d in detections if d.class_name in allowed]

def min_area_filter(detections, min_area: float = 16.0):
    out = []
    for d in detections:
        x1, y1, x2, y2 = d.xyxy
        if max(0.0, x2 - x1) * max(0.0, y2 - y1) >= min_area:
            out.append(d)
    return out

def center_xy(det: Detection):
    x1, y1, x2, y2 = det.xyxy
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
