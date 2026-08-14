# AIDO-EEA 2.0 Exp1 — Final Stability Validation Report

## Final verdict

> **ELIGIBLE FOR EXP1 FINAL DEVELOPMENT FREEZE**

This closes the current semantic-adapter development/calibration experiment. It does **not** claim a deterministic, production-grade, or generally externally validated classifier.

## Canonicalized instrument

- Flat canonical prompt SHA256: `395657f51ffe53058633941f546558eab7f28bbcd22dc5658c543389ddcc5619`
- Frozen 97-case input SHA256: `2cd00cdd2e951bdc81dcdd81f50f608beb82132e4f5fbdef258247a721cc86bb`
- Previous nested-prompt lineage removed.
- Three independent blind runs used the same prompt and input.

## Repeatability

- 3/3 stable: **75/97 = 77.3%**
- 2/3 unstable: **22/97 = 22.7%**
- Three different labels: **0/97**
- Mean pairwise agreement: **84.9%**

The observed **22.7% case-level instability** is retained as the empirical measurement-instability estimate for this development corpus.

## Repair-driving validation

All repair-driving cases that were **3/3 stable** showed the intended repaired behavior:

- `HD-G0034` → DESCRIPTIVE — 3/3
- `HD-G0046` → UNCERTAIN_OTHER — 3/3
- `HD-G0071` → GENERALIZATION — 3/3
- `HD-G0086` → GENERALIZATION — 3/3
- `HD-G0088` → GENERALIZATION — 3/3
- `V08-R4-A2` → UTILITY — 3/3

`HD-G0065` remained unstable:
DESCRIPTIVE / MECHANISTIC / DESCRIPTIVE.
It is therefore recorded as **MEASUREMENT_INSTABILITY**, not as evidence for another semantic repair.

## R4 boundary validation

All **3/3-stable** R4 challenge cases matched the intended boundary behavior.

The remaining non-matching challenge behavior occurred only in unstable cases:
- `V08-R4-B1` — CAUSAL / MECHANISTIC / CAUSAL
- `V08-R4-D1-2` — DESCRIPTIVE / ABSTAIN / ABSTAIN

These do not authorize further tuning under the frozen stopping rule.

## Governance debt

Known Frozen-Gold/Contract conflicts and ontology/boundary governance cases remain append-only governance records. They are not silently converted into adapter errors and Gold remains unchanged.

Stable legacy-Gold mismatches such as `HD-G0139` and `HD-G0094` remain within their previously adjudicated Gold/Contract-conflict category, not unexplained new regressions.

## Stopping rule

No new semantic repair is authorized from:
- a single-run label flip;
- a 2/3 disagreement;
- a previously adjudicated Gold/Contract conflict;
- an ontology/boundary governance quarantine.

Only a new **3/3-stable, systematic, contract-supported failure pattern** would justify reopening Exp1.

No such new pattern is present in the final stability assessment.

## Scope boundary

This freeze supports:
- a frozen semantic rule set;
- a canonical non-nested prompt;
- an empirical repeatability estimate;
- a frozen regression/stability corpus;
- known failure and governance boundaries.

It does not support claims of:
- deterministic behavior;
- zero-error claim typing;
- production readiness;
- general external operating characteristics.

Future semantic-adapter improvement must proceed as a new experiment / external validation phase rather than further tuning against this frozen 97-case corpus.
