from .config import TrackerConfig
from .types import Track
from .assignment import iou_cost, greedy_match
from .geometry import center

class MultiObjectTracker:
    def __init__(self,config=None):
        self.config=config or TrackerConfig(); self.tracks=[]; self._next_id=1
    def update(self,detections):
        pairs=greedy_match(iou_cost(self.tracks,detections),1-self.config.match_iou)
        matched_t={i for i,_ in pairs}; matched_d={j for _,j in pairs}
        for i,j in pairs:
            t,d=self.tracks[i],detections[j]; t.xyxy=d.xyxy; t.confidence=d.confidence; t.class_name=d.class_name; t.age+=1; t.missed=0; t.history.append(center(d.xyxy))
        for i,t in enumerate(self.tracks):
            if i not in matched_t: t.missed+=1
        for j,d in enumerate(detections):
            if j not in matched_d and d.confidence>=self.config.high_conf:
                t=Track(self._next_id,d.xyxy,d.class_name,d.confidence); t.history.append(center(d.xyxy)); self._next_id+=1; self.tracks.append(t)
        self.tracks=[t for t in self.tracks if t.missed<=self.config.max_age]
        return list(self.tracks)
