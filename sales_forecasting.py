# Sales Forecasting with Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the data
df = df = pd.read_csv(r"C:\Users\rakes\OneDrive\Desktop\Rakesh Projects\Stock_Prediction\sales_data.csv")


# Step 2: Preprocess the data
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Step 3: Aggregate data monthly (or change to 'W' for weekly)
df_monthly = df.resample('M', on='Date').sum().reset_index()

# Step 4: Feature Engineering
df_monthly['Month'] = df_monthly['Date'].dt.month
df_monthly['Year'] = df_monthly['Date'].dt.year

# Step 5: Prepare data for regression
X = df_monthly[['Month', 'Year']]
y = df_monthly['Revenue']

# Step 6: Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Step 7: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Step 10: Plot actual vs predicted
plt.figure(figsize=(10,5))
plt.plot(df_monthly['Date'][-len(y_test):], y_test, label='Actual Sales', marker='o')
plt.plot(df_monthly['Date'][-len(y_test):], y_pred, label='Predicted Sales', linestyle='--', marker='x')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 11: Output forecast table
forecast_df = pd.DataFrame({
    'Date': df_monthly['Date'][-len(y_test):],
    'Actual Revenue': y_test.values,
    'Predicted Revenue': y_pred
})

print("\nForecast Table:")
print(forecast_df)
