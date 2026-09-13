# Project Structure

## FitnessML Master Thesis

This document describes the internal organization of the project and the development pipeline.

---

# Development Pipeline

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

---

# Core Configuration

## config.py

Central project configuration.

Responsibilities:

- project paths;
- dataset locations;
- global parameters;
- experiment configuration.

---

# Utility Layer

## utils.py

Shared helper functions used across notebooks.

Contains:

- reusable data processing functions;
- visualization helpers;
- common utilities.

---

# Research Pipeline

## 00_project_setup

Purpose:

Initialize project environment.

Tasks:

- configure paths;
- prepare dependencies;
- verify project structure.

---

## 01_dataset_audit

Purpose:

Initial dataset investigation.

Tasks:

- inspect dataset structure;
- validate columns;
- check data quality;
- identify possible issues.

---

## 02_eda

Purpose:

Exploratory Data Analysis.

Tasks:

- analyze distributions;
- visualize variables;
- investigate relationships;
- identify important patterns.

---

## 03_preprocessing

Purpose:

Prepare clean data for modeling.

Tasks:

- data cleaning;
- missing value handling;
- transformations;
- dataset preparation.

---

## 04_feature_engineering

Purpose:

Create machine learning features.

Tasks:

- temporal features;
- aggregated statistics;
- behavioral indicators;
- model input preparation.

---

## 05_modeling

Purpose:

Train and compare machine learning models.

Tasks:

- model experiments;
- training;
- hyperparameter evaluation;
- performance comparison.

---

## 06_evaluation

Purpose:

Final model evaluation.

Tasks:

- compare metrics;
- analyze errors;
- select final model;
- prepare final results.

---

# Final Application Layer

After the research pipeline, the project was extended into an interactive machine learning application.

## Final Model

Contains:

- trained model artifacts;
- prediction pipeline;
- metadata.

---

## Explainable AI

Implemented:

- SHAP analysis;
- feature importance;
- prediction interpretation.

---

## Voilà Dashboard

Files:

```
0014_VOILA.ipynb
0015x_VOILA_Launcher.ipynb
```

Purpose:

Provide an interactive interface for:

- selecting users;
- generating predictions;
- visualizing results;
- explaining model decisions.

---

# Repository Evolution

The project evolved from a research notebook workflow into a complete ML application:

```
Data Research
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning
      │
      ▼
Model Evaluation
      │
      ▼
Explainability
      │
      ▼
Interactive Dashboard
```
