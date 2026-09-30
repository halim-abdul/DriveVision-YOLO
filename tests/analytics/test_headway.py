from drivevision.analytics.headway import time_headway,headway_state

def test_headway():
    assert time_headway(20,10)==2.0
    assert headway_state(.8)=="critical"
    assert headway_state(1.5)=="warning"
