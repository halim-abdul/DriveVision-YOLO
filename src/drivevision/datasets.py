from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DatasetSpec:
    name:str
    root:Path
    split:str
    version:str="local"

def validate_dataset(spec):
    return {"name":spec.name,"exists":spec.root.exists(),"split":spec.split,"version":spec.version}
