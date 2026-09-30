import csv

def write_rows(path,rows):
    rows=list(rows)
    if not rows:return
    with open(path,"w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()));writer.writeheader();writer.writerows(rows)
