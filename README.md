# Sentiment Analysis for Product Reviews

### 📦 Industry
E-commerce

### 🧠 Project Overview
This project analyzes Amazon product reviews to determine sentiment (positive, negative, or neutral) and derive insights to improve product offerings.

### ⚙️ Steps
1. **Data Preprocessing:** Clean and prepare review text (tokenize, remove stopwords, lemmatize).
2. **Feature Extraction:** Convert text to numerical form using TF-IDF or Word2Vec embeddings.
3. **Model Training:** Train classification models (Naive Bayes, Logistic Regression, LSTM).
4. **Evaluation:** Evaluate using Accuracy, Precision, Recall, and F1-score.
5. **Visualization:** Optionally, build a dashboard to visualize sentiment trends.

### 📂 Folder Structure

sentiment-analysis-product-reviews/
├── data/
│ ├── raw/ <- Original datasets
│ ├── interim/ <- Intermediate cleaned data
│ └── processed/ <- Final processed dataset
├── notebooks/ <- Jupyter notebooks for EDA & modeling
├── src/ <- Source code
│ ├── data/ <- Data loading scripts
│ ├── features/ <- Feature extraction scripts
│ ├── models/ <- Model training & prediction
│ ├── utils/ <- Helper functions
│ └── dashboard/ <- Dashboard app
├── tests/ <- Unit tests
├── docker/ <- Docker configuration
├── experiments/ <- Model reports, confusion matrices
├── requirements.txt
└── README.md


### 🧰 Tools & Libraries
- **Programming:** Python  
- **Libraries:** NLTK, spaCy, Scikit-learn, TensorFlow, Gensim, Matplotlib, Plotly, Flask  

### 📊 Dataset
- Source: Amazon Product Reviews Dataset (Kaggle / Datafiniti)
- Files in `data/raw/`

### ▶️ How to Run
```bash
# create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run preprocessing
python src/data/make_dataset.py
