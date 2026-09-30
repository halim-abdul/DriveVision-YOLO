def iou(a, b):
    ax1, ay1, ax2, ay2 = a; bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    aa = max(0, ax2 - ax1) * max(0, ay2 - ay1)
    bb = max(0, bx2 - bx1) * max(0, by2 - by1)
    return inter / (aa + bb - inter + 1e-9)

def class_agnostic_nms(detections, threshold=0.5):
    ordered = sorted(detections, key=lambda d: d.confidence, reverse=True)
    keep = []
    while ordered:
        best = ordered.pop(0)
        keep.append(best)
        ordered = [d for d in ordered if iou(best.xyxy, d.xyxy) < threshold]
    return keep
