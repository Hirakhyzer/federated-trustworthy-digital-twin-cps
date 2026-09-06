from __future__ import annotations
import csv, json
from pathlib import Path

def write_json(data, path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(data,indent=2),encoding="utf-8")

def write_csv(rows, path, fields=None):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    if not rows: return
    fields=fields or [k for k,v in rows[0].items() if not isinstance(v,(dict,list))]
    with p.open("w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=fields); wr.writeheader()
        for row in rows: wr.writerow({k:row.get(k) for k in fields})
