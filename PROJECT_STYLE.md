# Project Style Guide

This document defines coding and formatting conventions used throughout the project.

---

# General principles

- Keep notebooks modular.
- One notebook = one pipeline stage.
- Reuse functions from utils.py whenever possible.
- Store constants in config.py.
- Avoid duplicated code.

---

# Naming conventions

## Notebooks

00_project_setup

01_dataset_audit

02_eda

03_preprocessing

...

---

## Figures

Example:

02_histograms.png

02_boxplots.png

03_scaled_features.png

---

## Tables

Example:

02_correlation_matrix.csv

03_train_dataset.csv

---

## Reports

Example:

02_eda.md

03_preprocessing.md

---

# Notebook formatting

Every notebook should contain:

1. Markdown introduction

2. Imports

3. Project initialization

4. Dataset loading

5. Analysis

6. Export

7. Completion message

---

# Markdown style

Use Markdown before every major section.

Explain:

- what is being done;
- why it is performed;
- expected outcome.

---

# Console output

Use

```python
utils.section(...)
```

for major sections.

Avoid excessive print() statements.

---

# Graphs

All graphs should be saved using

```python
utils.save_figure()
```

Titles should be informative.

Axis labels should be readable.

---

# Tables

Save every important table.

Use

```python
utils.save_table()
```

---

# Reports

Each notebook should generate its own Markdown report.

Reports are stored in

reports/

---

# Configuration

Do not hardcode:

- file paths;
- random seeds;
- dataset names;
- feature lists.

Store them in config.py.

---

# Version control

Commit after completing a logical stage.

Use descriptive commit messages.

Example:

Refactor preprocessing pipeline

Add EDA visualizations

Improve dataset audit

# Machine Learning Workflow

00 Project setup

↓

01 Dataset audit

↓

02 Exploratory data analysis

↓

03 Preprocessing

↓

04 Feature engineering

↓

05 Model training

↓

06 Model evaluation

↓

07 Model comparison

↓

08 Explainability

↓

09 Final results