# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import os

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Load trained model -------------------
MODEL_PATH = "models/rf_model_balanced.pkl"
FEATURES_PATH = "models/features.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
if not os.path.exists(FEATURES_PATH):
    raise FileNotFoundError(f"Feature list not found at {FEATURES_PATH}")

model = joblib.load(MODEL_PATH)
FEATURES = joblib.load(FEATURES_PATH)  # exact feature order

# ------------------- Prediction endpoint -------------------
@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()

        # Normalize keys: lowercase or capitalized
        normalized = {}
        for feature in FEATURES:
            if feature in data:
                normalized[feature] = float(data[feature])
            elif feature.lower() in data:
                normalized[feature] = float(data[feature.lower()])
            else:
                # Missing features set to 0
                normalized[feature] = 0.0

        # Convert to DataFrame with correct column order
        input_df = pd.DataFrame([normalized], columns=FEATURES)

        # Predict fraud probability
        fraud_prob = float(model.predict_proba(input_df)[:, 1][0])
        is_fraud = fraud_prob > 0.5

        return {"fraud_probability": fraud_prob, "is_fraud": is_fraud}

    except Exception as e:
        print("Error in /predict:", e)
        raise HTTPException(status_code=500, detail="Prediction failed")



