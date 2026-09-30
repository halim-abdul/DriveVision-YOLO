from drivevision.lanes.offset import lateral_offset_m

def test_centered_vehicle():
    value = lateral_offset_m(200, 600, 800)
    assert abs(value) < 1e-12
