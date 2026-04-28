from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_news

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (VERY IMPORTANT for frontend connection)
CORS(app)

# Home route (optional - for testing server)
@app.route('/')
def home():
    return "Fake News Detection API is running..."

# 🔍 Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from frontend
        data = request.get_json()

        if not data:
            return jsonify({
                "prediction": "Error",
                "confidence": 0,
                "message": "No input data received"
            })

        # Get text
        text = data.get("text")

        if not text or text.strip() == "":
            return jsonify({
                "prediction": "Error",
                "confidence": 0,
                "message": "Empty input"
            })

        # Call predict function
        result = predict_news(text)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "prediction": "Error",
            "confidence": 0,
            "message": str(e)
        })


# Run server
if __name__ == '__main__':
    app.run(debug=True)