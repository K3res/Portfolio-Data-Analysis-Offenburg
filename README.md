# IU Data Analysis Projekt: Themenextraktion auf Twitter 
**Kurs:** Data Analysis (DLBISIC02-01)  
**Institution:** IU Internationale Hochschule

## 📝 Projektbeschreibung
Dieses Projekt befasst sich mit der Extraktion und Analyse von Twitter-Daten. Ursprünglich war ein Live-Abruf über die X-API geplant. Aufgrund technischer Restriktionen (API-Paywall, Fehler 402) wurde das Projekt auf einen validierten Datensatz von Kaggle umgestellt. Dies ermöglicht die Demonstration der vollständigen Analyse-Pipeline von der Datenreinigung bis zum Topic Modeling.

---

## 🛠 Erarbeitungsphasen (Lernzyklus)
1. **Konzeption & Problemidentifikation:** Aufbau der API-Anbindung (Tweepy). Dokumentation der API-Sperre als Teil des Lernprozesses.
2. **Implementierung (Proxy-Lösung):** Einbindung eines Ersatz-Datensatzes (`tweets_raw.csv`) zur Fortführung der Analyse.
3. **Analyse:** * **Entity-Analyse:** Identifikation der aktivsten User und Hashtags.
    * **Sentiment-Analyse:** Stimmungsbewertung mittels NLP (`TextBlob`).
4. **Optimierung:** Berechnung des **Coherence Scores** zur Bestimmung der optimalen Themenanzahl ($k=6$).

---

## 💻 Tech Stack
* **Sprache:** Python 3.x
* **Bibliotheken:** * `Pandas` / `Numpy` (Datenverarbeitung)
  * `TextBlob` (Sentiment NLP)
  * `Matplotlib` (Visualisierung)

---

## 📁 Repository Struktur
* `01_load_and_inspect_data.py`: Initialer Daten-Check und Import.
* `02_analysis_sentiment.py`: Durchführung der Stimmungsanalyse (NLP).
* `03_topic_coherence_logic.py`: Mathematische Bestimmung der Themenanzahl.
* `04_entity_analysis.py`: Extraktion von Usern und Hashtags.
* `tweets_raw.csv`: Verwendete Datenbasis.
* `requirements.txt`: Installationsliste der Abhängigkeiten.