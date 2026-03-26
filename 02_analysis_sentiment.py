import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# 1. Daten laden
df = pd.read_csv('tweets_raw.csv')

# 2. Sentiment-Funktion definieren
def get_sentiment(text):
    analysis = TextBlob(str(text))
    # Polarity liegt zwischen -1 (negativ) und 1 (positiv)
    if analysis.sentiment.polarity > 0:
        return 'Positiv'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negativ'

print("Analysiere Stimmungen... bitte warten...")

# 3. Analyse auf alle Tweets anwenden
df['Stimmung'] = df['Text'].apply(get_sentiment)

# 4. Ergebnisse zählen
sentiment_counts = df['Stimmung'].value_counts()
print("\nErgebnis der Analyse:")
print(sentiment_counts)

# 5. Visualisierung (Kuchendiagramm)
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'tomato', 'lightgray'])
plt.title('Stimmungsverteilung der analysierten Tweets')

# Grafik speichern
plt.savefig('sentiment_verteilung.png')
print("\nGrafik 'sentiment_verteilung.png' wurde erstellt!")
plt.show()