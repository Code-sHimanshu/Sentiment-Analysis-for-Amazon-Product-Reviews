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

# 📂 Folder Structure

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


# 🧰 Tools & Libraries
| Category | Tools |
|-----------|--------|
| **Programming** | Python 3.10+ |
| **Libraries** | NLTK, spaCy, Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Plotly |
| **Environment** | Virtualenv / venv |
| **Version Control** | Git, Git LFS |
| **Deployment** | Flask, Render / Docker |

# 📊 Dataset
- **Source:** Amazon Product Reviews Dataset (via [Kaggle](https://www.kaggle.com/datasets) 
- **Format:** CSV files containing review text and ratings.
- **Location:** Stored under `data/raw/`

| Column | Description |
|---------|--------------|
| `reviewText` | Customer review text |
| `overall` | Numeric rating (1–5) |
| `sentiment` | Label (Positive / Neutral / Negative) |

# ▶️ How to Run

### 1️⃣ create and activate virtual environment

python -m venv venv
venv\Scripts\activate


### 2️⃣ install dependencies

pip install -r requirements.txt

### 3️⃣ run preprocessing

python src/data/make_dataset.py

### 4️⃣ Build features

python -m src.features.build_features

### 5️⃣ Train models

python -m src.models.train_model

### (Optional) Train multiple models and compare

python -m src.models.multiple_models

### 6️⃣ Run predictions on new data

python -m src.models.predict_model

### ⚠️ Troubleshooting: "npm error could not determine executable to run" (Windows / frontend)
If `npx tailwindcss init -p` fails with "could not determine executable to run" or "'tailwindcss' is not recognized", follow these steps from the frontend folder:

1. Verify Node/npm are installed:
```bash
node -v
npm -v
```

2. Ensure you're in the frontend folder and package.json exists:
```bash
cd frontend
dir package.json   # use ls package.json on WSL/mac
# If missing:
npm init -y
```

3. Install Tailwind and PostCSS locally:
```bash
npm install -D tailwindcss postcss autoprefixer
```

4. Initialize Tailwind (pick one command if one fails):
```bash
npx tailwindcss init -p
# If npx still errors, try:
npm exec --package tailwindcss tailwindcss init -p
# or
npx --package tailwindcss@latest tailwindcss init -p
```

5. If you see "'tailwindcss' is not recognized..." or persistent npx errors:
```bash
npm cache verify
# or (if necessary)
npm cache clean --force
# Try running the same commands in cmd.exe or Windows Terminal (not an unusual/isolated shell).
```

6. If none of the above fixes it, open the npm debug log referenced in the error (example path shown in your error):
C:\Users\<your-user>\AppData\Local\npm-cache\_logs\<timestamp>-debug-0.log

Then paste the last ~50 lines here and I'll help diagnose further.

# 📈 Results

      Model	                    Accuracy	    F1-Score

-Logistic Regression	        ~93.7%	           0.93
-Random   Forest	            ~95.3%	           0.95
-XGBoost 	                    ~95%+              0.95

- Random Forest achieved the highest accuracy among the tested models.

- XGBoost provided balanced performance across precision and recall.

- Insights and prediction reports are available in the reports/ directory.

# 🚀 Future Enhancements

- Incorporate deep learning models (e.g., LSTM, BERT).

- Build an interactive dashboard to visualize sentiment trends.

- Deploy API endpoint using Flask or FastAPI.

- Automate model retraining using a CI/CD pipeline.

# 🧑‍💻 Author

**Himanshu Singh**

- [Portfolio](https://dev-himanshusing.netlify.app/)
- [Email](mailto:connecttohimanshu.singh@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/connectto-himanshu/)
- [GitHub](https://github.com/Code-sHimanshu)
