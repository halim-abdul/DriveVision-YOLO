# Multi-Object Tracking

The tracking layer turns frame-local detections into persistent road-user identities. It includes IoU association, constant-velocity filtering, trajectory history, line crossing, occupancy, speed estimation, TTC helpers, occlusion scoring and a ReID extension point.

Evaluate with HOTA/IDF1/MOTA-style metrics, identity switches and track fragmentation. Treat pixel-to-meter speed estimates as uncalibrated unless camera geometry is explicitly measured.
