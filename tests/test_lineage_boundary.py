import csv
from pathlib import Path

def test_no_ait_scientific_engine_is_marked_as_copied():
    root = Path(__file__).resolve().parents[1]
    with (root/"provenance"/"CODE_LINEAGE.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ait_rows = [r for r in rows if "AIT" in r["origin"]]
    assert ait_rows
    assert all(r["copied_code"].lower().startswith("no") for r in ait_rows)
    assert all(r["modifies_entitlement_semantics"].lower() == "no" for r in ait_rows)
