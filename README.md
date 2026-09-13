![Python](https://img.shields.io/badge/Python-3.12-blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-supported-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![SHAP](https://img.shields.io/badge/Explainable%20AI-SHAP-purple)
![Voilà](https://img.shields.io/badge/Interactive%20Dashboard-Voilà-green)
![Git](https://img.shields.io/badge/Version%20Control-Git-black)
![Status](https://img.shields.io/badge/Status-Final%20Development-brightgreen)

# 🧠 FitnessML Master Thesis

Machine Learning project developed as part of a Master's degree thesis.

This repository contains the final implementation of a machine learning system for forecasting daily energy expenditure using fitness tracker data.

The project focuses on developing a complete pipeline from processed fitness data to an interactive prediction dashboard with explainable AI capabilities.

---

# 📌 Project Overview

The main objective of the project is to create a predictive model capable of forecasting:

```
target_calories_next_day
```

using historical fitness tracker information and engineered behavioral features.

The final system includes:

- data processing;
- feature engineering;
- machine learning modeling;
- model evaluation;
- final model selection;
- prediction generation;
- explainable AI analysis;
- interactive dashboard deployment.

---

# 🏗️ Final System Architecture

```
Fitness Tracker Data
          │
          ▼
Data Processing
          │
          ▼
Feature Engineering
          │
          ▼
Machine Learning Models
          │
          ▼
Model Evaluation
          │
          ▼
Final Random Forest Model
          │
          ▼
Prediction Engine
          │
          ▼
SHAP Explainability
          │
          ▼
Voilà Interactive Dashboard
```

---

# 📂 Repository Structure

```
FitnessML_Master/

│
├── notebooks/
│
│   ├── 0014_VOILA.ipynb
│   │       Final interactive dashboard application
│   │
│   └── 0015x_VOILA_Launcher.ipynb
│           Voilà runtime launcher
│
├── results/
│
│   └── 009_final_results/
│
│       ├── random_forest_final.pkl
│       │       Final trained Random Forest model
│       │
│       ├── prediction_results.csv
│       │       Generated predictions
│       │
│       ├── fitbit_modeling_features.csv
│       │       Final modeling dataset
│       │
│       ├── model_metadata.json
│       │       Model configuration and metadata
│       │
│       └── ui_config.json
│               Dashboard configuration
│
├── README.md
```

---

# 🤖 Machine Learning Model

## Final Model

The selected final model is:

**Random Forest Regressor**

The model predicts:

```
target_calories_next_day
```

The final model:

- uses engineered fitness features;
- contains the final trained parameters;
- supports individual predictions;
- is integrated into the dashboard application.

Model artifact:

```
results/009_final_results/random_forest_final.pkl
```

---

# 📊 Prediction System

The prediction system allows:

- selecting a user;
- selecting a prediction date;
- generating next-day energy expenditure forecasts;
- viewing historical information;
- analysing prediction results.

Generated results are stored in:

```
results/009_final_results/prediction_results.csv
```

---

# 🔍 Explainable AI

To improve transparency and interpretability, the project includes:

## SHAP (SHapley Additive exPlanations)

Implemented functionality:

- feature contribution analysis;
- individual prediction explanation;
- model behaviour interpretation;
- importance ranking.

SHAP explanations are integrated into the interactive dashboard.

---

# 🖥️ Interactive Dashboard

The project includes a web-based interactive dashboard built with:

- Voilà;
- Jupyter Widgets;
- ipywidgets.

Dashboard functionality:

- user selection;
- date selection;
- prediction generation;
- result visualization;
- historical analysis;
- SHAP explanations.

Application notebooks:

```
0014_VOILA.ipynb
```

and

```
0015x_VOILA_Launcher.ipynb
```

The launcher prepares the runtime environment and starts the Voilà application.

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

## Explainable AI

- SHAP

## Visualization

- Matplotlib
- Seaborn

## Interactive Application

- Voilà
- ipywidgets

## Version Control

- Git
- GitHub

---

# 🚀 Running the Dashboard

The dashboard is designed to run inside Google Colab.

Start the application using:

```
0015x_VOILA_Launcher.ipynb
```

The launcher:

1. mounts project storage;
2. prepares the Voilà environment;
3. loads the final dashboard notebook;
4. starts the interactive application.

---

# 📈 Project Status

Completed:

✅ Data processing pipeline  
✅ Feature engineering  
✅ Machine learning experiments  
✅ Model evaluation  
✅ Final model selection  
✅ Prediction system  
✅ SHAP explainability  
✅ Interactive dashboard  

Current work:

🔄 Master's thesis documentation  
🔄 Final figures and tables  
🔄 Presentation materials  

---

# 🎓 Thesis Context

This project was developed as part of a Master's degree thesis.

Field:

**Artificial Intelligence / Machine Learning**

Research direction:

**Predictive modeling of fitness tracker data using machine learning methods**

---

# 👤 Author

**Oles Nabok**

Master's Degree Thesis

Artificial Intelligence / Machine Learning
