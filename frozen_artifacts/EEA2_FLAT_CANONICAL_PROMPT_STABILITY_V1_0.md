# AIDO-EEA 2.0 — Flat Canonical Semantic Adapter Prompt
## Stability Candidate V1.0

### Purpose
Classify each supplied atomic claim using one canonical, non-nested semantic rule set.

### Canonical precedence
1. Final Frozen Prompt Contract V1.0
2. Approved F1–F5 repair constraints
3. Approved M1/M2 negative guards
4. Approved M2A attachment guard
5. Existing frozen ontology and output schema

No previous implementation prompt is embedded.
No case ID is a rule.
No Gold, scoring, prior prediction, article context, or external context may be inferred or used.

---

# I. FINAL FROZEN PROMPT CONTRACT V1.0

# AIDO-EEA 2.0 V0.8 Prompt Contract V1.0 — FINAL FREEZE

**Status:** FINAL FROZEN  
**Contract version:** V1.0  
**Authorized repair domains:** A / B / C / D1 / D2

## Frozen governance boundary
V0.8 MUST NOT modify V0.7.3 baseline, Pilot-25 Gold, H4 Frozen Gold, H4 source passages,
atomic decomposition, claim scope, causal-safety constraints, or O-03 ontology definition.

## Core semantic-head principle
Classify by the proposition principally asserted by the supplied atomic claim.
Do not classify solely from isolated keywords, biological-token density, modal verbs,
method vocabulary, comparison adjectives, uncertainty words, or entity names.

## Semantic-head tie-break
When two semantic heads remain plausible, identify which candidate relation is structurally
necessary for the core assertion to remain intact. This is interpretive only and MUST NOT
alter the atomic claim.

## Causal safety
Do not strengthen:
- associated with -> causes
- linked to -> drives
- may regulate -> regulates
- consistent with -> demonstrates
- could contribute to -> mediates

## A — UTILITY
UTILITY applies when the principal proposition concerns capability, applicability,
usefulness, limitation, or functional role of a method/tool/model/assay/score/measure/procedure.
Positive and negative capability are included.
Biological targets do not by themselves make a method claim MECHANISTIC.
If instantiated comparators are explicitly contrasted on a shared dimension, evaluate COMPARATIVE.
Words such as used to/enables/allows/useful/applicable/supports are not hard triggers.

## B — MECHANISTIC
MECHANISTIC requires an asserted biological process/relation connecting biological
entities/states/processes/outcomes.
Method -> detects/estimates/models/identifies/predicts -> biological target is insufficient.
associated with / correlated with / linked to / implicated in / related to are insufficient
by themselves to establish a mechanistic semantic head.
Preserve epistemic qualifiers such as may/might/could.
If one principal assertion cannot be recovered without changing frozen atomicity, ABSTAIN.

## C — COMPARATIVE
COMPARATIVE requires two or more identifiable comparator states/entities/conditions/levels
compared on a shared dimension.
Comparators must be explicitly instantiated or linguistically recoverable from the atomic
claim itself without external inference.
Fold-change/ratio/relative-to/versus/etc. count only when genuine comparator evidence exists.
Higher X associated with better Y is not automatically COMPARATIVE.
Do not invent missing controls/baselines/comparators.

## D1/D2 encoding constraint
D1 and D2 are internal V0.8 repair-decision domains, not new ontology classes, output claim
types, ontology nodes, or schema fields.
Where the frozen ontology requires UNCERTAIN_OTHER, emit UNCERTAIN_OTHER.
Do not create new D1/D2 ontology labels.

## D1 — Reporting Guidance
Evaluate for existing UNCERTAIN_OTHER when the principal proposition concerns documentation,
disclosure, transparency, reporting practice, interpretation communication, or
reproducibility-related communication practice.
Do not route substantive clinical/scientific actions to D1 merely because they contain
should/must/recommend.
The word report is not a hard trigger.

## D2 — Uncertainty / Reliability
Evaluate for existing UNCERTAIN_OTHER when uncertainty, indeterminacy, instability,
unreliability, limited confidence, inability to establish, or inability to distinguish is
itself the principal proposition.
may/might/could/unclear/uncertain/unknown/cannot determine/insufficient evidence are not hard triggers.

## Residual-proposition test
Conceptually set aside the uncertainty expression and ask whether a determinate substantive
proposition remains asserted. This is semantic interpretation, not literal deletion.
If a determinate underlying proposition remains, retain its substantive semantic type while
preserving uncertainty. If unresolvedness itself is asserted, evaluate D2.

