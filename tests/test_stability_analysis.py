from pathlib import Path
from stability_analysis import analyze

def test_synthetic_stability_summary():
    root = Path(__file__).resolve().parents[1]
    paths = [root / "examples" / f"synthetic_run_0{i}_predictions.jsonl" for i in (1,2,3)]
    summary, ledger = analyze(paths)
    assert summary["n_cases"] == 3
    assert summary["n_runs"] == 3
    assert summary["unanimous_cases"] == 2
    assert summary["majority_nonunanimous_cases"] == 1
    assert summary["no_majority_cases"] == 0
    assert len(ledger) == 3
