# Changelog

All notable changes to this project are documented in this file.

---

# [Current Development] — Final ML System & Voilà Dashboard

## Added

### Final Machine Learning Pipeline

- Completed final machine learning workflow for fitness tracker data.
- Added final feature engineering pipeline.
- Prepared final modeling dataset.
- Implemented final prediction workflow.
- Added exported model artifacts.

### Final Model

- Selected final Random Forest regression model.
- Exported trained model:

```
results/009_final_results/random_forest_final.pkl
```

- Added model metadata storage:

```
results/009_final_results/model_metadata.json
```

### Prediction System

Added:

- prediction generation;
- user-based selection;
- date-based forecasting;
- prediction result export.

Generated results:

```
results/009_final_results/prediction_results.csv
```

---

# Explainable AI Integration

## Added

Implemented model interpretation using:

- SHAP TreeExplainer;
- feature contribution analysis;
- prediction explanation;
- feature importance visualization.

The explainability module allows analysis of why the model produces specific predictions.

---

# Interactive Dashboard

## Added

Created interactive Voilà dashboard.

Implemented:

- user selection interface;
- date selection;
- prediction display;
- historical analysis;
- SHAP explanation view;
- validation/demo functionality.

Dashboard notebook:

```
0014_VOILA.ipynb
```

---

# Voilà Launcher

## Added

Created dedicated launcher notebook:

```
0015x_VOILA_Launcher.ipynb
```

Features:

- Google Drive integration;
- isolated Voilà environment;
- dependency management;
- automatic server startup;
- Colab compatibility.

---

# Repository Reorganization

## Changed

Updated repository structure to focus on final implementation.

Removed outdated project descriptions from documentation.

Updated README to represent the current state of the project:

- final ML system;
- final artifacts;
- interactive dashboard;
- explainable AI components.

---

# Previous Development Stages

## Dataset & Processing Stage

Implemented:

- initial dataset exploration;
- data validation;
- preprocessing workflow;
- feature preparation.

---

## Modeling Stage

Implemented:

- machine learning experiments;
- model evaluation;
- algorithm comparison;
- final model selection process.

---

## Research Stage

Implemented:

- exploratory analysis;
- visualization experiments;
- feature investigation;
- model interpretation experiments.

---

# Development Notes

The project evolved from experimental machine learning notebooks into a complete forecasting system with:

- trained model artifacts;
- automated inference;
- explainable predictions;
- interactive user interface.

---

# Future Work

Planned:

- final thesis documentation;
- final figures and tables;
- academic presentation materials;
- possible deployment improvements.
