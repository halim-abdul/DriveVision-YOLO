from drivevision.analytics.risk import aggregate_risk,risk_score

def test_aggregate():
    assert aggregate_risk(["normal","warning","attention"])=="warning"
    assert risk_score(["normal","critical"])==3
