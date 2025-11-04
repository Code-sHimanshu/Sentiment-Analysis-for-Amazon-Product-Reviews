import re
import string
import spacy
from nltk.corpus import stopwords
import nltk

# download stopwords if not already present
nltk.download("stopwords", quiet=True)
STOPWORDS = set(stopwords.words("english"))

# load spaCy English model (make sure it's installed: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")


def clean_text(text: str) -> str:
    """Basic cleaning: lowercase, remove special characters, extra spaces"""
    text = str(text).lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text


def remove_stopwords(text: str) -> str:
    """Remove common English stopwords"""
    tokens = text.split()
    filtered = [word for word in tokens if word not in STOPWORDS]
    return " ".join(filtered)


def lemmatize_text(text: str) -> str:
    """Lemmatize text using spaCy"""
    doc = nlp(text)
    lemmatized = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(lemmatized)


def preprocess_text(text: str) -> str:
    """Full preprocessing pipeline"""
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text


# quick test
if __name__ == "__main__":
    sample = "The products were amazing! I loved the packaging and quality."
    print("Original:", sample)
    print("Processed:", preprocess_text(sample))
