from drivevision.detection.metrics import precision, recall, f1

def test_metrics():
    assert precision(8, 2) == .8
    assert recall(8, 2) == .8
    assert abs(f1(8, 2, 2) - .8) < 1e-9
