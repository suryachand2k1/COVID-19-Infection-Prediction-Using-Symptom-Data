# COVID-19 Prediction Project

## Overview
This project uses advanced machine learning algorithms to predict COVID-19 infections from symptom data. It focuses on the application of various predictive models to analyze symptoms and demographic data, aiming to correlate these factors with COVID-19 test results.

## Dataset
- `data.csv`: Contains raw data with features like cough, fever, sore throat, shortness of breath, headache, age, gender, and test indication.
- `data_processed.csv`: Preprocessed data, formatted for input into machine learning models.

## Technical Features
- **Data Preprocessing:** Includes cleaning, normalization, and handling of missing values.
- **Feature Engineering:** Enhancement and selection of relevant features for improved model accuracy.
- **Machine Learning Models:** 
  - Logistic Regression: For baseline predictions and probability estimation.
  - Decision Trees: To capture non-linear relationships in data.
  - Random Forest: An ensemble method for improved accuracy and overfitting control.
  - Neural Networks: Advanced modeling to capture complex patterns in data.
  - Support Vector Machines (SVM): For high-dimensional data classification.
- **Model Evaluation:** Uses accuracy, precision, recall, F1 score, and ROC-AUC to evaluate model performance.

## File Structure
- `app.py`: Main application script for executing the predictive model.
- `Notebook.ipynb`: Detailed Jupyter Notebook for data analysis, model development, and evaluation.
- `data.csv`: Original dataset with raw symptom and test data.
- `data_processed.csv`: Dataset processed for machine learning model input.

## Installation & Usage
1. Ensure Python and necessary libraries (`numpy`, `pandas`, `scikit-learn`, `tensorflow`, etc.) are installed.
2. Execute `python app.py` for model prediction.
3. Explore `Notebook.ipynb` for a step-by-step analysis and model training process.

## Dependencies
- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- TensorFlow/Keras (for Neural Networks)

