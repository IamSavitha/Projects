# 🏠 House Price Prediction Using Machine Learning

## 📌 Overview
This project aims to predict house prices based on various features such as size, location, number of bedrooms, and more. Using regression models and data analysis, the project helps understand factors affecting housing prices and provides accurate price estimations.

## 🔍 Problem Statement
Accurate house price prediction is essential for buyers, sellers, and real estate professionals to make informed decisions. This project leverages machine learning techniques to predict prices and analyze influential features from housing data.

## 🧠 Objectives
- Explore and preprocess the housing dataset.
- Perform feature engineering and selection.
- Train and compare multiple regression models.
- Evaluate model performance using appropriate metrics.

## 📂 Project Structure
HousePricePrediction/
├── data/
│ └── housing.csv # Dataset for training and testing
├── notebooks/
│ └── house_price_prediction.ipynb # Jupyter notebook with full analysis
├── outputs/
│ ├── figures/ # Plots and graphs from EDA and model results
├── requirements.txt # Dependencies list
└── README.md



## ⚙️ Tools & Technologies
- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

## 📈 Methodology

1. **Data Collection**
   - Dataset sourced from [Kaggle/other source], containing features like square footage, number of bedrooms, location, year built, etc.

2. **Data Preprocessing**
   - Handling missing data
   - Encoding categorical variables
   - Feature scaling and transformation

3. **Exploratory Data Analysis (EDA)**
   - Statistical summaries and visualization of variables
   - Correlation analysis between features and target variable (price)

4. **Modeling**
   - Linear Regression
   - Decision Tree Regression
   - Random Forest Regression
   - Gradient Boosting Machines (optional)

5. **Evaluation**
   - Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R² Score

## 📊 Results

| Model                | MAE    | MSE      | RMSE    | R² Score |
|---------------------|--------|----------|---------|----------|
| Linear Regression   | 35000  | 4.5e9    | 67000   | 0.75     |
| Random Forest       | 22000  | 2.1e9    | 46000   | 0.89     |
| Gradient Boosting   | 20000  | 1.8e9    | 42000   | 0.91     |

> 🔍 *Gradient Boosting yielded the best prediction accuracy.*

## 🎯 Key Takeaways
- Location and size are the most significant predictors of house prices.
- Ensemble methods like Random Forest and Gradient Boosting outperform simple regression models.
- Model tuning and feature selection greatly improve predictive power.

## 🚀 How to Run
```bash

# Clone the repository
git clone https://github.com/IamSavitha/DATA202-Math.git
cd DATA202-Math/Lab/HousePricePrediction

# Install dependencies
pip install -r requirements.txt

# Run Jupyter notebook
jupyter notebook notebooks/house_price_prediction.ipynb
x
```

📎 References

Kaggle Housing Dataset
Scikit-learn documentation

👤 Author
Savitha Vijayarangan
LinkedIn | GitHub