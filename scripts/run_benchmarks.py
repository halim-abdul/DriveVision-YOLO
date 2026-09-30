from pathlib import Path

PROTOCOLS=["benchmarks/detection_protocol.md","benchmarks/tracking_protocol.md","benchmarks/lane_protocol.md","benchmarks/depth_protocol.md","benchmarks/sign_protocol.md","benchmarks/analytics_protocol.md"]

if __name__=="__main__":
    for item in PROTOCOLS:
        print(("FOUND" if Path(item).exists() else "MISSING"),item)
