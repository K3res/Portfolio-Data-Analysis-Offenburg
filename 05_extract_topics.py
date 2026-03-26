import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 1. Daten laden
df = pd.read_csv('tweets_raw.csv')

# 2. Text in Zahlen umwandeln (Vektorisierung)
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
tf = vectorizer.fit_transform(df['Text'].values.astype('U'))

# 3. LDA Modell (wir fordern 5 Themen an, wie im Aufgabentext)
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(tf)

# 4. Die wichtigsten Wörter pro Thema ausgeben
words = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    print(f"\nTopic #{topic_idx + 1}:")
    print([words[i] for i in topic.argsort()[:-11:-1]])