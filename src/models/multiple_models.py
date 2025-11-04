import os
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Paths
INTERIM_DIR = "data/interim"
REPORTS_DIR = "reports"
MODELS_DIR = "models"

os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

def load_data():
    X_train, y_train = joblib.load(os.path.join(INTERIM_DIR, "train_data.pkl"))
    X_test, y_test = joblib.load(os.path.join(INTERIM_DIR, "test_data.pkl"))
    return X_train, X_test, y_train, y_test

def save_report(model_name, y_true, y_pred, acc):
    report = classification_report(y_true, y_pred, output_dict=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    pd.DataFrame(report).to_csv(
        os.path.join(REPORTS_DIR, f"{model_name}_classification_report_{timestamp}.csv")
    )

    with open(os.path.join(REPORTS_DIR, f"{model_name}_accuracy_{timestamp}.txt"), "w") as f:
        f.write(f"Accuracy: {acc:.4f}\n")

def train_and_evaluate():
    print("🚀 Starting training for multiple models...\n")
    X_train, X_test, y_train, y_test = load_data()

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", random_state=42)
    }

    # Encode labels for XGBoost
    le = LabelEncoder()
    y_train_enc = le.fit_transform(y_train)
    y_test_enc = le.transform(y_test)

    for name, model in models.items():
        print(f"🔹 Training {name}...")
        if name == "XGBoost":
            model.fit(X_train, y_train_enc)
            y_pred_enc = model.predict(X_test)
            y_pred = le.inverse_transform(y_pred_enc)
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"✅ {name} Accuracy: {acc:.4f}")

        # Save model
        joblib.dump(model, os.path.join(MODELS_DIR, f"{name}_model_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pkl"))

        # Save evaluation
        save_report(name, y_test, y_pred, acc)
        print(f"✅ {name} evaluation saved!\n")

if __name__ == "__main__":
    train_and_evaluate()
