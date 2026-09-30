class TrafficSignRecognizer:
    def __init__(self, model=None, threshold=0.4):
        self.model = model
        self.threshold = threshold
    def predict(self, crop):
        if self.model is None:
            raise RuntimeError("traffic-sign model is not loaded")
        return self.model(crop)
