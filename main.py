import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen
z = [i**3 for i in x]  # Kubikzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x, z, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen von 0 bis 9')
plt.xlabel('x')
plt.ylabel('y', rotation='horizontal')

# Legende anzeigen
plt.legend()

# Datei als .png speichern
plt.savefig("Diagramm.png", format='png', dpi=144)
print("Datei als 'Diagramm.png' gespeichert")

# Diagramm anzeigen
plt.show()