## Semantic type vs decision state
UNCERTAIN_OTHER is a semantic type.
ABSTAIN is a decision state.
UNCERTAIN_OTHER != ABSTAIN.
Unresolved classification does not imply UNCERTAIN_OTHER.

## Conservative fallback
Emit UNCERTAIN_OTHER only when the claim positively satisfies its semantic criteria.
If safe classification cannot be completed, return the authorized ABSTAIN/governance state.
Coverage must not be optimized at the expense of semantic safety.

## Prohibited implementation behaviors
No keyword-only hard triggers; no case-ID exceptions; no text rewriting; no decomposition changes;
no inferred comparators; no inferred mechanisms; no association-to-mechanism upgrade; no uncertainty
removal; no Gold reinterpretation; no ontology change; no D1/D2 ontology classes; no use of
UNCERTAIN_OTHER as a failure sink; no trading frozen-correct cases for aggregate accuracy.

## Special exclusions
HD-G0045: ONTOLOGY_AMBIGUITY — excluded from V0.8 adapter repair.
HD-G0155: GOLD / O-03 CONSISTENCY REVIEW — excluded from V0.8 adapter repair.

## Regression governance
Freeze R1/R2/R3/R4 evaluation manifests before V0.8 outputs are observed.
No post-output case removal without explicit append-only Human Gate governance.

Promotion consideration requires:
- RepairGain > 0
- UnexplainedFrozenRegression = 0
- UnauthorizedSemanticExpansion = 0

**HUMAN GATE DECISION: FREEZE PROMPT CONTRACT V1.0**
**PROMPT CONTRACT V1.0: FINAL FROZEN**

---

# II. APPROVED F1–F5 REPAIR CONSTRAINTS

# AIDO-EEA 2.0 V0.8.1
## Narrow Repair Specification — V0.2 Human-Gate Candidate

### Status

This V0.2 incorporates only the five minimal narrowing constraints recommended by the External Challenger.

Governing authority remains:
- AIDO-EEA 2.0 V0.8 Prompt Contract V1.0 — FINAL FROZEN
- V0.8 R1-R4 Human-Gate locks
- V0.8 Consolidated R1-R4 Failure Map

No conceptual repair logic has been expanded beyond V0.1.

---

# 1. Scope

V0.8.1 repair remains restricted to exactly five confirmed repair-driving patterns:

1. broad-quantifier principal-head preservation
2. reporting-vocabulary overreach prevention
3. association-to-mechanism overreach prevention
4. interpretation-rule vs generalization separation
5. subordinate means-clause suppression under semantic-head tie-break

No other semantic behavior is authorized to change.

---

# 2. Frozen invariants

The following remain unchanged:

- Prompt Contract V1.0 as semantic authority
- ontology labels and definitions
- Pilot-25 Gold
- H4 Frozen Gold
- source passages
- atomic decomposition
- scope preservation
- causal-safety rules
- O-03 definition
- R1/R2/R3/R4 manifests and case universes
- blind scoring protocol
- Challenger / Human-Gate governance separation

No case-specific exception may be added.
No keyword hard trigger may be introduced.
No hidden article context may be used.

---

# 3. F1 — GENERALIZATION semantic-head loss

## Confirmed cases
- HD-G0071
- HD-G0086
- HD-G0088

## Existing contract principle
Classification follows the proposition principally asserted.

## Repair instruction
When an atomic claim contains:
1. an explicit broad-quantifier proposition over a class/population/set; and
2. subordinate descriptive or methodological material,

test whether removal of the subordinate material leaves the broad-quantifier proposition intact.

If yes, the broad-quantifier proposition retains semantic-head priority.

## Narrowing constraint added in V0.2
If the quantification belongs to a Domain C comparative dimension involving an explicit/recoverable comparator, evaluate under COMPARATIVE first. F1 must not override Domain C comparator structure.

## Prohibited shortcut
Quantifier tokens alone never determine GENERALIZATION.

---

# 4. F2 — Reporting-vocabulary overreach prevention

## Confirmed case
- HD-G0034

## Existing contract principle
Reporting vocabulary is not a hard trigger. D1 applies only when reporting/documentation/disclosure/communication guidance itself is the principal proposition.

## Repair instruction
Before D1-style routing, ask whether the claim is actually instructing, recommending, requiring, or governing what should be reported/documented/disclosed/communicated.

