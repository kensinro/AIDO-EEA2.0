from __future__ import annotations
import argparse, json
from pathlib import Path
import matplotlib.pyplot as plt

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--summary", required=True)
    ap.add_argument("--out", required=True)
    args=ap.parse_args()
    s=json.loads(Path(args.summary).read_text(encoding="utf-8"))
    n=s["n_cases"]
    vals=[s["unanimous_cases"], s["majority_nonunanimous_cases"], s["no_majority_cases"]]
    labels=["Unanimous","Majority non-unanimous","No majority"]
    fig,ax=plt.subplots(figsize=(7,4.6))
    bars=ax.bar(labels,vals)
    ax.set_ylabel(f"Cases (n={n})")
    ax.set_title("Repeated blind semantic-classification stability")
    for b,v in zip(bars,vals):
        ax.text(b.get_x()+b.get_width()/2, v + max(0.5,n*0.01), str(v), ha="center", va="bottom")
    ax.set_ylim(0,max(vals+[1])*1.15)
    fig.tight_layout()
    fig.savefig(args.out,dpi=220,bbox_inches="tight")
    print(args.out)

if __name__=="__main__":
    main()
