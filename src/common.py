from __future__ import annotations
from pathlib import Path
import hashlib, json

def sha256_file(path: str | Path) -> str:
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def read_jsonl(path: str | Path) -> list[dict]:
    rows = []
    with Path(path).open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}: invalid JSON on line {lineno}: {e}") from e
    return rows

def write_jsonl(path: str | Path, rows: list[dict]) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def normalized_label(row: dict) -> str:
    candidate_type = row.get("candidate_type")
    if candidate_type not in (None, ""):
        return str(candidate_type)
    state = row.get("decision_state") or "NO_TYPE"
    return f"__{state}__"
