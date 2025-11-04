import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from src.utils.text_utils import preprocess_text
import os


def build_features(input_path="data/processed/amazon_reviews_clean.csv",
                   output_dir="data/interim"):
    """Preprocess text and extract TF-IDF features"""

    print("📥 Loading cleaned dataset...")
    df = pd.read_csv(input_path)
    df.dropna(subset=["review_text", "sentiment"], inplace=True)

    print("🧹 Preprocessing text...")
    df["cleaned_text"] = df["review_text"].apply(preprocess_text)

    print("🔢 Converting text to TF-IDF features...")
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = tfidf.fit_transform(df["cleaned_text"])
    y = df["sentiment"]

    print("✂️ Splitting train/test data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    os.makedirs(output_dir, exist_ok=True)

    # save TF-IDF model and datasets
    with open(os.path.join(output_dir, "tfidf_vectorizer.pkl"), "wb") as f:
        pickle.dump(tfidf, f)
    with open(os.path.join(output_dir, "train_data.pkl"), "wb") as f:
        pickle.dump((X_train, y_train), f)
    with open(os.path.join(output_dir, "test_data.pkl"), "wb") as f:
        pickle.dump((X_test, y_test), f)

    print("✅ Features built and saved successfully!")
    print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")


if __name__ == "__main__":
    build_features()
