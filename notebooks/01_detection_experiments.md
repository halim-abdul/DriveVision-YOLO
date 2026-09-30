# Detection experiment notebook outline

1. Load a BDD100K/KITTI-compatible sample.
2. Compare YOLO model sizes at 640 and 960 px.
3. Plot class frequency and confidence distributions.
4. Measure AP by object scale and illumination.
5. Inspect false positives for traffic lights and small pedestrians.
6. Export ONNX and compare latency.

This markdown companion keeps the experiment protocol reproducible when notebook outputs are stripped from git.