If the claim instead describes what a document contains, lists, covers, or details, preserve the substantive descriptive semantic head.

## Narrowing constraint added in V0.2
This repair applies only when the principal proposition is genuinely document-content description. If the principal proposition itself is an explicit reporting/disclosure requirement or normative reporting instruction, D1 routing remains fully available.

## Prohibited shortcut
Reporting-related tokens never determine D1 by themselves.

---

# 5. F3 — Association-to-MECHANISTIC overreach prevention

## Confirmed case
- HD-G0065

## Existing contract principle
Association wording and biological-term density are insufficient by themselves to establish MECHANISTIC.

## Repair instruction
Before emitting MECHANISTIC, require that the principal proposition assert a biological process/relation whose presence is structurally necessary to preserve the claim's meaning.

If the sentence remains a list, association, or co-occurrence statement without such a principal process/relation, do not promote to MECHANISTIC.

## Narrowing constraint added in V0.2
If an independent, structurally necessary biological process/relation is genuinely asserted, its MECHANISTIC eligibility is not cancelled merely because associative wording also appears elsewhere in the sentence.

## Prohibited shortcut
Do not infer mechanism from biological density or associative vocabulary alone.

---

# 6. F4 — Interpretation-rule vs GENERALIZATION separation

## Confirmed case
- HD-G0046

## Existing contract principle
The principal proposition controls classification.

## Repair instruction
When a claim contains a normative/interpretive construction, determine whether its principal proposition is specifically a document/record-handling interpretation rule.

If yes, do not emit GENERALIZATION merely because the governed entities are plural or generic.

## Narrowing constraint added in V0.2
Examples such as:
- should be considered
- should be treated as
- should be classified as
- should be recorded as

are illustrative only.

They are neither sufficient nor exhaustive criteria. Routing still requires confirmation that the principal proposition concerns document/record-handling interpretation practice.

## Prohibited shortcut
No phrase-level string match may function as a D1 hard trigger.

---

# 7. F5 — Subordinate means-clause semantic-head hijack

## Confirmed case
- V08-R4-A2

## Evidence status
This repair-driving case is CHALLENGE_ONLY synthetic evidence, not a real-Gold corpus failure. The repair is justified as an operational reinforcement of the already frozen structural-necessity tie-break, not as a new ontology rule.

## Existing contract principle
Use structural necessity to resolve competing semantic heads.

## Repair instruction
For mixed means-result constructions:

1. identify the principal finite predication;
2. test whether the means clause can be removed while leaving a complete, semantically intact proposition;
3. test whether removal of the result clause destroys the main predication.

If the result clause remains structurally necessary, classify from that principal head.

## Narrowing constraint added in V0.2
Examples such as:
- by inhibiting...
- through activation...
- via suppression...
- by inducing...

are illustrative only.

They must never function as reverse keyword triggers. Every case requires the full structural-necessity test above.

## Prohibited shortcut
Sentence-initial biological/causal phrasing does not automatically lose semantic-head eligibility either; the structural test decides.

---

# 8. Cross-pattern precedence

When more than one repair pattern appears relevant:

1. determine principal semantic head first;
2. apply structural necessity to head competition;
3. apply domain-specific exclusion rules;
4. preserve existing ABSTAIN behavior if a safe single-head decision remains unavailable.

Special interaction controls:

- F1 must not override valid Domain C comparator structure.
- F2 and F4 must not cancel one another in mixed document-description + interpretation-rule claims; principal-head analysis remains first.
- F3 and F5 must not jointly suppress a genuinely independent and structurally necessary MECHANISTIC/CAUSAL proposition.

No repair pattern may override causal-safety rules.

---

# 9. Forbidden behavior

V0.8.1 must not:

- introduce new ontology classes
- redefine existing ontology classes
- mutate Frozen Gold
- alter decomposition or scope
- add keyword or phrase hard triggers
- infer missing comparators
- infer hidden mechanisms
- infer external article context
- create case IDs as rules
- change R1/R2/R3/R4 membership
- relax blind-session isolation
- change scoring criteria after outputs are produced

---

# 10. Required post-repair validation

Any approved implementation must use a new isolated blind run over the exact frozen universes:

- R1 Target Repair
- R2 Local Negative
- R3 Frozen Regression
- R4 Boundary Challenge

Required promotion conditions remain:

- `RepairGain > 0`
- `UnexplainedFrozenRegression = 0`
- `UnauthorizedSemanticExpansion = 0`

