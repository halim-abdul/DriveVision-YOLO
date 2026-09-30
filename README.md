# DriveVision-YOLO

**An end-to-end YOLO-based computer vision framework for autonomous driving, combining real-time object detection, tracking, lane perception, traffic-sign recognition, depth estimation, and driving-scene analytics.**

DriveVision-YOLO is a modular research and portfolio project for studying modern autonomous-driving perception. The repository is intentionally split into replaceable perception layers so experiments can compare models without rewriting the full pipeline.

## Core capabilities

- **YOLO object detection** — road users, vehicles, pedestrians, cyclists, traffic lights and signs; configurable confidence/IoU, ROI filtering, calibration analysis and ONNX export.
- **Multi-object tracking** — IoU association, Kalman motion model, trajectory history, occlusion heuristics, ReID extension point, line crossing, occupancy, speed and TTC helpers.
- **Lane & drivable-area perception** — color/edge CV baseline, bird's-eye transform, sliding-window polynomial fitting, curvature, lateral offset, temporal smoothing, segmentation-model adapter and departure heuristics.
- **Traffic-sign + depth fusion** — sign taxonomy and temporal voting, monocular depth adapter, robust box-distance estimates, uncertainty, camera intrinsics, 3D back-projection and sparse point clouds.
- **Driving-scene analytics** — unified scene records, density, proximity, ego-lane objects, headway, intersection flows, event logging, heatmaps, anomaly detection and trip summaries.
- **Research/MLOps layer** — Python packaging, Docker, CI, pre-commit, model/dataset registries, experiment metadata, runtime monitoring and benchmark protocols.

## Repository layout

```text
src/drivevision/
  detection/      # YOLO inference and evaluation utilities
  tracking/       # MOT, trajectories, TTC, speed
  lanes/          # lane/drivable-area perception
  fusion/         # signs, depth, geometry and distance fusion
  analytics/      # scene understanding and event analytics
configs/          # reproducible module profiles
scripts/          # runtime and benchmark entry points
tests/            # unit tests by subsystem
benchmarks/       # evaluation protocols
docs/             # architecture, datasets and reproducibility
notebooks/        # experiment plans / notebook companions
.github/workflows # CI
```

## Quick start

```bash
git clone https://github.com/halim-abdul/DriveVision-YOLO.git
cd DriveVision-YOLO
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e . -r requirements-dev.txt
pytest -q
python -m drivevision.cli doctor
```

## Example experiments

```bash
python scripts/detect_video.py path/to/video.mp4 --out runs/detect.mp4
python scripts/benchmark_detector.py path/to/video.mp4 --frames 200
python scripts/lane_video.py path/to/video.mp4
python scripts/analyze_events.py runs/events.jsonl
python scripts/run_benchmarks.py
```

Model weights and public datasets are **not** committed. Configure local data/weights according to the experiment documentation.

## Evaluation philosophy

A single mAP or FPS number is not enough for autonomous-driving research. DriveVision encourages per-class detection metrics, calibration, MOT identity metrics, lane IoU/geometric error, depth error by range, sign macro-F1, event false-alert rates, latency percentiles and qualitative failure analysis across weather, illumination and occlusion conditions.

## Reproducibility

For every experiment record the git SHA, dataset/version and split, model checksum, random seed, hardware, Python/PyTorch/CUDA/Ultralytics versions, input resolution, thresholds, precision mode and evaluation script. See `docs/reproducibility.md` and the files under `benchmarks/`.

## Safety and scope

This is a **research prototype**, not a certified autonomous-driving or ADAS product. It must not be used as the sole perception or vehicle-control source on public roads. Metric depth, speed, TTC and lane-offset estimates require appropriate camera calibration and independent validation.

## License

MIT — see `LICENSE`.
