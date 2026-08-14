# Reproducibility Notes

## Exp1 integrity boundary

The final stability instrument was defined by:
- flat canonical prompt SHA256: `395657f51ffe53058633941f546558eab7f28bbcd22dc5658c543389ddcc5619`
- frozen input SHA256: `2cd00cdd2e951bdc81dcdd81f50f608beb82132e4f5fbdef258247a721cc86bb`

Each final blind run recorded:
- no Gold access;
- no scoring access;
- no prior-prediction access;
- no project-memory access.

## Public-release rule

Do not publish source-derived claim text unless redistribution rights are confirmed. A Zenodo software release can contain the code, frozen hashes, prompt, schemas, and public-safe reports while the restricted corpus remains private.

## Recommended GitHub/Zenodo workflow

1. Create a GitHub repository.
2. Upload this package contents.
3. Select an explicit software license.
4. Fill `CITATION.cff` and `.zenodo.json`.
5. Create a tagged GitHub release, e.g. `v1.0.0-exp1`.
6. Connect the repository to Zenodo and archive the tagged release.
7. Insert the resulting DOI into the manuscript and SI.
