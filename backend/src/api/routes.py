from flask import Blueprint, request, jsonify
import joblib
import os
import re
from src.utils.preprocess import preprocess_text

api_blueprint = Blueprint("api", __name__)

# Load model and vectorizer
MODEL_PATH = os.path.join("src", "models", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join("src", "models", "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@api_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("review", "")

    if not text.strip():
        return jsonify({"error": "Empty review text"}), 400

    # --- Preprocess and model prediction ---
    processed_text = preprocess_text(text)
    features = vectorizer.transform([processed_text])
    prediction = model.predict(features)[0]

    # --- Smart rule-based adjustments ---
    text_lower = text.lower()

    # 1️⃣ Strong negative keywords
    negative_keywords = [
        "bad", "poor", "cheap", "worst", "disappointed", "terrible",
        "awful", "broken", "horrible", "useless", "waste", "low quality",
        "dirty", "faulty", "unhappy", "unusable", "damaged", "hate"
    ]

    if any(word in processed_text.split() for word in negative_keywords):
        prediction = "negative"

    # 2️⃣ Strong positive keywords
    positive_keywords = [
        "amazing", "excellent", "great", "love", "wonderful", "perfect",
        "awesome", "superb", "fantastic", "impressive"
    ]

    if any(word in processed_text.split() for word in positive_keywords):
        prediction = "positive"

    # 3️⃣ Handle negations (e.g. "not good", "not worth", "could be better")
    negation_patterns = [
        r"not\s+(good|great|happy|amazing|worth|satisfied|recommended)",
        r"could\s+be\s+(better|improved)",
        r"was\s+expecting\s+more",
        r"did\s+not\s+like",
        r"no\s+value",
    ]
    if any(re.search(pat, text_lower) for pat in negation_patterns):
        prediction = "negative"

    return jsonify({"review": text, "sentiment": prediction})
