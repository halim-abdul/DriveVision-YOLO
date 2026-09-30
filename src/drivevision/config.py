from pathlib import Path
import yaml

def load_yaml(path):
    with Path(path).open("r",encoding="utf-8") as f:return yaml.safe_load(f) or {}

def deep_update(base,override):
    out=dict(base)
    for k,v in override.items():
        if isinstance(v,dict) and isinstance(out.get(k),dict):out[k]=deep_update(out[k],v)
        else:out[k]=v
    return out
