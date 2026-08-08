# Fetal Health Monitoring using Cardiotocography

## About the Project

This project is a Machine Learning based system for predicting fetal health using Cardiotocography (CTG) data.

The model analyzes different CTG parameters and classifies fetal health into three categories:

- Normal
- Suspect
- Pathological

## Machine Learning

The project includes:

- Data preprocessing and cleaning
- Exploratory Data Analysis
- Correlation analysis
- PCA visualization
- Feature selection using Random Forest
- Logistic Regression
- SVM
- Decision Tree
- XGBoost

After comparing the models, XGBoost is used as the final prediction model.

## Web Application

A Flask web application is developed for the project.

The application allows the user to:

- Enter CTG parameters
- Enter a patient ID
- Predict fetal health
- Display the prediction result
- Give a simple recommendation based on the result
- Store and view previous prediction history

SQLite is used to store the patient prediction history.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Flask
- HTML
- SQLite
