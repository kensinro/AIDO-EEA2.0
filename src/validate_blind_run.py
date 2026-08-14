from __future__ import annotations
import argparse, json
from pathlib import Path
from common import read_jsonl, sha256_file

REQUIRED_PREDICTION_FIELDS = [
    "run_id",
    "prompt_version",
    "input_id",
    "passage_id",
    "candidate_atomic_claim",
    "candidate_type",
    "decision_state",
    "adapter_confidence",
]

def validate(input_path: Path, predictions_path: Path, execution_record_path: Path,
             expected_prompt_sha: str | None = None) -> dict:
    inputs = read_jsonl(input_path)
    predictions = read_jsonl(predictions_path)
    record = json.loads(execution_record_path.read_text(encoding="utf-8"))

    by_input = {r["input_id"]: r for r in inputs}
    schema_errors = []
    identity_errors = []

    for idx, pred in enumerate(predictions, 1):
        missing = [k for k in REQUIRED_PREDICTION_FIELDS if k not in pred]
        if missing:
            schema_errors.append({"row": idx, "missing": missing})
            continue
        src = by_input.get(pred["input_id"])
        if src is None:
            identity_errors.append({"row": idx, "input_id": pred["input_id"], "reason": "unknown input_id"})
            continue
        # Supports either atomic_claim or candidate_atomic_claim in input corpus.
        src_claim = src.get("atomic_claim", src.get("candidate_atomic_claim"))
        if pred["passage_id"] != src.get("passage_id") or pred["candidate_atomic_claim"] != src_claim:
            identity_errors.append({"row": idx, "input_id": pred["input_id"], "reason": "passage/claim identity mismatch"})

    pred_sha = sha256_file(predictions_path)
    input_sha = sha256_file(input_path)

    report = {
        "stage": "R0_RAW_OUTPUT_INTEGRITY",
        "prediction_rows": len(predictions),
        "input_rows": len(inputs),
        "unique_prediction_input_ids": len({r.get("input_id") for r in predictions}),
        "schema_errors": schema_errors,
        "identity_errors": identity_errors,
        "prediction_sha256_actual": pred_sha,
        "prediction_sha256_execution_record": record.get("prediction_sha256"),
        "prediction_hash_match": pred_sha == record.get("prediction_sha256"),
        "input_sha256_actual": input_sha,
        "input_sha256_execution_record": record.get("input_sha256"),
        "input_hash_match": input_sha == record.get("input_sha256"),
        "canonical_prompt_sha256_record": record.get("canonical_prompt_sha256") or record.get("implementation_prompt_sha256"),
        "expected_prompt_sha256": expected_prompt_sha,
        "prompt_hash_match": True if expected_prompt_sha is None else (
            (record.get("canonical_prompt_sha256") or record.get("implementation_prompt_sha256")) == expected_prompt_sha
        ),
        "memory_or_project_context_access": record.get("memory_or_project_context_access"),
        "gold_access": record.get("gold_access"),
        "scoring_access": record.get("scoring_access"),
        "prior_prediction_access": record.get("prior_prediction_access"),
        "status": record.get("status"),
    }

    report["pass"] = (
        len(predictions) == len(inputs)
        and len({r.get("input_id") for r in predictions}) == len(inputs)
        and not schema_errors
        and not identity_errors
        and report["prediction_hash_match"]
        and report["input_hash_match"]
        and report["prompt_hash_match"]
        and record.get("memory_or_project_context_access") is False
        and record.get("gold_access") is False
        and record.get("scoring_access") is False
        and record.get("status") == "COMPLETED"
    )
    return report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--predictions", required=True)
    ap.add_argument("--execution-record", required=True)
    ap.add_argument("--expected-prompt-sha")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    report = validate(Path(args.input), Path(args.predictions), Path(args.execution_record), args.expected_prompt_sha)
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print("PASS" if report["pass"] else "FAIL")
    print(args.out)

if __name__ == "__main__":
    main()
