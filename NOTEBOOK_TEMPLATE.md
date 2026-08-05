# Notebook Template

This document defines the standard structure for every notebook in the FitnessML Master Thesis project.

---

# Standard notebook structure

## 1. Notebook title

Markdown heading with a short description of the notebook purpose.

Example:

# 03. Data Preprocessing

---

## 2. Import libraries

```python
import os
import sys
import importlib
...
```

---

## 3. Connect Google Drive

```python
drive.mount(...)
```

---

## 4. Connect project

```python
PROJECT_DIR = ...
```

---

## 5. Import project modules

```python
import config
import utils
```

Always reload modules:

```python
config = importlib.reload(config)
utils = importlib.reload(utils)
```

---

## 6. Load dataset

```python
df = utils.load_dataset()
```

If necessary:

```python
utils.set_plot_style()
```

---

## 7. Main notebook sections

Each major step should begin with

```python
utils.section("Section title")
```

Examples:

- Dataset
- Data Quality
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Evaluation

---

## 8. Save generated results

Figures:

```python
utils.save_figure(...)
```

Tables:

```python
utils.save_table(...)
```

Reports:

```python
utils.save_report(...)
```

---

## 9. Finish notebook

```python
utils.section("Notebook completed")
```

---

# Naming convention

Notebook names:

00_project_setup

01_dataset_audit

02_eda

03_preprocessing

...

One notebook = one logical stage of the ML pipeline.