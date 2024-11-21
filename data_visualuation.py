import matplotlib.pyplot as plt

# Zahlen von 0 bis 9
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Berechnung der Zahlen
quadratzahlen = [i**2 for i in x]
kubikzahlen = [i**3 for i in x]

# LDiagramm für Quadratzahlen
plt.plot(x, quadratzahlen, label='Quadratzahlen', color='blue', marker='o')

# Diagramm für Kubikzahlen
plt.plot(x, kubikzahlen, label='Kubikzahlen', color='red', marker='x')

# Diagramm einrichten 
plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Wert')

# Legende anzeigen
plt.legend()

# speichern als Bild
plt.savefig('quadratzahlen_kubikzahlen.png')

# Diagramm anzeigen
# plt.show()
