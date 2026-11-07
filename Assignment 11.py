
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Create dummy categorical data
data = {
    'Age Group': ['Youth', 'Middle-Aged', 'Senior', 'Youth', 'Senior', 'Middle-Aged'],
    'Income': ['High', 'High', 'Medium', 'Low', 'Low', 'Medium'],
    'Student': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes'],
    'Purchased': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Separate features (X) and target label (y)
X = df.drop(columns=['Purchased'])
y = df['Purchased']

# Split into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Preprocessing: Apply One-Hot Encoding
categorical_features = ['Age Group', 'Income', 'Student']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# 3. Build a scikit-learn Pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 4. Train the model
model_pipeline.fit(X_train, y_train)

# 5. Predict on test set
y_pred = model_pipeline.predict(X_test)

# 6. Evaluate results
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",
      classification_report(y_test, y_pred, zero_division=0))
