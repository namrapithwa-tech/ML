# Diabetes Prediction Project

## Overview
This project focuses on predicting diabetes outcomes using a machine learning model. The project uses the **diabetes.csv** dataset for training and evaluation. The model is serialized and saved as **model_pickle** for reuse. The analysis, model training, and evaluation are documented in the Jupyter notebook **Lab6.ipynb**.

The aim is to provide a streamlined approach for predicting diabetes, which could support healthcare professionals in decision-making processes.

---

## Features
- Data preprocessing and exploratory data analysis (EDA) using Python.
- Training and evaluation of a machine learning model.
- Model serialization for deployment and reuse.
- Comprehensive documentation of the workflow in a Jupyter Notebook.

---

## Files
1. **diabetes.csv**: Contains the dataset used for training and evaluation. This file includes features like glucose levels, blood pressure, and BMI, among others.
2. **Lab6.ipynb**: A Jupyter Notebook with detailed steps for data analysis, preprocessing, model training, and evaluation.
3. **model_pickle**: Serialized machine learning model, saved for deployment or reuse without retraining.

---

## Prerequisites
### Required Libraries
Ensure you have the following Python libraries installed:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

Install missing libraries using pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn notebook
```

---

## Usage

### 1. Data Exploration and Model Training
1. Open **Lab6.ipynb** in Jupyter Notebook:
   ```bash
   jupyter notebook Lab6.ipynb
   ```
2. Run the cells step by step to:
   - Explore the dataset.
   - Preprocess the data.
   - Train the machine learning model.
   - Evaluate the model's performance.

### 2. Loading the Serialized Model
To reuse the trained model, load the **model_pickle** file in your Python environment:
```python
import pickle

# Load the model
with open('model_pickle', 'rb') as file:
    model = pickle.load(file)

# Example prediction
sample_data = [[5, 116, 74, 0, 0, 25.6, 0.201, 30]]  # Replace with real data
prediction = model.predict(sample_data)
print("Diabetes Prediction:", prediction)
```

---

## Dataset Information
The **diabetes.csv** dataset includes the following features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (0 = No Diabetes, 1 = Diabetes)

---

## Model
The project employs a supervised learning algorithm. The notebook covers the model's training process, including hyperparameter tuning and evaluation metrics.

---

## Contributions
Feel free to contribute to the project by improving the model, adding new features, or optimizing the workflow. Open a pull request with detailed descriptions of your changes.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- **Dataset**: [Kaggle Diabetes Dataset](https://www.kaggle.com/)
- Special thanks to the Python and machine learning community for providing excellent resources and tools.
