# COVID-19 Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\rakes\OneDrive\Desktop\Rakesh Projects\Stock_prediction\covid_analsis\covid_extended_data.csv")

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Display basic info
print("Dataset Info:")
print(df.info())
print("\nUnique Countries:")
print(df['location'].unique())

# Latest date in dataset
latest_date = df['date'].max()

# Summary for latest date
print(f"\nSummary on {latest_date.date()}:")
latest_data = df[df['date'] == latest_date]
print(latest_data[['location', 'total_cases', 'total_deaths']])

# Line Plot: Total Cases over Time for All Countries
plt.figure(figsize=(12, 6))
countries = df['location'].unique()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Area Chart for India: Total Cases and Deaths
plt.figure(figsize=(10, 5))
india_data = df[df['location'] == "India"]
india_data.set_index("date")[['total_cases', 'total_deaths']].plot(kind='area', stacked=True, alpha=0.4)
plt.title("COVID-19 in India: Cases vs Deaths")
plt.ylabel("Count")
plt.xlabel("Date")
plt.tight_layout()
plt.show()

# Heatmap of Total Cases for Each Country on Latest Date
plt.figure(figsize=(8, 6))
heatmap_data = latest_data.pivot_table(index='location', values='total_cases')
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="Reds")
plt.title(f"Total Cases by Country on {latest_date.date()}")
plt.tight_layout()
plt.show()

# Calculate and Display Death Rate
df['death_rate'] = (df['total_deaths'] / df['total_cases']) * 100
death_rates = df[df['date'] == latest_date][['location', 'death_rate']]
print("\nDeath Rates on Latest Date:")
print(death_rates.sort_values(by='death_rate', ascending=False))

# Optional: Save Processed Data
df.to_csv("processed_covid_data.csv", index=False)
print("\nProcessed data saved as 'processed_covid_data.csv'")
