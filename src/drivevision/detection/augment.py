import cv2
import random

def photometric(image, brightness=.15, contrast=.15):
    alpha = 1 + random.uniform(-contrast, contrast)
    beta = 255 * random.uniform(-brightness, brightness)
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def horizontal_flip(image, boxes):
    out = cv2.flip(image, 1)
    w = image.shape[1]
    flipped = [(w-x2, y1, w-x1, y2) for x1, y1, x2, y2 in boxes]
    return out, flipped
