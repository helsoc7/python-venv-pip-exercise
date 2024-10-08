
import matplotlib.pyplot as plt
import pandas as pd

# Quadratzahlen und Kubikzahlen berechnen
zahlen = list(range(10))
quadratzahlen = [x**2 for x in zahlen]
kubikzahlen = [x**3 for x in zahlen]

# Diagramm erstellen
plt.figure(figsize=(10, 5))
plt.plot(zahlen, quadratzahlen, label='Quadratzahlen', marker='o')
plt.plot(zahlen, kubikzahlen, label='Kubikzahlen', marker='s')

# Legende und Beschriftungen hinzufügen
plt.title('Quadrat- und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahlen')
plt.ylabel('Werte')
plt.legend()

# Diagramm speichern
plt.savefig('diagramm.png')
# DataFrame erstellen
df = pd.DataFrame({
    'Zahlen': zahlen,
    'Quadratzahlen': quadratzahlen,
    'Kubikzahlen': kubikzahlen
})

# CSV-Datei speichern
df.to_csv('zahlen.csv', index=False)





# Diagramm anzeigen
plt.show()









