from pathlib import Path

def yolo_label_path(image_path):
    p = Path(image_path)
    return p.parent.parent / "labels" / p.parent.name / (p.stem + ".txt")

def parse_yolo_labels(path):
    path = Path(path)
    rows = []
    if not path.exists(): return rows
    for line in path.read_text().splitlines():
        cid, x, y, w, h = line.split()
        rows.append((int(cid), float(x), float(y), float(w), float(h)))
    return rows
