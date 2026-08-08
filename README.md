# Fetal Health Monitoring using Cardiotocography (CTG)

## Project Overview

Fetal Health Monitoring using Cardiotocography (CTG) is a Machine Learning based web application designed to classify fetal health conditions into three categories:

- Normal
- Suspect
- Pathological

The system uses important Cardiotocography (CTG) parameters and a trained XGBoost machine learning model to provide a fetal health risk classification.

The project combines Machine Learning with a Flask-based web dashboard to provide an interactive interface for entering CTG parameters and viewing prediction results.

> **Note:** This project is an academic/ML prototype intended for educational and demonstration purposes. It is not intended to replace professional medical diagnosis or clinical decision-making.

---

## Objectives

- Analyze Cardiotocography (CTG) parameters using Machine Learning.
- Identify important features affecting fetal health classification.
- Compare different Machine Learning algorithms.
- Train an XGBoost classification model.
- Build a Flask-based interactive prediction dashboard.
- Store prediction history using SQLite.
- Provide an easy-to-understand fetal health risk classification.

---

## Machine Learning Workflow

```text
CTG Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Correlation Analysis
     ↓
PCA Visualization
     ↓
Feature Importance Analysis
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Model Training
     ↓
Model Comparison
     ↓
XGBoost Model
     ↓
Model Serialization
     ↓
Flask Web Dashboard
