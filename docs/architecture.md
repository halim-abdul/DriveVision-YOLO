# Architecture

The framework is organized as six research layers: YOLO detection, multi-object tracking, lane/drivable-area perception, traffic-sign + depth fusion, scene analytics, and production tooling. Modules communicate through small typed records rather than model-specific outputs, making detector, tracker and depth implementations replaceable.

A full runtime processes frames in this order: ingest -> detection -> tracking -> lane perception -> depth/sign fusion -> scene state -> analytics/events -> visualization/export. Offline evaluation uses the same intermediate records where possible.
