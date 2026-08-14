# AIDO-EEA 2.0 Exp1 — Flat Canonical Prompt Stability Report

## Executive result

- Frozen cases: **97**
- Stable 3/3: **75/97 = 77.3%**
- Unstable 2/3: **22/97 = 22.7%**
- High-instability (3 different): **0/97 = 0.0%**
- Empirical case-level instability / noise floor: **22.7%**
- Mean pairwise agreement: **84.9%**

### Pairwise agreement
- Run01 vs Run02: **78/97 = 80.4%**
- Run01 vs Run03: **80/97 = 82.5%**
- Run02 vs Run03: **89/97 = 91.8%**

## Unstable cases

- `HD-G0033`: DESCRIPTIVE / GENERALIZATION / GENERALIZATION → majority `GENERALIZATION`
- `HD-G0060`: UTILITY / UTILITY / DESCRIPTIVE → majority `UTILITY`
- `HD-G0065`: DESCRIPTIVE / MECHANISTIC / DESCRIPTIVE → majority `DESCRIPTIVE`
- `HD-G0075`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0080`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0081`: ASSOCIATIVE / ASSOCIATIVE / DESCRIPTIVE → majority `ASSOCIATIVE`
- `HD-G0083`: DESCRIPTIVE / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0096`: DESCRIPTIVE / GENERALIZATION / DESCRIPTIVE → majority `DESCRIPTIVE`
- `HD-G0100`: COMPARATIVE / ASSOCIATIVE / ASSOCIATIVE → majority `ASSOCIATIVE`
- `HD-G0102`: DESCRIPTIVE / UTILITY / UTILITY → majority `UTILITY`
- `HD-G0103`: DESCRIPTIVE / UTILITY / UTILITY → majority `UTILITY`
- `HD-G0109`: DESCRIPTIVE / UTILITY / UTILITY → majority `UTILITY`
- `HD-G0113`: DESCRIPTIVE / UTILITY / DESCRIPTIVE → majority `DESCRIPTIVE`
- `HD-G0145`: DESCRIPTIVE / DESCRIPTIVE / UTILITY → majority `DESCRIPTIVE`
- `HD-G0148`: DESCRIPTIVE / UTILITY / DESCRIPTIVE → majority `DESCRIPTIVE`
- `HD-G0151`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0152`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0153`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `HD-G0154`: CAUSAL / MECHANISTIC / MECHANISTIC → majority `MECHANISTIC`
- `V08-R4-B1`: CAUSAL / MECHANISTIC / CAUSAL → majority `CAUSAL`
- `V08-R4-B2`: DESCRIPTIVE / UTILITY / UTILITY → majority `UTILITY`
- `V08-R4-D1-2`: DESCRIPTIVE / __ABSTAIN__ / __ABSTAIN__ → majority `__ABSTAIN__`

## Interpretation

Stable 3/3 cases are repeatable measurements under the frozen flat canonical prompt.
2/3 cases are measurement instability unless independent contract review demonstrates a stable semantic-rule failure.
3-different cases, if any, are high-instability and must not drive a repair rule from this evidence alone.

Per the frozen stopping rule, single-run stochastic flips do not authorize new semantic repairs.