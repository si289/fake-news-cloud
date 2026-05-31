# predict.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 🔹 Sample dataset (you can replace later with real dataset)
data = {
    "text": [
        "Breaking: Government passes new education policy",
        "Shocking! Celebrity caught in scandal",
        "NASA launches new satellite successfully",
        "You won't believe what happened next!!!",
        "Scientists discover cure for disease",
        "Click here to win lottery now!!!"
    ],
    "label": [
        "REAL",
        "FAKE",
        "REAL",
        "FAKE",
        "REAL",
        "FAKE"
    ]
}

df = pd.DataFrame(data)

# 🔹 Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# 🔹 Train model
model = LogisticRegression()
model.fit(X, df["label"])


# 🔹 Prediction function
def predict_news(news_text):
    news_vector = vectorizer.transform([news_text])
    prediction = model.predict(news_vector)[0]
    return prediction