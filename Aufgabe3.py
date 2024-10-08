import pandas as pd

# Erstelle eine Liste der Zahlen von 0 bis 9
zahlen = list(range(10))

# Berechne die Quadrate und Kubikzahlen
quadrate = [x ** 2 for x in zahlen]
kubikzahlen = [x ** 3 for x in zahlen]

# Erstelle ein DataFrame
df = pd.DataFrame({
    'Zahl': zahlen,
    'Quadrat': quadrate,
    'Kubikzahl': kubikzahlen
})

# Speichere das DataFrame in einer CSV-Datei
df.to_csv('zahlen.csv', index=False)

print("Die Datei 'zahlen.csv' wurde erfolgreich erstellt.")