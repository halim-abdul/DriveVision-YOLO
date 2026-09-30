from drivevision.lanes.departure import departure_state

def test_states():
    assert departure_state(0.1) == "centered"
    assert departure_state(0.4) == "warning"
    assert departure_state(0.8) == "critical"
