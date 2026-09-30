import argparse
import cv2
from drivevision.fusion.depth import DepthEstimator

p=argparse.ArgumentParser();p.add_argument("source");a=p.parse_args()
cap=cv2.VideoCapture(a.source);estimator=DepthEstimator()
while cap.isOpened():
    ok,frame=cap.read()
    if not ok:break
    # Load a depth model before runtime: estimator.model = ...
    cv2.imshow("DriveVision depth input",frame)
    if cv2.waitKey(1)&0xFF==27:break
cap.release();cv2.destroyAllWindows()
