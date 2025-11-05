# Sentiment Analysis for Product Reviews

### 📦 Industry
E-commerce

### 🧠 Project Overview
This project analyzes Amazon product reviews to determine sentiment (positive, negative, or neutral) and derive insights to improve product offerings.  
It now includes a fully functional **Flask API** backend and a **React-based frontend dashboard** styled with **Tailwind CSS**, designed with an Amazon-like theme.

---

### ⚙️ Steps
1. **Data Preprocessing:** Clean and prepare review text (tokenize, remove stopwords, lemmatize).
2. **Feature Extraction:** Convert text to numerical form using TF-IDF.
3. **Model Training:** Train classification models — Logistic Regression, Random Forest, and XGBoost.
4. **Evaluation:** Evaluate models using Accuracy, Precision, Recall, and F1-score.
5. **Visualization & Deployment:** Develop and serve an interactive Sentiment Dashboard.

---

## 🧰 Tools & Libraries
| Category | Tools |
|-----------|--------|
| **Programming** | Python 3.10+, JavaScript (ES6+) |
| **ML Libraries** | Scikit-learn, XGBoost, Pandas, NumPy |
| **NLP Tools** | NLTK, spaCy |
| **Visualization** | Matplotlib, Plotly, Recharts |
| **Frontend** | React (Vite), Tailwind CSS |
| **Backend** | Flask |
| **Deployment** | Docker, Nginx |
| **Version Control** | Git, Git LFS |

---

## 📊 Dataset
- **Source:** Amazon Product Reviews Dataset ([Kaggle](https://www.kaggle.com/datasets))  
- **Format:** CSV with text and ratings.  
- **Columns:**
  | Column | Description |
  |---------|--------------|
  | `reviewText` | Customer review |
  | `overall` | Numeric rating (1–5) |
  | `sentiment` | Derived label (Positive / Neutral / Negative) |

---

## ▶️ How to Run

### 🧩 1. Backend (Flask API)

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run
API will start at: http://127.0.0.1:5000

💻 2. Frontend (React + Vite)
bash
Copy code
cd frontend
npm install
npm run dev
Frontend will run at: http://localhost:5173

🔗 3. API Integration
The React frontend sends POST requests to:

arduino
Copy code
http://127.0.0.1:5000/api/predict
Example response:

json
Copy code
{
  "review": "The product quality is amazing!",
  "sentiment": "positive"
}
🧱 Docker Setup
🐍 Backend (Dockerfile.backend)
Build and run:

bash
Copy code
docker build -t sentiment-backend -f Dockerfile.backend .
docker run -p 5000:5000 sentiment-backend
⚛️ Frontend (Dockerfile.frontend)
Build and run:

bash
Copy code
docker build -t sentiment-frontend -f Dockerfile.frontend .
docker run -p 5173:80 sentiment-frontend
🧩 Optional (Compose Both)
yaml
Copy code
version: "3.9"
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.backend
    ports:
      - "5000:5000"
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.frontend
    ports:
      - "5173:80"
    depends_on:
      - backend
Run both together:

bash
Copy code
docker-compose up --build
📈 Results
Model	Accuracy	F1-Score
Logistic Regression	93.7%	0.93
Random Forest	95.3%	0.95
XGBoost	95%+	0.95

✅ Random Forest achieved the best overall accuracy.
✅ XGBoost maintained strong precision-recall balance.

Visualizations and reports are stored under /experiments.

🎨 Dashboard Overview
The Amazon Sentiment Dashboard provides:

A clean, modern UI built with React + TailwindCSS.

Text input for user reviews.

Real-time sentiment predictions via Flask API.

Placeholder section for live sentiment distribution charts (via Recharts).

Amazon-inspired design theme with yellow and gray tones.

🚀 Future Enhancements
Integrate interactive charts (Pie/Bar) to display sentiment trends.

Add user review upload (CSV input).

Expand to deep learning models (LSTM / BERT).

Integrate Gunicorn + Nginx for production deployment.

Add CI/CD pipeline for automated builds and model updates.

Deploy full-stack app via Docker Compose or cloud (Render, AWS).


# 🧑‍💻 Author

**Himanshu Singh**

- [Portfolio](https://dev-himanshusing.netlify.app/)
- [Email](mailto:connecttohimanshu.singh@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/connectto-himanshu/)
- [GitHub](https://github.com/Code-sHimanshu)
