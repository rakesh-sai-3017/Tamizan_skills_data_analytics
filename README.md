# 📈 Sales Forecasting with Linear Regression

## 🧠 Problem Statement
Businesses often struggle to estimate future sales based on past performance. This project uses a simple yet effective linear regression model to forecast future sales using historical sales data.

---

## 🎯 Objective
Build a regression model to predict future revenue based on historical sales data using Python and visualize the predictions.

---

## 📂 Dataset
A CSV file containing:
- `Date`: Transaction date
- `Product`: Product name
- `Quantity`: Number of units sold
- `Revenue`: Total revenue for the transaction

---

## ⚙️ Technologies Used
- Python 🐍
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## 🛠️ Project Workflow

1. **Data Preprocessing**
   - Handling missing values
   - Aggregating data monthly

2. **Model Building**
   - Linear Regression using Scikit-learn

3. **Model Evaluation**
   - Mean Squared Error (MSE)
   - R² Score

4. **Forecasting & Visualization**
   - Plot actual vs predicted sales
   - Tabular view of forecast

---

## 📊 Output

- 📅 Monthly Sales Forecast
- 📈 Line Plot: Actual vs Predicted Revenue
- 📋 Tabular Forecast Data


## 💡 Future Scope
- Include seasonality and holiday effects
- Use advanced forecasting models (ARIMA, LSTM)
- Build a Power BI Dashboard for business visualization



# 🎓 Student Performance Analytics Dashboard

An interactive Streamlit dashboard for analyzing student performance data, identifying trends, and detecting at-risk students based on their marks, attendance, and login activity.

---

## 🧠 Problem Statement

Educational institutions need data-driven systems to detect early signs of academic risk such as low grades or absenteeism. This project aims to provide insights through a visual dashboard.

---

## 🎯 Objective

Develop a user-friendly dashboard to:
- Monitor academic performance
- Correlate attendance, marks, and engagement
- Highlight students who may need academic support

---

## 📊 Features

- 📌 **Summary Statistics**: Average marks, attendance, and logins  
- 📈 **Visualizations**:
  - Bar Chart: Marks distribution
  - Heatmap: Correlation matrix between performance metrics
  - Scatter Plot: Attendance vs Marks
- ⚠️ **Risk Filter**: View students below performance thresholds

---

## 📁 Dataset

`student_data.csv` with the following columns:

| Column Name | Description                       |
|-------------|-----------------------------------|
| Name        | Student name                      |
| Marks       | Academic score (0–100)            |
| Attendance  | Attendance percentage (0–100%)    |
| Logins      | Number of platform logins         |

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas
- Seaborn
- Matplotlib
- Streamlit

---

## 🚀 How to Run

1. Clone the repository or download the files  
2. Install required libraries:

``bash
pip install pandas streamlit seaborn matplotlib

##Run the app:

``bash
streamlit run students_dashboard.py

##Open browser at: http://localhost:8501

 ##Project Structure
Student_Analytics/
├── students_dashboard.py       # Streamlit app script
├── student_data.csv            # Sample dataset
└── README.md                   # Project documentation


# 🦠 COVID-19 Data Analysis & Visualization Project

This project provides a data-driven analysis and visualization of COVID-19 trends across multiple countries. It helps understand the spread of the virus, compare infection and death rates, and visualize the impact over time.

---

## 📌 Objective

- Analyze global COVID-19 data to understand trends and patterns.
- Compare total cases and deaths across countries.
- Visualize daily and cumulative statistics using various plot types.

---

## 📁 Dataset

- Filename: `covid_extended_data.csv`
- Format: CSV
- Fields:
  - `date`: Date of record
  - `location`: Country name
  - `total_cases`: Cumulative number of confirmed cases
  - `new_cases`: Daily new confirmed cases
  - `total_deaths`: Cumulative number of deaths
  - `new_deaths`: Daily new deaths
  - `population`: Total population of the country

> **Note:** Data in this project is a simplified sample for learning purposes. You can extend it using real-world datasets from OWID or Johns Hopkins.

---

## 📊 Visualizations Included

- 📈 **Line Plot** — Total cases over time for multiple countries
- 📊 **Area Chart** — Country-specific analysis of cases vs deaths (India)
- 🔥 **Heatmap** — Compare total cases across countries on the latest date
- 📋 **Printed Summary** — Death rates and country-wise statistics

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- VS Code

---

## ▶️ How to Run the Project

1. Clone the repository or download the files.
2. Make sure `covid_extended_data.csv` is in the same folder as `covid_analytics.py`.
3. Install the required Python libraries:

``bash
pip install pandas matplotlib seaborn

##Run the script:
python covid_analytics.py

✅ Future Improvements
Add vaccination and recovery stats.

Use real-world datasets with more countries and longer date ranges.

Build an interactive dashboard using Plotly, Dash, or Power BI.

Perform trend forecasting using time series models (ARIMA, Prophet).

