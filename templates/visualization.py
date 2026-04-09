import pandas as pd
import matplotlib.pyplot as plt

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

labels = ["Fake","True"]
values = [len(fake),len(true)]

plt.bar(labels,values)

plt.title("Fake vs True News Distribution")

plt.xlabel("News Type")
plt.ylabel("Count")

plt.show()