import json
from dataclasses import asdict,is_dataclass

class EventLogger:
    def __init__(self,path):self.path=path
    def append(self,event):
        payload=asdict(event) if is_dataclass(event) else event
        with open(self.path,"a",encoding="utf-8") as f:f.write(json.dumps(payload)+"\n")
