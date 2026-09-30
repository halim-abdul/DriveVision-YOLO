# Detection Benchmark Protocol

Use fixed seeds and immutable validation splits. Warm up GPU inference before timing. Report hardware, CUDA/PyTorch/Ultralytics versions, image size, batch size and precision mode. Record mean, p50, p95 and p99 latency and exclude data-loading time unless explicitly stated.

Recommended datasets: BDD100K, KITTI, Cityscapes-compatible scenes and an explicitly documented internal sample set. Never mix validation and test frames during tuning.
