import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Wir simulieren die Berechnung der Kohärenz-Werte
# In der Realität würde hier die LDA-Schleife laufen
themen_anzahl = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Typische Kohärenzwerte (steigen oft an und flachen dann ab)
kohaerenz_werte = [0.42, 0.48, 0.55, 0.62, 0.65, 0.64, 0.63, 0.61, 0.59, 0.58] 
# Wir kürzen auf die Länge der Themenliste
kohaerenz_werte = kohaerenz_werte[:len(themen_anzahl)]

# 2. Grafik erstellen
plt.figure(figsize=(10, 5))
plt.plot(themen_anzahl, kohaerenz_werte, marker='o', linestyle='-', color='darkorange')

# 3. Den "Optimalen Punkt" markieren (der höchste Punkt)
plt.axvline(x=6, color='red', linestyle='--', label='Optimales K (6 Themen)')

plt.title('Identifikation der optimalen Themenanzahl (Coherence Score)')
plt.xlabel('Anzahl der Themen (k)')
plt.ylabel('Coherence Score (c_v)')
plt.legend()
plt.grid(True)

# Speichern für das Portfolio
plt.savefig('topic_coherence_analysis.png')
print("Grafik 'topic_coherence_analysis.png' wurde erstellt!")
plt.show()