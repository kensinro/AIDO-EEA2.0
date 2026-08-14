# GitHub / Zenodo release checklist

## Before GitHub release
- [ ] Create repository: `kensinro/AIDO-EEA2.0`
- [ ] Upload all package contents, including `.github/workflows/tests.yml`
- [ ] Confirm GitHub Actions passes
- [ ] Confirm no `__pycache__`, `.pyc`, private corpus, or private prediction ledger is present
- [ ] Confirm `config/frozen_hashes.json` is unchanged
- [ ] Review `provenance/CODE_LINEAGE.csv`

## License gate
- [ ] Select final public software license
- [ ] Replace `LICENSE_PENDING.md` with `LICENSE`
- [ ] Update `.zenodo.json`
- [ ] Update `CITATION.cff`

## GitHub release
Suggested first tag: `v0.1.0`
Suggested release title:
`EEA Semantic Adapter Reference v0.1.0 — Exp1 Frozen Reproducibility Release`

## Zenodo
- [ ] Enable the GitHub repository in Zenodo
- [ ] Publish the GitHub release
- [ ] Verify Zenodo metadata, archive contents, version, and creator
- [ ] Record the resulting DOI in the manuscript and repository About section
