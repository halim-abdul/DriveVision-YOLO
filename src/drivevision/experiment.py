from dataclasses import dataclass,asdict
from datetime import datetime,timezone
import json
from pathlib import Path

@dataclass
class Experiment:
    name:str
    config:dict
    metrics:dict
    git_sha:str|None=None
    created_at:str=""
    def save(self,path):
        self.created_at=self.created_at or datetime.now(timezone.utc).isoformat()
        p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(asdict(self),indent=2))
