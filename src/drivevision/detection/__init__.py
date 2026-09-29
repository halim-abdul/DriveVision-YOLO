"""YOLO detection subsystem."""
from .detector import YOLODetector
from .types import Detection, DetectionBatch

__all__=["YOLODetector","Detection","DetectionBatch"]
