from drivevision.tracking.ttc import ttc_from_distance,risk_level

def test_ttc(): assert ttc_from_distance(20,10)==2.0
def test_non_closing(): assert ttc_from_distance(20,0)==float("inf")
def test_risk(): assert risk_level(1.0)=="critical"
