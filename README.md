# 🚀 Credit Score Prediction with Machine Learning

## 📋 Description

This project builds machine learning models in Python to predict customer credit scores based on demographic and behavioral data. It uses the Random Forest and K-Nearest Neighbors (KNN) algorithms to train on labeled data and then predicts scores for new customers.

## 🛠️ Technologies Used

- Python 3  
- Pandas — data manipulation  
- Scikit-learn — machine learning models and preprocessing  

## ⚙️ How It Works

- 📥 Loads customer data from CSV files.  
- 🔄 Encodes categorical features into numerical values using LabelEncoder.  
- 🧑‍🏫 Splits the dataset into training and test sets.  
- 🌲 Trains Random Forest and KNN classifiers to predict credit scores.  
- 📊 Evaluates model accuracy using the test set.  
- 🔮 Predicts credit scores for new customers based on the trained model.

## ✅ Setup Instructions

### 📌 Prerequisites

- Python 3 installed on your system

### 🧱 Environment Setup

1. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # Linux / MacOS
venv\Scripts\activate       # Windows
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Run the main Python script to train models and predict credit scores:

```bash
python main.py
```
