import pickle
import os

# Get current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and vectorizer
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

# Load files safely
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)

except Exception as e:
    print("Error loading model or vectorizer:", e)
    model = None
    vectorizer = None


# 🔍 Prediction Function
def predict_news(text):
    if model is None or vectorizer is None:
        return {
            "prediction": "Error",
            "confidence": 0
        }

    try:
        # Transform input text
        text_vector = vectorizer.transform([text])

        # Predict
        prediction = model.predict(text_vector)[0]

        # Get probability if available
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(text_vector)[0]
            confidence = max(prob)
        else:
            confidence = 0

        # Convert result
        if prediction == 1:
            result = "Real News"
        else:
            result = "Fake News"

        return {
            "prediction": result,
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        return {
            "prediction": "Error",
            "confidence": 0,
            "message": str(e)
        }
    
    
 



