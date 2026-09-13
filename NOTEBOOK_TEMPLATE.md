# Notebook Template

This document defines the standard structure and development conventions for notebooks in the FitnessML Master Thesis project.

The goal is to keep all notebooks consistent, reproducible and easy to maintain.

---

# Standard Notebook Structure

Each notebook should follow the same general organization.

---

# 1. Notebook title

Every notebook starts with a clear Markdown title describing its purpose.

Example:

```markdown
# 03. Data Preprocessing

Description of notebook purpose.
```

---

# 2. Import libraries

Standard Python imports.

Example:

```python
import os
import sys
import importlib

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
```

Project-specific imports:

```python
import config
import utils
```

---

# 3. Reload project modules

During development, always reload local modules.

Example:

```python
config = importlib.reload(config)
utils = importlib.reload(utils)
```

This ensures that changes in project files are applied without restarting the notebook.

---

# 4. Connect Google Drive (if required)

For Google Colab notebooks:

```python
from google.colab import drive

drive.mount("/content/drive")
```

---

# 5. Configure project paths

Use centralized configuration.

Example:

```python
PROJECT_DIR = config.PROJECT_DIR
DATA_DIR = config.DATA_DIR
RESULTS_DIR = config.RESULTS_DIR
```

Avoid hardcoding paths inside notebooks.

---

# 6. Load data

Datasets should be loaded through project utilities whenever possible.

Example:

```python
df = utils.load_dataset()
```

Additional preparation:

```python
utils.set_plot_style()
```

---

# 7. Notebook sections

Each major logical block should start with:

```python
utils.section("Section title")
```

Recommended sections:

- Dataset Overview
- Data Quality Analysis
- Exploratory Data Analysis
- Data Preparation
- Feature Engineering
- Model Training
- Model Evaluation
- Results Analysis

---

# 8. Results generation

All generated artifacts should be saved using project utilities.

## Figures

```python
utils.save_figure(
    fig,
    "figure_name"
)
```

---

## Tables

```python
utils.save_table(
    dataframe,
    "table_name"
)
```

---

## Reports

```python
utils.save_report(
    content,
    "report_name"
)
```

---

# 9. Machine Learning notebooks

Modeling notebooks should additionally contain:

## Dataset definition

- input features;
- target variable;
- train/test split strategy.

---

## Model configuration

Document:

- algorithm;
- parameters;
- random seed;
- evaluation metrics.

Example:

```python
MODEL_NAME = "Random Forest"

RANDOM_STATE = 42
```

---

## Training

Training code should be separated from evaluation.

Example:

```python
model.fit(
    X_train,
    y_train
)
```

---

## Evaluation

Always include:

- selected metrics;
- comparison tables;
- visual analysis;
- saved results.

---

# 10. Final notebook section

Every notebook should end with:

```python
utils.section("Notebook completed")
```

Optional:

```python
print("Notebook completed successfully.")
```

---

# Naming Convention

Notebook names follow the project pipeline order:

```
00_project_setup

01_dataset_audit

02_eda

03_preprocessing

04_feature_engineering

05_modeling

06_evaluation
```

Additional application notebooks:

```
0014_VOILA

0015_VOILA_Launcher
```

---

# Notebook Principles

## One notebook = one logical stage

Avoid mixing unrelated tasks.

Example:

Good:

```
05_modeling
    - train models
    - compare models
```

Bad:

```
05_everything
    - preprocessing
    - training
    - visualization
    - final app
```

---

## Reproducibility

Every notebook should:

- use project configuration;
- avoid hidden state;
- save important outputs;
- document important decisions.

---

## Research Traceability

Each notebook should make clear:

- what was done;
- why it was done;
- what result was obtained;
- where the result was saved.

---

# Current Project Pipeline

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
Final Model
        │
        ▼
Explainable AI
        │
        ▼
Voilà Application
```
