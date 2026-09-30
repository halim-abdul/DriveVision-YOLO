# Lane Perception

DriveVision supports a classical lane pipeline and a learned-segmentation extension point. The classical path combines color thresholds, edge extraction, perspective warping, sliding windows, polynomial fitting, temporal smoothing, curvature, lateral offset and departure heuristics.

Pixel-to-meter quantities depend on calibration and road geometry. Do not interpret default scaling constants as universal real-world measurements.
