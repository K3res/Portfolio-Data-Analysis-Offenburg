import pandas as pd
import os

# 1. Pfad zur Kaggle-Datei definieren
file_name = 'tweets_raw.csv'

print(f"Lade Datensatz: {file_name}...")

# 2. Daten laden
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    
    # 3. Erster Check: Was ist drin?
    print("\n--- Erste 5 Zeilen des Datensatzes ---")
    print(df.head())
    
    print("\n--- Spaltenübersichten ---")
    print(df.columns.tolist())
    
    print(f"\nErfolgreich geladen: {len(df)} Zeilen gefunden.")
else:
    print(f"FEHLER: Die Datei '{file_name}' wurde nicht im Ordner gefunden!")