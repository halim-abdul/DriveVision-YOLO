import numpy as np

def expected_calibration_error(confidences, correct, bins=10):
    c = np.asarray(confidences, dtype=float)
    y = np.asarray(correct, dtype=float)
    if len(c) == 0: return 0.0
    edges = np.linspace(0, 1, bins + 1)
    ece = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (c >= lo) & (c < (hi if hi < 1 else hi + 1e-12))
        if mask.any():
            ece += mask.mean() * abs(c[mask].mean() - y[mask].mean())
    return float(ece)
