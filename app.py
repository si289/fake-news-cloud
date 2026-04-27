from flask import Flask, render_template, request
from predict import predict_news
import requests

app = Flask(__name__)

# ✅ NewsData.io API Key
API_KEY = "pub_16abcf8ded784efdadf48ab9e7cd3574"

# ------------------------------
# Home Page
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------
# Manual News Prediction
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form["news"]

    prediction, category, confidence = predict_news(news_text)

    return render_template(
        "index.html",
        prediction=prediction,
        category=category,
        confidence=confidence
    )
# ------------------------------
# 🔴 Live News Detection
# ------------------------------
@app.route("/live-news")
def live_news():
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country=in&language=en"

    response = requests.get(url)
    data = response.json()

    results = []

    if "results" in data:
        for article in data["results"][:5]:
            title = article.get("title", "")
            description = article.get("description", "")
            news_text = title + " " + str(description)

            prediction, category, confidence = predict_news(news_text)

            results.append({
                "title": title,
                "prediction": prediction,
                "category": category,
                "confidence": confidence,
                "source": article.get("source_id", "Unknown"),
                "link": article.get("link", "#")
            })

    return render_template("live_news.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
   
           


        