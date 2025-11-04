import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.metrics import (
    confusion_matrix,
    roc_curve,
    auc,
    RocCurveDisplay
)

# Directories
REPORTS_DIR = "reports"
PLOTS_DIR = os.path.join(REPORTS_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

def load_latest_report():
    """Load the most recent training report and prediction file"""
    report_files = [f for f in os.listdir(REPORTS_DIR) if f.startswith("training_report_") and f.endswith(".json")]
    preds_files = [f for f in os.listdir(REPORTS_DIR) if f.startswith("predictions_") and f.endswith(".csv")]

    if not report_files or not preds_files:
        raise FileNotFoundError("No training reports or prediction files found in 'reports/'.")

    # Get latest by timestamp
    latest_report = sorted(report_files)[-1]
    latest_preds = sorted(preds_files)[-1]

    with open(os.path.join(REPORTS_DIR, latest_report), "r") as f:
        metrics = json.load(f)

    preds_df = pd.read_csv(os.path.join(REPORTS_DIR, latest_preds))
    return metrics, preds_df, latest_report, latest_preds

def plot_confusion_matrix(y_true, y_pred, timestamp):
    """Generate and save confusion matrix heatmap"""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")

    path = os.path.join(PLOTS_DIR, f"confusion_matrix_{timestamp}.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"📘 Saved: {path}")

def plot_classification_report(report, timestamp):
    """Visualize precision, recall, and f1-score"""
    df = pd.DataFrame(report).transpose().drop(["accuracy"], errors="ignore")
    df = df[["precision", "recall", "f1-score"]].head(-1)

    df.plot(kind="bar", figsize=(8, 5))
    plt.title("Classification Report")
    plt.ylabel("Score")
    plt.ylim(0, 1)
    plt.legend(loc="lower right")

    path = os.path.join(PLOTS_DIR, f"classification_report_{timestamp}.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"📗 Saved: {path}")

def plot_accuracy_bar(acc, timestamp):
    """Plot accuracy as a simple bar chart"""
    plt.figure(figsize=(4, 5))
    plt.bar(["Accuracy"], [acc], color="green")
    plt.ylim(0, 1)
    plt.title("Model Accuracy")
    plt.text(0, acc / 2, f"{acc:.2%}", ha="center", va="center", color="white", fontsize=12, fontweight="bold")

    path = os.path.join(PLOTS_DIR, f"accuracy_{timestamp}.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"📙 Saved: {path}")

def plot_roc_curve(y_true, y_score, timestamp):
    """Plot and save ROC curve"""
    # Ensure binary classification labels (0/1)
    if len(set(y_true)) != 2:
        print("⚠️ ROC Curve skipped (non-binary classification detected).")
        return

    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC curve (AUC = {roc_auc:.2f})")
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operating Characteristic (ROC Curve)")
    plt.legend(loc="lower right")

    path = os.path.join(PLOTS_DIR, f"roc_curve_{timestamp}.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"📕 Saved: {path}")

if __name__ == "__main__":
    print("📈 Generating model performance visualizations...")
    metrics, preds_df, report_name, preds_name = load_latest_report()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    y_true = preds_df["y_test"]
    y_pred = preds_df["y_pred"]

    # ROC curve requires predicted probabilities — skip if not available
    if "y_score" in preds_df.columns:
        y_score = preds_df["y_score"]
    else:
        # fallback: convert y_pred to 0/1 numeric if possible
        y_score = y_pred.apply(lambda x: 1 if x in [1, "positive", "pos"] else 0)

    y_true_num = y_true.apply(lambda x: 1 if x in [1, "positive", "pos"] else 0)

    # Generate plots
    plot_confusion_matrix(y_true, y_pred, timestamp)
    plot_classification_report(metrics["classification_report"], timestamp)
    plot_accuracy_bar(metrics["accuracy"], timestamp)
    plot_roc_curve(y_true_num, y_score, timestamp)

    print("\n✅ All evaluation visualizations saved successfully!")
