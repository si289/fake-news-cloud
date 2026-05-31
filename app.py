from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_news

app = Flask(__name__)
CORS(app)  # 🔥 important for Netlify connection

@app.route('/')
def home():
    return "Fake News Detection API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    news_text = data['text']
    result = predict_news(news_text)

    return jsonify({
        "prediction": result
    })

if __name__ == '__main__':
    app.run(debug=True)