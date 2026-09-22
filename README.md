<div align="center">

# 🧬 Protein Mutation Analyzer

**A reusable Colab notebook for comparing a wild-type protein with a single-residue variant**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/Protein_Mutation_Analyzer.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Biopython](https://img.shields.io/badge/Biopython-Bioinformatics-green)
![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=matplotlib)
[![UniProt](https://img.shields.io/badge/Data-UniProt-orange)](https://www.uniprot.org/)

</div>

---

<div align="center">

# 🧬 Protein Mutation Analyzer

**A reusable Colab notebook for comparing a wild-type protein with a single-residue variant**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/Protein_Mutation_Analyzer.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Biopython](https://img.shields.io/badge/Biopython-1.80%2B-1f9d55?logo=biopython&logoColor=white)](https://biopython.org/)
[![UniProt](https://img.shields.io/badge/Data-UniProt-orange)](https://www.uniprot.org/)

</div>

---

## 📖 Overview

This notebook downloads a real protein sequence from **UniProt**, builds a mutant sequence from a variant you give it (for example `R175H`), and compares the two computationally: residue properties, substitution scores, whole-protein properties, and UniProt annotation context.

The built-in example is **human TP53** (UniProt `P04637`) with the well-known cancer variant **p.Arg175His (R175H)** — but the notebook works for any protein and any single amino-acid substitution. Change two settings and it runs on your own protein.

> ⚠️ **Scope:** protein sequence analysis only. No DNA/nucleotide analysis, no structure prediction, no pathogenicity prediction.

---

## ✨ What it does

| Step | What happens |
|:---:|---|
| 🌐 | Downloads the reference sequence from **UniProt** and validates it |
| ✅ | Confirms the wild-type residue is really at the given position |
| 🧪 | Builds and validates the mutant sequence |
| 🔍 | Detects substitutions, insertions and deletions (self-tested first) |
| ⚖️ | Compares residue properties — weight, hydropathy, polarity, **charge at pH 7.4** |
| 📊 | Scores the substitution with **BLOSUM62** and the **Grantham distance** |
| 🧫 | Compares whole-protein properties (MW, pI, GRAVY, instability index…) |
| 📈 | Plots net charge across the full pH range |
| 🗺️ | Shows where the mutation sits relative to annotated UniProt domains |
| 🔁 | Compares several variants of the same protein side by side |
| 💾 | Exports tables, figures, a text report and a metadata file |

---

## 📷 Example output — TP53 R175H

<div align="center">
<img src="images/R175H_residue_property_comparison.png" width="700" alt="Residue property comparison"/>
</div>

| Property | Arginine (wild type) | Histidine (mutant) | Change |
|---|---:|---:|---:|
| Molecular weight (Da) | 174.20 | 155.15 | **−19.05** |
| Hydropathy (Kyte–Doolittle) | −4.50 | −3.20 | **+1.30** |
| Charge at pH 7.4 | +1.00 | +0.04 | **−0.96** |

**BLOSUM62 score:** `0`  **Grantham distance:** `29` *(conservative)*

<div align="center">
<img src="images/TP53_R175H_position.png" width="700" alt="Mutation position on the protein"/>
</div>

> 💡 R175H scores as a "conservative" substitution by both measures, yet it is one of the most frequently observed TP53 mutations in cancer. Sequence-similarity scores describe the *type* of amino-acid change, not *where* it happens or what it does to the folded protein — which is exactly why this notebook does not stop there.

---

## 🚀 How to use it

1. Click **Open in Colab** above.
2. In **Section 2**, set:
   ```python
   UNIPROT_ID = "P04637"   # any UniProt accession
   VARIANT    = "R175H"    # or "p.R175H" or "p.Arg175His"
   ```
3. **Runtime → Run all**. An internet connection is required (UniProt lookup).
4. Results are saved to `results_<accession>_<variant>/` and offered as a zip download.

---

## 📁 Output files

```
results_P04637_R175H/
├── P04637.fasta                          reference sequence, exactly as downloaded
├── mutation_comparison.csv               substitutions / insertions / deletions found
├── protein_property_comparison.csv       whole-protein properties, WT vs mutant
├── amino_acid_property_change.csv        residue-level property changes
├── variant_comparison.csv                multi-variant comparison table
├── uniprot_features_at_position.csv      UniProt domains/sites at the mutation
├── mutation_summary.csv                  one-row summary of the whole analysis
├── protein_mutation_report.txt           plain-text report
├── analysis_metadata.json                UniProt version, date, checksum, package versions
└── *.png                                 all figures, print quality (300 dpi)
```

---

## 🧰 Built with

<div align="left">
<img src="https://img.shields.io/badge/Biopython-sequence%20parsing-1f9d55?logo=biopython&logoColor=white" />
<img src="https://img.shields.io/badge/pandas-data%20tables-150458?logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-numerics-013243?logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-figures-11557C?logo=plotly&logoColor=white" />
<img src="https://img.shields.io/badge/UniProt%20REST%20API-data%20source-orange" />
</div>

---

## ⚠️ Limitations

- Sequence-level only — no 3D structure, no evolutionary conservation.
- Side-chain charge is estimated from free-amino-acid pKa values; the real pKa inside a folded protein can shift.
- BLOSUM62 and Grantham describe the *type* of substitution, not its structural position or effect.
- The variant must be numbered against the same reference sequence that is downloaded (isoform mismatches will fail the validation step on purpose).
- **Does not predict pathogenicity.** For that, see AlphaFold DB, PolyPhen-2, SIFT, CADD, AlphaMissense, ClinVar and gnomAD.

---



##  Author

**Wajeeha Urooj**
Bioinformatics | Computational Biology

</div>

<div align="center">

*Built as part of an MPhil research portfolio in Bioinformatics.*

</div>
