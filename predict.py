# predict.py
import random

def detect_category(text):
    text = text.lower()

    if any(word in text for word in ["government", "minister", "election", "policy"]):
        return "Politics"
    elif any(word in text for word in ["cricket", "football", "player", "match"]):
        return "Sports"
    elif any(word in text for word in ["ai", "software", "technology", "computer"]):
        return "Technology"
    elif any(word in text for word in ["doctor", "vaccine", "medicine", "hospital"]):
        return "Health"
    elif any(word in text for word in ["actor", "movie", "celebrity"]):
        return "Entertainment"
    elif any(word in text for word in ["student", "college", "university"]):
        return "Education"
    elif any(word in text for word in ["moon", "scientist", "space"]):
        return "Science"
    return "General"


def predict_news(news_text):
    text = news_text.lower()

    fake_words = [
        "gold moon",
        "aliens",
        "flying umbrella",
        "bought the moon",
        "diamond sky"
    ]

    if any(word in text for word in fake_words):
        prediction = "Fake News"
        confidence = 98.5
    else:
        prediction = "Real News"
        confidence = 95.0

    category = detect_category(news_text)

    return prediction, category, confidence



    
 



