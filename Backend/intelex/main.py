from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
from timeit import default_timer as timer
from sklearnex import patch_sklearn

patch_sklearn()

# Load your dataset (assuming it is in CSV format)
df = pd.read_csv('crop_yield.csv')

# Sample 20,000 rows from the dataset (randomly)
df_sampled = df.sample(n=50000, random_state=42)

# Define the features and the target variable
X = df_sampled.drop('Yield_tons_per_hectare', axis=1)  # Features
y = df_sampled['Yield_tons_per_hectare']  # Target

# Convert categorical variables to numerical values using one-hot encoding
X = pd.get_dummies(X, columns=['Region', 'Soil_Type', 'Crop', 'Weather_Condition'], drop_first=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

start_rf = timer()
rf_model.fit(X_train, y_train)
train_time_rf = timer() - start_rf
print(f"Random Forest Training time: {train_time_rf:.2f} seconds")

# Make predictions and evaluate the Random Forest model
y_pred_rf = rf_model.predict(X_test)

# Calculate Mean Squared Error (MSE) for Random Forest
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print(f"Random Forest Mean Squared Error: {mse_rf:.2f}")
print(f"Random Forest Accuracy : {r2_rf:.2f}")

# Export the trained Random Forest model to a pickle file
with open('crop_yield_random_forest_model.pkl', 'wb') as file:
    pickle.dump(rf_model, file)

# Train the Linear Regression model
lin_model = LinearRegression()

start_lin = timer()
lin_model.fit(X_train, y_train)
train_time_lin = timer() - start_lin
print(f"Linear Regression Training time: {train_time_lin:.2f} seconds")

# Make predictions and evaluate the Linear Regression model
y_pred_lin = lin_model.predict(X_test)

# Calculate Mean Squared Error (MSE) for Linear Regression
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)
print(f"Linear Regression Mean Squared Error: {mse_lin:.2f}")
print(f"Linear Regression Accuracy : {r2_lin:.2f}")

# Export the trained Linear Regression model to a pickle file
with open('crop_yield_linear_regression_model.pkl', 'wb') as file:
    pickle.dump(lin_model, file)

# Compare the performance of both models
print("\nPerformance Comparison:")
print(f"Random Forest MSE: {mse_rf:.2f}, Accuracy : {r2_rf:.2f}")
print(f"Linear Regression MSE: {mse_lin:.2f}, Accuracy : {r2_lin:.2f}")
