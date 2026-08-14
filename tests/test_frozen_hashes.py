import json
from pathlib import Path

def test_frozen_hash_contract_present():
    root = Path(__file__).resolve().parents[1]
    obj = json.loads((root/"config"/"frozen_hashes.json").read_text(encoding="utf-8"))
    text = json.dumps(obj)
    assert "395657f51ffe53058633941f546558eab7f28bbcd22dc5658c543389ddcc5619" in text
    assert "2cd00cdd2e951bdc81dcdd81f50f608beb82132e4f5fbdef258247a721cc86bb" in text
