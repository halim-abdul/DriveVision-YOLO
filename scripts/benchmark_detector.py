import argparse
import statistics
from drivevision.detection.detector import YOLODetector
from drivevision.detection.stream import video_frames

p = argparse.ArgumentParser()
p.add_argument("source")
p.add_argument("--frames", type=int, default=200)
a = p.parse_args()
model = YOLODetector().load()
times = []
for i, frame in video_frames(a.source):
    times.append(model.predict(frame, i).inference_ms)
    if len(times) >= a.frames: break
mean = statistics.mean(times) if times else 0.0
print({"frames": len(times), "mean_ms": round(mean, 2), "fps": round(1000 / max(mean, 1e-9), 2)})
