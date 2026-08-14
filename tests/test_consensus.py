from pathlib import Path
from collections import Counter
from common import read_jsonl, normalized_label

def test_each_synthetic_case_has_majority():
    root = Path(__file__).resolve().parents[1]
    runs = [read_jsonl(root/"examples"/f"synthetic_run_0{i}_predictions.jsonl") for i in (1,2,3)]
    bys = [{r["input_id"]: r for r in run} for run in runs]
    ids = set.intersection(*(set(b) for b in bys))
    assert len(ids) == 3
    for cid in ids:
        labels = [normalized_label(b[cid]) for b in bys]
        assert Counter(labels).most_common(1)[0][1] >= 2
