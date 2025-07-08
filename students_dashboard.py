# student_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit Config
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Load Dataset
file_path = r"C:\Users\rakes\OneDrive\Desktop\Rakesh Projects\Stock_prediction\students_analytics\student_data.csv"

df = pd.read_csv(file_path)
df = df.ffill()

# Title
st.title("🎓 Student Performance Analytics Dashboard")

# Metrics
st.subheader("📊 Average Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Marks", f"{df['Marks'].mean():.2f}")
col2.metric("Average Attendance", f"{df['Attendance'].mean():.2f}%")
col3.metric("Average Logins", f"{df['Logins'].mean():.0f}")

# Risk Tagging
df['Risk'] = df.apply(lambda x: 'High' if x['Marks'] < 50 or x['Attendance'] < 60 else 'Low', axis=1)

# Sidebar Filters
st.sidebar.header("📌 Filters")
selected_risk = st.sidebar.multiselect("Select Risk Level", options=df['Risk'].unique(), default=df['Risk'].unique())

# Filtered Data
filtered_df = df[df['Risk'].isin(selected_risk)]

# Bar Plot - Marks Ranking
st.subheader("🏅 Student Marks Ranking")
fig1, ax1 = plt.subplots(figsize=(12,5))
sns.barplot(x='Name', y='Marks', data=filtered_df.sort_values(by='Marks', ascending=False), palette='coolwarm', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Heatmap - Correlation
st.subheader("🔗 Correlation Between Metrics")
fig2, ax2 = plt.subplots()
sns.heatmap(df[['Marks', 'Attendance', 'Logins']].corr(), annot=True, cmap='YlGnBu', ax=ax2)
st.pyplot(fig2)

# Scatter Plot - Attendance vs Marks
st.subheader("📉 Attendance Impact on Marks")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Attendance', y='Marks', hue='Risk', style='Risk', s=100, ax=ax3)
st.pyplot(fig3)

# Scatter Plot - Logins vs Marks
st.subheader("💻 Logins Impact on Marks")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Logins', y='Marks', hue='Risk', style='Risk', s=100, ax=ax4)
st.pyplot(fig4)

# Table - At-Risk Students
st.subheader("⚠️ High-Risk Students")
st.dataframe(df[df['Risk'] == 'High'][['Student_ID', 'Name', 'Marks', 'Attendance', 'Logins']])
