import pandas as pd
from collections import Counter
import re

# 1. Daten laden
df = pd.read_csv('tweets_raw.csv')

# 2. Aktivste User (Wer postet am meisten?)
active_users = df['Username'].value_counts().head(10)
print("Aktivste User (Top 10):")
print(active_users)

# 3. Häufigste Hashtags extrahieren
def get_hashtags(text):
    return re.findall(r"#(\w+)", str(text))

all_hashtags = []
df['Text'].apply(lambda x: all_hashtags.extend(get_hashtags(x)))

hashtag_counts = Counter(all_hashtags).most_common(10)
print("\nHäufigste Hashtags (Top 10):")
print(hashtag_counts)
