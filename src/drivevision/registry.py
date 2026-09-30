import json
from pathlib import Path

class ModelRegistry:
    def __init__(self,path="artifacts/registry.json"):
        self.path=Path(path)
    def load(self):
        return json.loads(self.path.read_text()) if self.path.exists() else {}
    def register(self,name,metadata):
        data=self.load();data[name]=metadata;self.path.parent.mkdir(parents=True,exist_ok=True);self.path.write_text(json.dumps(data,indent=2));return metadata
