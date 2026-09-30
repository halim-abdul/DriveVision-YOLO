from time import perf_counter
from .config import DetectorConfig
from .types import Detection, DetectionBatch

class YOLODetector:
    """Thin Ultralytics adapter that exposes stable project-facing outputs."""
    def __init__(self, config: DetectorConfig | None = None):
        self.config = config or DetectorConfig()
        self.model = None

    def load(self):
        from ultralytics import YOLO
        self.model = YOLO(self.config.weights)
        return self

    def predict(self, frame, frame_id: int = 0) -> DetectionBatch:
        if self.model is None:
            self.load()
        t0 = perf_counter()
        result = self.model.predict(
            frame,
            conf=self.config.confidence,
            iou=self.config.iou,
            imgsz=self.config.imgsz,
            device=self.config.device,
            half=self.config.half,
            max_det=self.config.max_det,
            verbose=False,
        )[0]
        detections = []
        if result.boxes is not None:
            for box in result.boxes:
                cid = int(box.cls.item())
                detections.append(
                    Detection(
                        tuple(float(x) for x in box.xyxy[0].tolist()),
                        float(box.conf.item()),
                        cid,
                        str(result.names[cid]),
                    )
                )
        return DetectionBatch(frame_id, detections, (perf_counter() - t0) * 1000.0)
