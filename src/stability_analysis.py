from __future__ import annotations
import argparse, json, statistics
from pathlib import Path
from collections import Counter
from common import read_jsonl, normalized_label, write_jsonl

def fleiss_kappa(label_matrix: list[list[str]]) -> float:
    """Fleiss' kappa for N subjects, fixed n raters."""
    if not label_matrix:
        return float("nan")
    n = len(label_matrix[0])
    labels = sorted({lab for row in label_matrix for lab in row})
    N = len(label_matrix)
    per_subject_counts = []
    total_counts = Counter()
    for row in label_matrix:
        c = Counter(row)
        per_subject_counts.append(c)
        total_counts.update(row)
    P_i = []
    for c in per_subject_counts:
        s = sum(v * (v - 1) for v in c.values())
        P_i.append(s / (n * (n - 1)))
    P_bar = sum(P_i) / N
    p = {lab: total_counts[lab] / (N * n) for lab in labels}
    P_e = sum(v * v for v in p.values())
    if abs(1 - P_e) < 1e-15:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)

def analyze(paths: list[Path]) -> tuple[dict, list[dict]]:
    runs = [read_jsonl(p) for p in paths]
    bys = [{r["input_id"]: r for r in run} for run in runs]
    common = set.intersection(*(set(b) for b in bys))
    union = set.union(*(set(b) for b in bys))
    if len(common) != len(union):
        raise ValueError("Runs do not contain identical input_id universes.")

    ledger = []
    pair_agree = Counter()
    label_matrix = []
    for cid in sorted(common):
        labs = [normalized_label(b[cid]) for b in bys]
        label_matrix.append(labs)
        c = Counter(labs)
        consensus, count = c.most_common(1)[0]
        if count == len(labs):
            cat = f"STABLE_{len(labs)}_OF_{len(labs)}"
        elif count > len(labs)/2:
            cat = f"UNSTABLE_{count}_OF_{len(labs)}"
        else:
            cat = "NO_MAJORITY"
        for i in range(len(labs)):
            for j in range(i+1, len(labs)):
                if labs[i] == labs[j]:
                    pair_agree[f"{i+1}_{j+1}"] += 1
        ledger.append({
            "input_id": cid,
            **{f"run{i+1:02d}": lab for i,lab in enumerate(labs)},
            "consensus": consensus,
            "consensus_count": count,
            "stability_category": cat,
            "candidate_atomic_claim": bys[0][cid].get("candidate_atomic_claim"),
        })

    N = len(common)
    stable = sum(1 for r in ledger if r["consensus_count"] == len(paths))
    majority_nonunanimous = sum(1 for r in ledger if len(paths)/2 < r["consensus_count"] < len(paths))
    no_majority = N - stable - majority_nonunanimous
    pair_rates = {k:v/N for k,v in pair_agree.items()}
    summary = {
        "n_cases": N,
        "n_runs": len(paths),
        "unanimous_cases": stable,
        "unanimous_rate": stable/N,
        "majority_nonunanimous_cases": majority_nonunanimous,
        "majority_nonunanimous_rate": majority_nonunanimous/N,
        "no_majority_cases": no_majority,
        "no_majority_rate": no_majority/N,
        "pairwise_agreement_counts": dict(pair_agree),
        "pairwise_agreement_rates": pair_rates,
        "mean_pairwise_agreement": statistics.mean(pair_rates.values()) if pair_rates else None,
        "fleiss_kappa": fleiss_kappa(label_matrix),
        "nonunanimous_case_ids": [r["input_id"] for r in ledger if r["consensus_count"] < len(paths)],
    }
    return summary, ledger

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--predictions", nargs="+", required=True)
    ap.add_argument("--summary-out", required=True)
    ap.add_argument("--ledger-out", required=True)
    args=ap.parse_args()
    summary, ledger=analyze([Path(p) for p in args.predictions])
    Path(args.summary_out).write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    write_jsonl(args.ledger_out, ledger)
    print(json.dumps(summary, indent=2))

if __name__=="__main__":
    main()
