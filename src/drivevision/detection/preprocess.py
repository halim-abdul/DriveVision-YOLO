import cv2
import numpy as np

def letterbox(image: np.ndarray, size: int = 640, pad_value: int = 114):
    h, w = image.shape[:2]
    scale = min(size / w, size / h)
    nw, nh = int(round(w * scale)), int(round(h * scale))
    resized = cv2.resize(image, (nw, nh), interpolation=cv2.INTER_LINEAR)
    canvas = np.full((size, size, 3), pad_value, dtype=image.dtype)
    x, y = (size - nw) // 2, (size - nh) // 2
    canvas[y:y + nh, x:x + nw] = resized
    return canvas, scale, (x, y)

def normalize_rgb(image: np.ndarray):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype("float32") / 255.0
