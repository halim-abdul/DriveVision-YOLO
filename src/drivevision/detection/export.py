def export_model(weights, fmt="onnx", imgsz=640, half=False, dynamic=True):
    from ultralytics import YOLO
    model = YOLO(weights)
    return model.export(format=fmt, imgsz=imgsz, half=half, dynamic=dynamic)