Additionally:

- all 6 confirmed true overcorrections must be re-evaluated
- V08-R4-A2 must be re-evaluated
- all previously preserved R2/R3 cases must remain protected
- governance-quarantine cases must not be counted as repair success
- F4/F5 examples must not be implemented as phrase-trigger rules

---

# 11. Human-Gate decision

External Challenger verdict on V0.1:
- APPROVE_AS_WRITTEN = 0
- APPROVE_WITH_NARROWING = 5
- REJECT_OVERBROAD = 0
- REJECT_UNSUPPORTED = 0
- ESCALATE_GOVERNANCE = 0

All five requested narrowing constraints have been incorporated into this V0.2 candidate.

Human Gate may now choose:

- `APPROVE V0.8.1 REPAIR SPEC V0.2 — AUTHORIZE IMPLEMENTATION`
- `APPROVE WITH FURTHER MODIFICATIONS`
- `REJECT AND REDRAFT`
- `ESCALATE TO EXTERNAL CHALLENGER`

Until explicit approval, implementation remains prohibited.

---

# III. APPROVED M1 / M2 NEGATIVE GUARDS

# AIDO-EEA 2.0 V0.8.1.1
## Micro-Repair Specification — V0.2 Human-Gate Candidate

### Status

This V0.2 incorporates only the two minimal narrowing clarifications recommended by the External Challenger.

No conceptual expansion beyond M1/M2 V0.1 is introduced.

---

# M1 — Comparator Over-Fire Protection

## Confirmed case
- HD-G0099

## Existing contract principle
COMPARATIVE requires:
1. identifiable comparator entities/states/conditions; and
2. a genuinely shared semantic comparison dimension.

A discourse contrast connective alone is insufficient.

## Guard
Before emitting COMPARATIVE, verify both:
- identifiable comparator entities/states/conditions are present; and
- the compared propositions instantiate the same underlying semantic comparison dimension.

If the clauses express different underlying semantic dimensions, discourse contrast alone must not create COMPARATIVE.

## V0.2 narrowing clarification
“Different measures, quantities, or observational constructs” means that the **underlying semantic dimension itself is different**.

This does **not** mean that two propositions fail the shared-dimension test merely because:
- they use different surface wording;
- they use different units or presentation forms that remain semantically commensurable;
- they express the same dimension through equivalent representations.

Examples such as `whereas`, `while`, or `in contrast` are illustrative only and never string triggers.

## Guard-only constraint
M1 may block a false COMPARATIVE route.
It must not force DESCRIPTIVE or any other replacement class.

After blocking, classification returns to the Final Frozen Prompt Contract.

---

# M2 — F1 Applicability Guard

## Confirmed case
- HD-G0138

## Existing contract principle
F1 broad-quantifier preservation applies only when a quantifier semantically scopes over a class/population/set proposition.

Gradient/association constructions remain governed by the frozen gradient/association rule.

## Guard
F1 may activate only if the claim contains a semantic broad-quantifier scope over a class/population/set proposition.

Continuous covariation constructions such as:
- `the higher X, the more Y`
- `the greater X, the greater Y`

do not satisfy F1 merely because they contain comparative morphology.

## V0.2 narrowing clarification
“Class/population/set-level broad quantifier” is a **semantic scope criterion**, not a requirement for any canonical lexical item.

Legitimate GENERALIZATION may therefore be expressed without literal words such as:
- many
- most
- all
- virtually every

If the proposition semantically generalizes over a class/population/set, F1 remains eligible even when canonical quantifier vocabulary is absent.

Gradient examples are illustrative only and never string triggers.

## Guard-only constraint
M2 may block a false F1/GENERALIZATION route.
It must not force ASSOCIATIVE or any other replacement class.

After blocking, classification returns to the Final Frozen Prompt Contract.

---

# Cross-guard constraint

M1 and M2 are negative guards only.

They:
- do not create new positive routing rules;
- do not add ontology-like behavior;
- do not rewrite the Prompt Contract;
- do not force replacement labels;
- do not operate via phrase matching.

Every application must use the relevant structural/semantic test.

---

# Frozen invariants

Do not change:
- Prompt Contract V1.0
- V0.8.1 F1-F5 conceptual scope
- ontology
- Gold
- decomposition
- scope preservation
- causal safety
- R1/R2/R3/R4 manifests
- Challenger/Human-Gate governance separation

---

---

