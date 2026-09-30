import json

def track_to_dict(t):
    return {"track_id":t.track_id,"xyxy":list(t.xyxy),"class_name":t.class_name,"confidence":t.confidence,"age":t.age,"missed":t.missed,"history":[list(p) for p in t.history]}

def write_jsonl(path,frames):
    with open(path,"w",encoding="utf-8") as f:
        for frame in frames:f.write(json.dumps(frame)+"\n")
