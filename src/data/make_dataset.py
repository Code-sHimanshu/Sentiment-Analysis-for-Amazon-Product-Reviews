# src/data/make_dataset.py

import os
import pandas as pd

def load_raw_data(raw_dir="data/raw"):
    """Load and combine all CSV files from raw directory"""
    all_files = [os.path.join(raw_dir, f) for f in os.listdir(raw_dir) if f.endswith(".csv")]
    dfs = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    print(f"Loaded {len(combined_df)} total rows from {len(all_files)} files.")
    return combined_df


def clean_data(df):
    """Clean and standardize columns"""
    # try to handle different column name variations
    possible_text_cols = ["reviews.text", "reviewText", "reviews_body", "text"]
    possible_rating_cols = ["reviews.rating", "overall", "rating", "stars"]

    text_col = next((col for col in possible_text_cols if col in df.columns), None)
    rating_col = next((col for col in possible_rating_cols if col in df.columns), None)

    if not text_col or not rating_col:
        raise ValueError("Could not find review text or rating column in dataset.")

    df = df[[text_col, rating_col]].rename(columns={text_col: "review_text", rating_col: "rating"})
    df.dropna(subset=["review_text", "rating"], inplace=True)

    # convert rating to sentiment label
    def get_sentiment(r):
        if r >= 4:
            return "positive"
        elif r <= 2:
            return "negative"
        else:
            return "neutral"

    df["sentiment"] = df["rating"].apply(get_sentiment)
    return df


def save_clean_data(df, path_out="data/processed/amazon_reviews_clean.csv"):
    os.makedirs(os.path.dirname(path_out), exist_ok=True)
    df.to_csv(path_out, index=False)
    print(f"✅ Clean dataset saved to {path_out}")


def run():
    df_raw = load_raw_data()
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean)


if __name__ == "__main__":
    run()
