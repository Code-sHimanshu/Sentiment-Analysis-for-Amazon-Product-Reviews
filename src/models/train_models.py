import os
import joblib
import json
import pandas as pd
import pickle
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV

# Paths
PROCESSED_DATA_DIR = "data/processed"
MODEL_DIR = "models"
REPORTS_DIR = "reports"
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def load_features():
    print("📦 Loading TF-IDF features and data splits...")
    processed_dir = "data/interim"

    # Load TF-IDF vectorizer
    with open(os.path.join(processed_dir, "tfidf_vectorizer.pkl"), "rb") as f:
        tfidf = pickle.load(f)

    # Load training data
    with open(os.path.join(processed_dir, "train_data.pkl"), "rb") as f:
        X_train, y_train = pickle.load(f)

    # Load test data
    with open(os.path.join(processed_dir, "test_data.pkl"), "rb") as f:
        X_test, y_test = pickle.load(f)

    print("✅ Features and vectorizer loaded successfully!")
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    print("🤖 Training Logistic Regression model with hyperparameter tuning...")
    params = {
        "C": [0.1, 1, 10],
        "penalty": ["l2"],
        "solver": ["liblinear"]
    }
    grid = GridSearchCV(LogisticRegression(max_iter=1000), param_grid=params, cv=3, n_jobs=-1, verbose=1)
    grid.fit(X_train, y_train)
    print(f"✅ Best Parameters: {grid.best_params_}")
    return grid.best_estimator_, grid.best_params_

def evaluate_model(model, X_test, y_test):
    print("📊 Evaluating model performance...")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred).tolist()

    print(f"✅ Accuracy: {acc:.4f}\n")
    print("🔍 Classification Report:\n", classification_report(y_test, y_pred))
    print("🧩 Confusion Matrix:\n", cm)
    return acc, report, cm, y_pred

def save_outputs(model, best_params, acc, report, cm, y_test, y_pred):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save model
    model_path = os.path.join(MODEL_DIR, f"sentiment_model_{timestamp}.pkl")
    joblib.dump(model, model_path)

    # Save metrics
    metrics_path = os.path.join(REPORTS_DIR, f"training_report_{timestamp}.json")
    metrics = {
        "timestamp": timestamp,
        "best_params": best_params,
        "accuracy": acc,
        "classification_report": report,
        "confusion_matrix": cm
    }
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    # Save predictions
    preds_path = os.path.join(REPORTS_DIR, f"predictions_{timestamp}.csv")
    pd.DataFrame({
        "y_test": y_test,
        "y_pred": y_pred
    }).to_csv(preds_path, index=False)

    print(f"\n💾 Model saved at: {model_path}")
    print(f"📊 Training report saved at: {metrics_path}")
    print(f"🧾 Predictions saved at: {preds_path}")

if __name__ == "__main__":
    print("🚀 Starting model training process...")
    X_train, X_test, y_train, y_test = load_features()
    model, best_params = train_model(X_train, y_train)
    acc, report, cm, y_pred = evaluate_model(model, X_test, y_test)
    save_outputs(model, best_params, acc, report, cm, y_test, y_pred)
    print("🎉 Training complete!")
