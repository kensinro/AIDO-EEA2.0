from __future__ import annotations
import argparse, json
from pathlib import Path
from common import sha256_file

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", required=True)
    args=ap.parse_args()
    root=Path(args.root)
    out_path=Path(args.out).resolve()
    records=[]
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.resolve()!=out_path:
            records.append({
                "path": str(p.relative_to(root)).replace("\\","/"),
                "bytes": p.stat().st_size,
                "sha256": sha256_file(p)
            })
    Path(args.out).write_text(json.dumps({"files":records},indent=2),encoding="utf-8")
    print(args.out)

if __name__=="__main__":
    main()
