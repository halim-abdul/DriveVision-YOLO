import argparse
import cv2
from drivevision.fusion.signs import TrafficSignRecognizer

p=argparse.ArgumentParser();p.add_argument("image");a=p.parse_args()
image=cv2.imread(a.image)
if image is None: raise SystemExit("image not found")
recognizer=TrafficSignRecognizer()
print("Attach a trained sign model to recognizer.model before inference.")
