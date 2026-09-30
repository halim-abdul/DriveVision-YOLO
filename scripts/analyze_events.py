import argparse,json
from collections import Counter

p=argparse.ArgumentParser();p.add_argument("jsonl");a=p.parse_args()
events=[json.loads(line) for line in open(a.jsonl,encoding="utf-8") if line.strip()]
print("events",len(events))
print("types",Counter(e.get("event_type","unknown") for e in events))
print("severity",Counter(e.get("severity","unknown") for e in events))
