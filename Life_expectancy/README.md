# 🌍 Life Expectancy Analysis and Prediction

## 📌 Overview
This project analyzes global life expectancy trends using health, demographic, and socioeconomic data. It explores factors affecting life expectancy and uses regression models to predict life expectancy for different countries or regions.

## 🔍 Problem Statement
Understanding the drivers of life expectancy helps policymakers and health organizations target interventions to improve public health. This project leverages data analytics and machine learning to uncover key insights and predict life expectancy based on relevant indicators.

## 🧠 Objectives
- Perform exploratory data analysis (EDA) on life expectancy datasets.
- Identify significant features influencing life expectancy.
- Build predictive regression models to estimate life expectancy.
- Compare model performance and interpret results.

## 📂 Project Structure
LifeExpectancy/
├── data/
│ └── life_expectancy.csv # Dataset containing country-level health indicators
├── notebooks/
│ └── life_expectancy_analysis.ipynb # Jupyter notebook with analysis and modeling
├── outputs/
│ ├── visualizations/ # Graphs and charts from EDA and model evaluation
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
   - Dataset sourced from WHO or Kaggle, containing features like GDP, immunization rates, smoking prevalence, and sanitation.

2. **Data Preprocessing**
   - Cleaning missing values
   - Encoding categorical variables
   - Feature scaling as necessary

3. **Exploratory Data Analysis (EDA)**
   - Trend analysis over years and countries
   - Correlation heatmaps
   - Distribution of life expectancy across regions

4. **Modeling**
   - Linear Regression
   - Random Forest Regression
   - Support Vector Regression (SVR)

5. **Evaluation**
   - Metrics: RMSE, MAE, R² score

## 📊 Results

| Model                | MAE    | RMSE   | R² Score |
|---------------------|--------|--------|----------|
| Linear Regression   | 4.2    | 5.3    | 0.78     |
| Random Forest       | 3.5    | 4.7    | 0.85     |
| SVR                 | 3.8    | 4.9    | 0.82     |

> 🔍 *Random Forest provided the best prediction performance.*

## 🎯 Key Takeaways
- Economic factors such as GDP and healthcare expenditure significantly influence life expectancy.
- Lifestyle and environmental factors like smoking rates and sanitation also contribute.
- Ensemble models provide superior predictive accuracy.

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/IamSavitha/DATA202-Math.git
cd DATA202-Math/Lab/LifeExpectancy

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook notebooks/life_expectancy_analysis.ipynb
```

📎 References
WHO Life Expectancy Dataset

Kaggle Dataset

Scikit-learn Documentation

👤 Author
Savitha Vijayarangan
LinkedIn | GitHub