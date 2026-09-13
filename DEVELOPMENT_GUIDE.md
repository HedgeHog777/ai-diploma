# Development Guide

## FitnessML Master Thesis Development Pipeline

This document describes the development workflow and evolution of the FitnessML project.

The project was developed through several stages, starting from data preparation and exploration and progressing toward a final machine learning system with an interactive Voilà dashboard.

---

# Development Workflow

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
Final Model Selection
        │
        ▼
Explainable AI
        │
        ▼
Voilà Dashboard
```

---

# Stage 0 — Project Setup

## Purpose

Initial project configuration and environment preparation.

Main components:

```
config.py
utils.py
```

Responsibilities:

- project paths;
- common configuration;
- reusable helper functions;
- environment initialization.

---

# Stage 1 — Dataset Audit

Notebook:

```
00_project_setup
01_dataset_audit
```

Purpose:

- inspect source data;
- validate structure;
- identify missing values;
- analyze available features;
- prepare data understanding.

---

# Stage 2 — Exploratory Data Analysis

Notebook:

```
02_eda
```

Purpose:

- investigate data distributions;
- analyze relationships between variables;
- visualize activity and physiological patterns;
- identify important characteristics for modeling.

---

# Stage 3 — Data Preprocessing

Notebook:

```
03_preprocessing
```

Purpose:

- clean data;
- prepare modeling tables;
- transform variables;
- create consistent input format.

---

# Stage 4 — Feature Engineering

Notebook:

```
04_feature_engineering
```

Purpose:

Creation of machine learning features:

- temporal features;
- historical behavior indicators;
- aggregated metrics;
- model-ready feature sets.

The output of this stage became the basis for final model training.

---

# Stage 5 — Machine Learning Modeling

Notebook:

```
05_modeling
```

Purpose:

Development and comparison of machine learning approaches.

Activities:

- model training;
- parameter evaluation;
- performance comparison;
- model selection.

---

# Stage 6 — Model Evaluation

Notebook:

```
06_evaluation
```

Purpose:

- compare model performance;
- analyze prediction quality;
- select final candidate model;
- prepare final results.

---

# Final Development Stage

After the research pipeline was completed, the project evolved into an application-oriented system.

Added components:

## Final Model

```
random_forest_final.pkl
```

A trained Random Forest model prepared for inference.

---

## Prediction System

Generated artifacts:

```
prediction_results.csv
fitbit_modeling_features.csv
model_metadata.json
```

Used for:

- predictions;
- dashboard operation;
- model information.

---

## Explainable AI

Implemented:

- SHAP analysis;
- feature contribution analysis;
- prediction explanations.

---

## Interactive Dashboard

Final application:

```
0014_VOILA.ipynb
```

Launcher:

```
0015x_VOILA_Launcher.ipynb
```

The dashboard provides:

- user selection;
- prediction generation;
- result visualization;
- explainability information.

---

# Development Evolution

The project progressed through the following phases:

```
Research Prototype
        │
        ▼
Data Analysis Pipeline
        │
        ▼
Feature Engineering Pipeline
        │
        ▼
Machine Learning Experiments
        │
        ▼
Final Predictive Model
        │
        ▼
Interactive ML Application
```

---

# Current Project State

The current repository represents the final application stage.

The original experimental notebooks document the research process, while the final artifacts and Voilà application represent the deployed thesis system.
