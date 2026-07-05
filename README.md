# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project predicts whether a person is at risk of developing heart disease within the next 10 years using Machine Learning classification algorithms.

The project uses the **Framingham Heart Study Dataset** and compares the performance of multiple classification models to identify the best-performing algorithm.

---

## 🎯 Project Objective

The objective of this project is to build a machine learning model that can accurately predict the risk of heart disease based on patient health information. Such predictions can help in early diagnosis and preventive healthcare.

---

## 📂 Dataset

- **Dataset:** Framingham Heart Study Dataset
- **Target Variable:** `TenYearCHD`

### Features Used

- Gender
- Age
- Current Smoker
- Cigarettes Per Day
- Blood Pressure Medication
- Prevalent Stroke
- Prevalent Hypertension
- Diabetes
- Total Cholesterol
- Systolic Blood Pressure
- Diastolic Blood Pressure
- BMI
- Glucose Level

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 📚 Machine Learning Algorithms

The following models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

---

## 🔄 Project Workflow

1. Import Required Libraries
2. Load Dataset
3. Data Cleaning
4. Handle Missing Values
5. Drop Unnecessary Columns
6. Exploratory Data Analysis (EDA)
7. Correlation Heatmap
8. Feature Selection
9. Train-Test Split
10. Feature Scaling using StandardScaler
11. Train Multiple Machine Learning Models
12. Compare Model Accuracy
13. Generate Classification Report
14. Plot Confusion Matrix
15. Predict Heart Disease for New Patient Data
16. Save Trained Model using Joblib

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Removed missing values
- Removed unnecessary columns:
  - education
  - heartRate
  - BPMeds
- Feature Scaling using StandardScaler
- Train-Test Split (70% Training, 30% Testing)

---

## 📈 Model Evaluation

Evaluation metrics used:

- Accuracy Score
- Classification Report
- Confusion Matrix

The project compares multiple machine learning algorithms and selects the best-performing model.

---

## 🧠 Sample Prediction

The model predicts:

- ✅ No Heart Disease
- ❤️ Heart Disease Risk

It also provides the prediction probability using:

```python
predict_proba()
```

---

## 💾 Saved Model

The trained model is saved as:

- `heart_disease_model.pkl`

Scaler file:

- `scale.pkl`

These files can be used later for deployment without retraining the model.

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── ML_Project.ipynb
├── framingham.csv
├── heart_disease_model.pkl
├── scale.pkl
├── README.md
└── images/
    ├── heatmap.png
    ├── confusion_matrix.png
    └── countplot.png
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

Run the notebook:

```bash
jupyter notebook
```

---

## 📷 Project Screenshots

### Correlation Heatmap

_Add screenshot here_

```markdown
![Heatmap](images/heatmap.png)
```

### Confusion Matrix

```markdown
![Confusion Matrix](images/confusion_matrix.png)
```

### Target Variable Distribution

```markdown
![Countplot](images/countplot.png)
```

---

## 🔮 Future Improvements

- Deploy the model using Streamlit or Flask
- Improve accuracy using Hyperparameter Tuning
- Handle class imbalance using SMOTE
- Perform Feature Engineering
- Build a user-friendly web interface

---

## 👩‍💻 Author

**Sayali Korlekar**

Aspiring Data Analyst | Machine Learning Enthusiast

---

## ⭐ If you found this project useful, please consider giving it a star!
