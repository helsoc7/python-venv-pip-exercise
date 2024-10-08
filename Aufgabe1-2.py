import matplotlib.pyplot as plt

# Erstellen der Listen für Quadratzahlen und Kubikzahlen

zahlen = list(range(10))
quadratzahlen = [x**2 for x in zahlen]
kubikzahlen = [x**3 for x in zahlen]

# Erstellen des Diagramms

plt.figure(figsize=(10, 6))
plt.plot(zahlen, quadratzahlen, label='Quadratzahlen (n²)', marker='o')
plt.plot(zahlen, kubikzahlen, label='Kubikzahlen (n³)', marker='s')

# Diagramm formatieren

plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl (n)')
plt.ylabel('Wert')
plt.xticks(zahlen)  # x-Achsen-Beschriftungen auf die Zahlen 0-9 setzen
plt.legend()  # Legende hinzufügen
plt.grid(True)  # Gitter aktivieren
plt.tight_layout()  # Layout anpassen

# Diagramm als Bild speichern
plt.savefig('quadratzahlen_kubikzahlen.png', format='png')


# Diagramm anzeigen
plt.show()