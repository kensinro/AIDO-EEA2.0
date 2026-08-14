from __future__ import annotations
import argparse, json
from pathlib import Path
from collections import Counter
from common import read_jsonl, normalized_label, write_jsonl

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--predictions", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args=ap.parse_args()

    runs=[read_jsonl(p) for p in args.predictions]
    bys=[{r["input_id"]:r for r in run} for run in runs]
    ids=set.intersection(*(set(b) for b in bys))
    out=[]
    for cid in sorted(ids):
        labels=[normalized_label(b[cid]) for b in bys]
        consensus,count=Counter(labels).most_common(1)[0]
        # choose first row with consensus label
        source=None
        for b in bys:
            if normalized_label(b[cid])==consensus:
                source=dict(b[cid]); break
        source["run_id"]="STABILITY_CONSENSUS"
        source["stability_consensus_count"]=count
        source["stability_total_runs"]=len(runs)
        source["stability_unanimous"]=(count==len(runs))
        out.append(source)
    write_jsonl(args.out,out)
    print(args.out)

if __name__=="__main__":
    main()
