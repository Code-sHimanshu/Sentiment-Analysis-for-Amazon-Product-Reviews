from flask import Flask
from flask_cors import CORS
from src.api.routes import api_blueprint

app = Flask(__name__)
CORS(app)

# Register API routes
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route('/')
def home():
    return {"message": "🚀 Sentiment Analysis API is running successfully!"}

if __name__ == "__main__":
    app.run(debug=True)
