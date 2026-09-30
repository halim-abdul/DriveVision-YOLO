import argparse
import cv2
from drivevision.detection.detector import YOLODetector
from drivevision.detection.stream import video_frames
from drivevision.detection.visualize import draw_detections

p = argparse.ArgumentParser()
p.add_argument("source")
p.add_argument("--out", default="runs/detect.mp4")
a = p.parse_args()
model = YOLODetector().load()
writer = None
for i, frame in video_frames(a.source):
    batch = model.predict(frame, i)
    vis = draw_detections(frame, batch.detections)
    if writer is None:
        writer = cv2.VideoWriter(a.out, cv2.VideoWriter_fourcc(*"mp4v"), 30, (vis.shape[1], vis.shape[0]))
    writer.write(vis)
if writer: writer.release()
