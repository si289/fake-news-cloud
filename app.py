from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

# Initialize app
app = Flask(__name__)
CORS(app)   # ✅ Allows Netlify frontend to connect

# Load ML model
model_path = "model.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError("model.pkl file not found!")

model = pickle.load(open(model_path, "rb"))

# Home route
@app.route("/")
def home():
    return "✅ Fake News Detection API is Running"

# Prediction route (for Netlify frontend)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "news" not in data:
            return jsonify({"error": "No news text provided"}), 400

        text = data["news"]

        # Prediction
        prediction = model.predict([text])[0]

        # Optional: Convert output to readable format
        if str(prediction) == "0":
            result = "Fake News ❌"
        else:
            result = "Real News ✅"

        return jsonify({
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# Optional: Live news route (only if you implemented it)
@app.route("/live-news")
def live_news():
    return "Live News Feature Coming Soon 🚀"


# Run app
if __name__ == "__main__":
    app.run(debug=True)




            