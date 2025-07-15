# 🎬 Movie Recommendation System Using Collaborative Filtering

## 📌 Overview
This project develops a movie recommendation system that suggests movies to users based on their preferences and past ratings. Using collaborative filtering techniques, it aims to provide personalized recommendations and improve user experience on streaming platforms.

## 🔍 Problem Statement
With thousands of movies available, users often struggle to find movies they will enjoy. Recommendation systems help by predicting user preferences based on historical data. This project builds a collaborative filtering model to recommend movies effectively.

## 🧠 Objectives
- Analyze user rating data to understand preferences.
- Implement collaborative filtering algorithms.
- Evaluate the recommendation system’s accuracy.
- Explore potential improvements with hybrid methods.

## 📂 Project Structure
MovieRecommendation/
├── data/
│ ├── movies.csv # Movie metadata
│ └── ratings.csv # User ratings dataset
├── notebooks/
│ └── movie_recommendation.ipynb # Jupyter notebook with analysis and modeling
├── outputs/
│ ├── visualizations/ # Plots related to data and model evaluation
├── requirements.txt # Python dependencies
└── README.md


## ⚙️ Tools & Technologies
- Python 3.x
- Pandas, NumPy
- Scikit-learn, Surprise library
- Matplotlib, Seaborn
- Jupyter Notebook

## 📈 Methodology

1. **Data Collection**
   - Dataset from [MovieLens](https://grouplens.org/datasets/movielens/) or similar source containing user ratings and movie metadata.

2. **Data Preprocessing**
   - Handling missing values
   - Data transformation and normalization

3. **Exploratory Data Analysis (EDA)**
   - Distribution of movie ratings
   - Popularity analysis of movies and users
   - Visualization of rating patterns

4. **Modeling**
   - User-based Collaborative Filtering
   - Item-based Collaborative Filtering
   - Matrix Factorization (e.g., SVD)

5. **Evaluation**
   - Metrics: RMSE, MAE
   - Cross-validation to test generalization

## 📊 Results

| Model                      | RMSE   | MAE    |
|----------------------------|--------|--------|
| User-based CF              | 0.88   | 0.68   |
| Item-based CF              | 0.86   | 0.65   |
| Matrix Factorization (SVD) | 0.82   | 0.62   |

> 🔍 *Matrix Factorization using SVD performed best in predicting user ratings.*

## 🎯 Key Takeaways
- Collaborative filtering effectively captures user preferences.
- Matrix factorization techniques improve recommendation accuracy.
- Data sparsity and cold-start problems remain challenges to address.

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/IamSavitha/DATA202-Math.git
cd DATA202-Math/Lab/MovieRecommendation

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/movie_recommendation.ipynb
```


📎 References
MovieLens Dataset

Surprise Library Documentation

Scikit-learn Documentation

👤 Author
Savitha Vijayarangan
LinkedIn | GitHub

