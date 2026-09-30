from drivevision.fusion.camera import CameraIntrinsics
from drivevision.fusion.backproject import backproject

def test_optical_center():
    k=CameraIntrinsics(100,100,50,40)
    assert backproject(50,40,10,k)==(0.0,0.0,10)
