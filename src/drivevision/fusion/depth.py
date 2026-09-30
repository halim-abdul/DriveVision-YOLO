import numpy as np

class DepthEstimator:
    """Pluggable monocular-depth adapter with normalized metric conversion hooks."""
    def __init__(self, model=None, scale=1.0):
        self.model = model
        self.scale = scale
    def predict(self, image):
        if self.model is None:
            raise RuntimeError("depth model is not loaded")
        depth = self.model(image)
        return np.asarray(depth, dtype="float32") * self.scale