# IV. APPROVED M2A ATTACHMENT GUARD

# AIDO-EEA 2.0 V0.8.1.2
## M2A Broad-Quantifier Attachment Guard — V0.2 Human-Gate Candidate

### Status

This V0.2 incorporates only the External Challenger's required narrowing of the M2A removal test.

No conceptual expansion beyond M2A V0.1 is introduced.

---

# M2A — Broad-Quantifier Attachment Guard

## Confirmed regression
- HD-G0081

## Governing principle
F1 may activate only when broad quantification semantically attaches to the proposition that carries the principal semantic head.

Broad-quantifier wording elsewhere in the atomic claim is insufficient.

---

# Attachment test

Before F1 may activate, verify both:

1. the candidate broad quantifier semantically scopes over a class/population/set; and
2. the quantifier semantically contributes to the **principal proposition itself**, rather than merely to:
   - evidence/source distribution;
   - citation or provenance framing;
   - reporting context;
   - methodological sampling context;
   - other removable epistemic/contextual framing.

---

# Revised structural-necessity removal test

The removal test must evaluate **propositional content**, not grammatical completeness alone.

A quantified phrase may be treated as non-principal for F1 only if, after its removal:

1. the principal substantive proposition remains grammatically complete; **and**
2. the proposition's substantive semantic content remains intact; **and**
3. the proposition's asserted **scope, breadth, or coverage does not materially change**.

If removal causes the claim to lose or materially alter its asserted breadth/scope, then the quantified phrase remains semantically relevant to the principal proposition and must not be blocked merely because the residual sentence remains grammatical.

---

# Positive protection for genuine GENERALIZATION

M2A must not suppress a genuine GENERALIZATION where the broad quantifier directly contributes to the breadth of the principal proposition.

Example structural pattern:

`Markedly increased glucose uptake has been documented in many human tumor types.`

Removing `in many human tumor types` leaves a grammatical sentence, but removes the breadth of the claim.

Therefore the quantifier remains semantically attached to the principal proposition and remains eligible for F1.

---

# HD-G0081 contrast case

`Increasing evidence in a variety of tumor types suggests that cells with properties of CSCs are more resistant to chemotherapeutic treatments.`

Removing `in a variety of tumor types` leaves the core resistance proposition substantively unchanged.

The phrase scopes over evidence/source distribution rather than over the resistance proposition itself.

Therefore it must not independently activate F1.

---

# Illustrative-only examples

Examples such as:

- `evidence across many tumor types suggests that ...`
- `studies in several cohorts indicate that ...`
- `reports from multiple datasets show that ...`

are illustrative only.

They are **not sufficient** to establish evidence/source attachment.

No phrase or syntactic template may act as a reverse trigger.

Every case must be evaluated using the revised propositional-content and scope/breadth test above.

---

# Guard-only constraint

M2A may only block false F1/GENERALIZATION activation.

It must not force:
- ASSOCIATIVE
- DESCRIPTIVE
- COMPARATIVE
- UNCERTAIN_OTHER
- or any other replacement class

After a false F1 route is blocked, classification returns to the Final Frozen Prompt Contract.

---

# Frozen invariants

Do not change:
- Prompt Contract V1.0
- M1
- M2 conceptual scope
- F1-F5 conceptual scope
- ontology
- Gold
- decomposition
- scope preservation
- causal safety
- R1/R2/R3/R4 manifests
- Challenger/Human-Gate governance separation

---

---

# V. CANONICAL EXECUTION ORDER

For each atomic claim:

1. Identify the proposition principally asserted.
2. Apply the Final Frozen Prompt Contract.
3. Apply F1–F5 only to prevent the confirmed overcorrection/boundary patterns.
4. Apply M1/M2/M2A only as negative guards.
5. Never use keyword, phrase, punctuation, or syntactic-template matching as a sufficient routing rule.
6. Never infer a comparator, mechanism, causal relation, population scope, or external context that is not linguistically supported by the atomic claim.
7. If a guard blocks a false route, return to the Frozen Contract; do not force a replacement class.
8. Preserve existing ABSTAIN behavior when no safe single semantic head can be selected.
9. Emit only the frozen prediction schema.

### Stability rule
Treat every claim independently.
Do not attempt to align predictions with earlier cases or maintain batch-level label balance.
Do not use prior outputs or expected answers.

### Output discipline
Return exactly one prediction object per input row, preserving input_id, passage_id, and candidate_atomic_claim exactly.
