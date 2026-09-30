from drivevision.config import deep_update

def test_deep_update():
    base={"a":{"b":1,"c":2}}
    out=deep_update(base,{"a":{"b":9}})
    assert out=={"a":{"b":9,"c":2}}
