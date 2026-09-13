# Project Style Guide

This document defines coding, formatting and development conventions used throughout the FitnessML Master Thesis project.

The goal is to keep the project reproducible, modular and easy to maintain.

---

# General Principles

## Modular development

- Keep notebooks focused on one logical task.
- Avoid large monolithic notebooks.
- Move reusable functionality into Python modules.
- Store configuration parameters separately.

Main project modules:

```
config.py
utils.py
```

---

## Notebook philosophy

One notebook = one pipeline stage.

Notebooks should:

- perform analysis or experiments;
- generate documented results;
- save artifacts;
- avoid unnecessary duplicated code.

---

# Naming Conventions

## Notebooks

Notebook names follow pipeline order:

```
00_project_setup

01_dataset_audit

02_eda

03_preprocessing

04_feature_engineering

05_modeling

06_evaluation
```

Additional final-stage notebooks:

```
0014_VOILA

0015_VOILA_Launcher
```

---

# Files and Artifacts

## Figures

Naming format:

```
<stage>_<description>.png
```

Examples:

```
02_activity_distribution.png

03_missing_values_heatmap.png

06_model_comparison.png
```

All important figures should be saved using:

```python
utils.save_figure()
```

---

## Tables

Naming format:

```
<stage>_<description>.csv
```

Examples:

```
01_dataset_summary.csv

03_processed_features.csv

06_model_metrics.csv
```

Save tables using:

```python
utils.save_table()
```

---

## Reports

Markdown reports:

```
reports/
```

Naming format:

```
<stage>_<description>.md
```

Examples:

```
01_dataset_audit.md

06_model_evaluation.md
```

---

# Notebook Formatting

Every notebook should contain:

## 1. Introduction

Markdown cell explaining:

- notebook purpose;
- research question;
- expected output.

---

## 2. Imports

Example:

```python
import os
import sys
import importlib

import numpy as np
import pandas as pd

import config
import utils
```

---

## 3. Project initialization

Reload local modules:

```python
config = importlib.reload(config)
utils = importlib.reload(utils)
```

Initialize paths and settings.

---

## 4. Dataset loading

Use project utilities where possible.

Avoid hardcoded paths.

Example:

```python
df = utils.load_dataset()
```

---

## 5. Main analysis

Each major section starts with:

```python
utils.section("Section name")
```

Examples:

```
Dataset overview

Data quality

Feature engineering

Model training

Evaluation
```

---

## 6. Export results

Generated artifacts must be stored in project directories.

Examples:

```
figures/

tables/

reports/

results/
models/
```

---

## 7. Completion

Every notebook should end with:

```python
utils.section("Notebook completed")
```

---

# Markdown Style

Before every major code block explain:

- what is being performed;
- why it is needed;
- expected result.

Avoid unexplained code blocks.

---

# Console Output

Preferred:

```python
utils.section("Section name")
```

Avoid excessive:

```python
print()
```

Use print only for important status information.

---

# Configuration Rules

Do not hardcode:

- file paths;
- random seeds;
- dataset locations;
- feature lists;
- model parameters.

Store reusable values in:

```
config.py
```

---

# Machine Learning Workflow

Current project pipeline:

```
config.py
        │
        ▼
utils.py
        │
        ▼
00_project_setup
        │
        ▼
01_dataset_audit
        │
        ▼
02_eda
        │
        ▼
03_preprocessing
        │
        ▼
04_feature_engineering
        │
        ▼
05_modeling
        │
        ▼
06_evaluation
        │
        ▼
Model comparison
        │
        ▼
Explainable AI
        │
        ▼
Final results
        │
        ▼
Voilà Application
```

---

# Machine Learning Experiment Rules

Every experiment should document:

## Dataset

- input dataset;
- features;
- target variable;
- preprocessing steps.

---

## Model

Include:

- algorithm;
- parameters;
- random state;
- training configuration.

Example:

```python
RANDOM_STATE = 42
```

---

## Evaluation

Include:

- selected metrics;
- comparison tables;
- visualizations;
- conclusions.

---

# Version Control

Commit after completing a logical development step.

Commit messages should describe the change.

Examples:

```
Add feature engineering pipeline

Improve model evaluation metrics

Create Voilà dashboard

Refactor project utilities
```

---

# Code Quality

Prefer:

- readable code;
- reusable functions;
- clear variable names;
- minimal duplication.

Avoid:

- unused code;
- temporary experiments in final notebooks;
- hidden dependencies.

---

# Final Project Structure

```
FitnessML_Master/

├── config.py
├── utils.py
├── notebooks/
├── data/
├── models/
├── figures/
├── tables/
├── reports/
├── results/
└── thesis/
```
