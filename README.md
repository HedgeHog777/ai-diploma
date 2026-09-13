![Python](https://img.shields.io/badge/Python-3.12-blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-supported-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![SHAP](https://img.shields.io/badge/Explainable%20AI-SHAP-purple)
![Voilà](https://img.shields.io/badge/Interactive%20Dashboard-Voilà-green)
![GitHub](https://img.shields.io/badge/Version%20Control-Git-black)
![Status](https://img.shields.io/badge/Status-Final%20Development-brightgreen)

# 🧠 FitnessML Master Thesis

Machine Learning system for forecasting daily energy expenditure using fitness tracker data.

This repository contains the implementation of a complete end-to-end machine learning pipeline developed as part of a Master's degree thesis in Artificial Intelligence / Machine Learning.

The project focuses on analyzing physiological and behavioral data collected from wearable fitness trackers and developing a predictive system capable of forecasting next-day energy expenditure.

---

# 📌 Project Overview

The project includes:

- dataset analysis and validation;
- exploratory data analysis (EDA);
- data preprocessing;
- temporal feature engineering;
- machine learning model development;
- model comparison and evaluation;
- final model selection;
- explainable AI analysis;
- interactive prediction dashboard.

The final prediction task:

**Forecasting next-day energy expenditure**

Target variable:

```
target_calories_next_day
```

The system uses historical activity, physiological and behavioral characteristics to estimate future energy expenditure.

---

# 🏗️ Machine Learning Pipeline

```
Fitness Tracker Dataset
            │
            ▼
Dataset Validation
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Data Preprocessing
            │
            ▼
Feature Engineering
            │
            ▼
Machine Learning Models
            │
            ▼
Model Evaluation & Comparison
            │
            ▼
Final Selected Model
(Random Forest Regressor)
            │
            ▼
Explainable AI
(SHAP Analysis)
            │
            ▼
Interactive Voilà Dashboard
```

---

# 📂 Repository Structure

```
FitnessML_Master/
│
├── README.md
├── config.py
├── utils.py
│
├── notebooks/
│   │
│   ├── 00_project_setup.ipynb
│   ├── 01_dataset_audit.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│   ├── 07_interpretability.ipynb
│   │
│   ├── 0014_VOILA.ipynb
│   └── 0015x_VOILA_Launcher.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── results/
│
│   └── 009_final_results/
│       │
│       ├── random_forest_final.pkl
│       ├── prediction_results.csv
│       ├── fitbit_modeling_features.csv
│       ├── model_metadata.json
│       └── ui_config.json
│
├── figures/
│
├── tables/
│
├── reports/
│
└── thesis/
```

---

# 📊 Dataset

Dataset:

**Health Fitness Tracking – 365 Days**

Main characteristics:

- approximately 365,000 observations;
- 1,000 users;
- 365 consecutive days;
- activity measurements;
- physiological parameters;
- behavioral indicators;
- daily fitness tracker statistics.

The dataset represents longitudinal user activity patterns suitable for time-dependent prediction tasks.

---

# 🤖 Machine Learning Models

The project explores different machine learning approaches:

- classical regression algorithms;
- ensemble learning methods;
- neural network experiments;
- model comparison;
- feature importance analysis.

---

# 🏆 Final Model

Selected final model:

## Random Forest Regressor

Final model properties:

- trained using engineered temporal features;
- uses 65 final input features;
- exported as a production-ready model;
- integrated into the prediction dashboard.

Stored model:

```
results/009_final_results/random_forest_final.pkl
```

---

# 🔍 Explainable Artificial Intelligence

The project includes model interpretation using:

## SHAP

Implemented techniques:

- SHAP TreeExplainer;
- feature contribution analysis;
- global feature importance;
- individual prediction explanation.

The goal is not only accurate forecasting but also understanding which factors influence the model decisions.

---

# 🖥️ Interactive Dashboard

The project contains an interactive Voilà application.

The dashboard provides:

- user selection;
- date selection;
- prediction generation;
- forecast visualization;
- historical user analysis;
- SHAP explanation;
- validation/demo functionality.

Architecture:

```
0014_VOILA.ipynb
        │
        ▼
Dashboard Application
        │
        ▼
0015x_VOILA_Launcher.ipynb
        │
        ▼
Voilà Server
```

Launch notebook:

```
0015x_VOILA_Launcher.ipynb
```

The launcher prepares the environment and starts the interactive application.

---

# 🛠️ Technologies

## Programming

- Python 3.12
- Jupyter Notebook
- Google Colab

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Random Forest
- Regression models

## Visualization

- Matplotlib
- Seaborn

## Explainability

- SHAP

## Interactive Application

- ipywidgets
- Voilà

## Version Control

- Git
- GitHub

---

# 📈 Project Status

Completed:

✅ Project structure  
✅ Dataset audit  
✅ Data validation  
✅ Data preprocessing  
✅ Feature engineering  
✅ Machine learning experiments  
✅ Model comparison  
✅ Final model selection  
✅ SHAP interpretation  
✅ Prediction dashboard  
✅ Final result export  

Current work:

🔄 Thesis documentation  
🔄 Final figures and tables  
🔄 Academic presentation materials  

---

# 🎓 Thesis Context

This project was developed as part of a Master's degree thesis.

Field:

**Artificial Intelligence / Machine Learning**

Research direction:

**Predictive modeling of physiological and behavioral patterns using wearable fitness tracker data**

---

# 👤 Author

**Oles Nabok**

Master's Degree Project

Artificial Intelligence / Machine Learning
