# Data exclusions

The public-ready package intentionally excludes:
- the frozen 97-case raw input corpus;
- prediction JSONL files containing the original atomic-claim text;
- case ledgers containing source-derived claim text;
- source passages/PDFs.

Reason: redistribution rights for source-derived scientific text should be confirmed before public release.

The frozen input SHA256 is retained in `config/frozen_hashes.json` so a private/local corpus can be integrity-checked against the Exp1 archive.

If redistribution is confirmed, add the corpus in a separate `data/` release and document its provenance/license explicitly.
