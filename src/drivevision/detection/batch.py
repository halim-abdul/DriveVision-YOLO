from pathlib import Path
import cv2

def image_paths(root):
    root = Path(root)
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp"):
        yield from sorted(root.rglob(ext))

def load_images(root):
    for path in image_paths(root):
        image = cv2.imread(str(path))
        if image is not None:
            yield path, image
