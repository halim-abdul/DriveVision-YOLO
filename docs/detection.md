# YOLO Detection

The detection subsystem wraps Ultralytics YOLO behind a stable project API. It supports image/video inference, road-user class filtering, latency measurement, calibration analysis, ROI gating and model export.

## Evaluation
Report mAP50-95, per-class AP, precision/recall, calibration error, latency percentiles, throughput and failure cases across day/night, rain, glare and occlusion.

## Safety
This repository is a research prototype. Perception outputs must not be used as a sole control signal in a road vehicle.
