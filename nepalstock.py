"""
This module contains functions for analyzing stock data from Nepal Stock Exchange.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('/workspaces/codespaces-jupyter/data/atlantis.csv')
data.head()
data.info()
data.isnull().sum()
data.head()
# Remove any unnecessary columns
data = data.drop(columns=['BUSINESS DATE'])

# Handling missing values
data = data.dropna()

# Split the data into independent and dependent variables
X = data.drop(columns=['CLOSE PRICE'])
y = data['CLOSE PRICE']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_test)

# Evaluate the model's performance
print('MSE:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))

# Make predictions on new data
new_data = np.array([[100, 200, 300, 400, 500]])
new_data = scaler.transform(new_data)
prediction = regressor.predict(new_data)
print('Prediction:', prediction)
