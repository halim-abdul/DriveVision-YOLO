class LaneSegmentationAdapter:
    """Adapter for learned lane/drivable-area segmentation models."""
    def __init__(self,model=None): self.model=model
    def predict(self,image):
        if self.model is None: raise RuntimeError("segmentation model is not loaded")
        return self.model(image)
