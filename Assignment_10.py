

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([35, 42, 50, 58, 65, 71, 78, 83, 90, 96])

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict test values
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Marks per hour (Slope): {model.coef_[0]:.2f}")
print(f"Base marks (Intercept): {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R2 Score: {r2:.4f}")

# Predict marks for 7.5 hours
new_hours = np.array([[7.5]])
predicted_marks = model.predict(new_hours)

print(f"Predicted Marks for 7.5 hours: {predicted_marks[0]:.1f}/100")
