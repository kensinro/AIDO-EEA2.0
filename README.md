# Evidence Entitlement Audit — Semantic Adapter Reference Implementation

**Release candidate:** v0.1.0-rc  
**Scientific stage:** EEA2 Exp1 final development freeze / manuscript integration  
**Repository target:** https://github.com/kensinro/AIDO-EEA2.0

This package provides the public-safe reference implementation and
reproducibility artifacts for the supervised semantic-adapter experiment
surrounding the Evidence Entitlement Audit (EEA) kernel.

## Architecture boundary

The package is **not a replacement entitlement engine**.

- The canonical EEA five-state semantics and Rmin/Rfull evidence contracts are inherited from the EEA kernel.
- The semantic adapter produces provisional claim/evidence objects.
- Final scientific entitlement remains human-governed.
- AIT-derived or AIT-inspired utilities are limited to provenance, regression, freeze, and release governance.

The compatible upstream kernel is:
https://github.com/kensinro/AIDO-EEA1.0

Kernel code is not vendored into this repository.

## Exp1 frozen repeatability result

Under the flat canonical prompt and frozen 97-case development/stability universe:

- 75/97 cases were 3/3 unanimous (**77.3%**);
- 22/97 retained a 2/3 majority (**22.7% three-run case-level non-unanimity**);
- 0/97 produced a three-way split;
- mean pairwise agreement was approximately **84.9%**.

These figures characterize the frozen Exp1 development/challenge corpus only.
They are not universal operating characteristics and the 22.7% result must not
be described as a universal noise floor.

## What this public package reproduces

- blind-run integrity checks;
- input/prediction SHA256 verification;
- three-run stability analysis;
- unanimous and majority-non-unanimous accounting;
- pairwise agreement and Fleiss' kappa;
- majority-consensus artifact construction;
- repeatability figure generation;
- release hash-manifest generation.

## Public-data boundary

The frozen 97-case source-derived corpus and prediction ledgers containing
source text are intentionally excluded pending redistribution-rights review.
The frozen corpus SHA256 is retained in `config/frozen_hashes.json`.

## Quick smoke test

```bash
python -m pip install -r requirements.txt
python src/stability_analysis.py --predictions   examples/synthetic_run_01_predictions.jsonl   examples/synthetic_run_02_predictions.jsonl   examples/synthetic_run_03_predictions.jsonl   --summary-out outputs_example/synthetic_stability_summary.json   --ledger-out outputs_example/synthetic_stability_ledger.jsonl

python src/build_consensus.py --predictions   examples/synthetic_run_01_predictions.jsonl   examples/synthetic_run_02_predictions.jsonl   examples/synthetic_run_03_predictions.jsonl   --out outputs_example/synthetic_consensus.jsonl

pytest -q
```

## Repository map

- `src/` — reproducibility and validation utilities
- `tests/` — public synthetic regression tests
- `config/` — prediction schema and frozen hashes
- `frozen_artifacts/` — public-safe Exp1 final locks and reports
- `provenance/` — EEA1 / EEA2 / AIT code-lineage and role maps
- `kernel_interface/` — upstream kernel compatibility declaration
- `governance/` — Human Gate and append-only repair boundaries
- `examples/` — synthetic public smoke-test fixtures
- `docs/` — reproducibility and release notes

## Exp1 freeze boundary

EEA2 Exp1 development/calibration is closed and final-frozen. The 97-case
regression/stability universe must not be reused for additional semantic-rule
tuning. Future development requires new unseen cases or a separately frozen
external-validation corpus.

## License

This software is released under the MIT License. See `LICENSE`.
