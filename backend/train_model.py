# train_model.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib

# ------------------- Load dataset -------------------
data_path = "data/creditcard.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError("Dataset not found. Please put creditcard.csv in the data/ folder.")

df = pd.read_csv(data_path)

# Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train-test split (stratify ensures same proportion of fraud/non-fraud)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------- Balance training set -------------------
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

print(f"Original training set shape: {X_train.shape}, {y_train.shape}")
print(f"Balanced training set shape: {X_res.shape}, {y_res.shape}")

# ------------------- Train Random Forest -------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_res, y_res)

# ------------------- Evaluate -------------------
y_pred = model.predict(X_test)
print("Classification report on test set:")
print(classification_report(y_test, y_pred))

# ------------------- Save model and feature order -------------------
os.makedirs("models", exist_ok=True)
model_path = "models/rf_model_balanced.pkl"
features_path = "models/features.pkl"

joblib.dump(model, model_path)
joblib.dump(X_res.columns.tolist(), features_path)

print(f"Balanced model saved at {model_path}")
print(f"Feature order saved at {features_path}")

