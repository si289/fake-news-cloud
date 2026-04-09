import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# load dataset
df = pd.read_csv("dataset\general_fake_news.csv")

# combine title + full text
X = df["title"] + " " + df["full_text"]

# fake/real label
y_label = df["label"]

# category label
y_category = df["category"]

# vectorizer
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vector = vectorizer.fit_transform(X)

# fake news model
fake_model = LogisticRegression(max_iter=1000)
fake_model.fit(X_vector, y_label)

# better category model
category_model = MultinomialNB()
category_model.fit(X_vector, y_category)

# save all files
with open("model.pkl", "wb") as f:
    pickle.dump(fake_model, f)

with open("category_model.pkl", "wb") as f:
    pickle.dump(category_model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Fake + Category models saved successfully")

