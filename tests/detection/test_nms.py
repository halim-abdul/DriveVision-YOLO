from drivevision.detection.nms import iou

def test_iou_identity():
    assert abs(iou((0,0,10,10), (0,0,10,10)) - 1) < 1e-9

def test_iou_disjoint():
    assert iou((0,0,1,1), (2,2,3,3)) == 0
