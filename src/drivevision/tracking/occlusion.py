from .geometry import bbox_iou

def occlusion_score(track,others):
    return max((bbox_iou(track.xyxy,o.xyxy) for o in others if o.track_id!=track.track_id),default=0.0)

def is_occluded(track,others,threshold=0.5):
    return occlusion_score(track,others)>=threshold
