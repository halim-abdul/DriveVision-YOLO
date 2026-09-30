from drivevision.fusion.risk import distance_risk

def test_distance_bands():
    assert distance_risk(4)=="near"
    assert distance_risk(12)=="caution"
    assert distance_risk(30)=="far"
