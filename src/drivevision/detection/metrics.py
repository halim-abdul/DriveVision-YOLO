def precision(tp, fp): return tp / max(tp + fp, 1)
def recall(tp, fn): return tp / max(tp + fn, 1)
def f1(tp, fp, fn):
    p, r = precision(tp, fp), recall(tp, fn)
    return 2 * p * r / max(p + r, 1e-12)

def latency_summary(values):
    if not values: return {"mean_ms": 0.0, "fps": 0.0}
    mean = sum(values) / len(values)
    return {"mean_ms": mean, "fps": 1000.0 / max(mean, 1e-9)}
