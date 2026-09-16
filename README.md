# 🧬 Protein Mutation Analyzer

<p align="center">
  <strong>A Python-based bioinformatics toolkit for protein mutation analysis</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Biopython-Bioinformatics-green">
  <img src="https://img.shields.io/badge/pandas-Data%20Analysis-purple?logo=pandas">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=matplotlib">
  <img src="https://img.shields.io/badge/pytest-12%20tests-success?logo=pytest">
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_NOTEBOOK_LINK)
</p>

---

## 🔬 Overview

**Protein Mutation Analyzer** is a reusable Python toolkit for comparing wild-type and mutant **protein sequences** and characterizing sequence-level and physicochemical changes associated with amino-acid substitutions.

The project combines protein sequence analysis, residue-level property analysis, whole-protein physicochemical analysis, visualization, and automated testing into a reproducible bioinformatics workflow.

---

## Biological Example

The development workflow uses the human **TP53 protein** as a real biological example.

| Feature            | Information             |
| ------------------ | ----------------------- |
| 🧬 Protein         | TP53                    |
| 🌍 Organism        | *Homo sapiens*          |
| 🔗 UniProt ID      | P04637                  |
| 📏 Protein length  | 393 aa                  |
| 🧪 Example variant | p.Arg175His (R175H)     |
| 🔄 Mutation type   | Amino-acid substitution |

The R175H example demonstrates how a single amino-acid substitution can be detected computationally and how the properties of the original and substituted residues can be compared.

---

## Key Features

### 🧪 Protein Sequence Analysis

* Compare wild-type and mutant protein sequences
* Detect amino-acid substitutions
* Identify mutation positions
* Calculate protein length changes
* Validate protein sequences
* Generate mutation summaries

### 📊 Physicochemical Analysis

The toolkit calculates and compares:

* Molecular weight
* Isoelectric point (pI)
* GRAVY / hydropathy
* Aromaticity
* Instability index
* Residue hydropathy
* Residue pKa
* Approximate residue charge at pH 7.4

### 📈 Visualization

The development notebook provides visual analysis of:

* Mutation positions
* Residue physicochemical differences
* Whole-protein property differences

### 🧪 Automated Testing

The project includes a `pytest` test suite covering:

* Sequence comparison
* Mutation detection
* Sequence validation
* Length changes
* Mutation summaries
* Residue properties
* Protein-level property calculations

**Current test status:**

**12 passed**

---

## Workflow

```
Wild-Type Protein
        │
        ▼
┌────────────────────┐
│ Sequence Validation │
└────────────────────┘
        │
        ▼
   Mutant Protein
        │
        ▼
┌────────────────────┐
│ Sequence Comparison │
└────────────────────┘
        │
   ┌────┴────┐
   ▼         ▼
Mutation   Length
Detection  Comparison
   │
   ▼
┌──────────────────────────┐
│ Residue Property Analysis│
└──────────────────────────┘
        │
        ▼
┌──────────────────────────┐
│ Whole-Protein Properties │
└──────────────────────────┘
        │
        ▼
   📊 Visualization
        │
        ▼
   📄 Result Reporting
```

---

## 📁 Project Structure

```
protein-mutation-analyzer/
│
├── protein_mutation/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── properties.py
│   └── cli.py
│
├── tests/
│   ├── test_analyzer.py
│   └── test_properties.py
│
├── Protein_Mutation_Analyzer_Development.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```
git clone https://github.com/wajeeha-urooj/protein-mutation-analyzer.git
cd protein-mutation-analyzer
```

Install the required dependencies:

```
pip install -r requirements.txt
```

---

## 💻 Command-Line Usage

The analyzer can compare two protein sequences directly from the command line.

Example:

```
python -m protein_mutation.cli "ACDEFGHIK" "ACDFFGHIK"
```

The program reports:

* 🧬 Wild-type and mutant sequence lengths
* 📏 Length difference
* 🔄 Detected amino-acid substitutions
* 📊 Whole-protein physicochemical properties
* 🧪 Residue-level property changes for a single substitution

---

## 🧪 Running the Tests

Run the complete test suite:

```
pytest -q
```

Expected result:

```
12 passed
```

---

## 📓 Development Notebook

The notebook **Protein_Mutation_Analyzer_Development.ipynb** demonstrates the complete analysis workflow using the human TP53 R175H example.

### Notebook Workflow

1. 🧬 Retrieve the TP53 reference sequence from UniProt
2. 🔍 Inspect and validate the reference sequence
3. 📍 Verify the mutation position
4. 🧪 Generate the mutant sequence
5. ✅ Validate the mutant sequence
6. 🔄 Detect sequence differences
7. 📏 Compare protein lengths
8. ⚗️ Analyze residue physicochemical properties
9. 📊 Compare whole-protein properties
10. 📈 Visualize mutation-related changes
11. 📤 Export analysis results

---

## 📤 Outputs

The analysis can generate:

* 📋 Mutation tables
* 🧬 Sequence comparison results
* 📊 Physicochemical property tables
* 📈 Visualization figures
* 📄 Text-based analysis reports
* 📁 CSV result files

---

## 🧠 Scientific Scope

This project focuses on **protein sequence-level mutation analysis**.

It currently does not directly predict:

* Protein structure
* Variant pathogenicity
* Clinical outcome
* Protein folding
* Functional impact using machine learning

The current length-change analysis reports differences in protein sequence length but does not perform advanced pairwise alignment for detailed insertion/deletion characterization.

Physicochemical property comparisons are computational sequence-derived measurements and should not be interpreted as experimental measurements.

---

## Future Development

Potential future extensions include:

* 📂 FASTA-file input
* 🧬 Pairwise sequence alignment for robust indel detection
* 🔢 Multiple mutation support
* 📊 Batch variant analysis
* 🧩 Structural mapping using PDB structures
* 🔗 Integration with public variant databases
* 📄 Automated report generation
* 🤖 Machine-learning-based functional impact prediction

---

## Technologies

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| 🐍 Python     | Core programming          |
| 🧬 Biopython  | Protein sequence analysis |
| 🐼 pandas     | Data processing           |
| 🔢 NumPy      | Numerical analysis        |
| 📊 Matplotlib | Visualization             |
| 🌐 Requests   | UniProt API retrieval     |
| 🧪 pytest     | Automated testing         |

---

##  Author

###  Wajeeha Urooj

**Bioinformatics | Computational Biology**

---

<p align="center">
  <i>Developed as a bioinformatics portfolio project for reproducible protein sequence analysis.</i>
</p>
