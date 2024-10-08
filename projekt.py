import matplotlib.pyplot as plt
import pandas as pd

# 1. Quadratzahlen und Kubikzahlen berechnen
quadratzahlen = [x**2 for x in range(10)]
kubikzahlen = [x**3 for x in range(10)]

# 2. Diagramm erstellen
plt.plot(range(10), quadratzahlen, label='Quadratzahlen', marker='o')
plt.plot(range(10), kubikzahlen, label='Kubikzahlen', marker='s')
plt.legend()
plt.xlabel('Zahl')
plt.ylabel('Wert')
plt.title('Quadrat- und Kubikzahlen von 0 bis 9')
plt.grid(True)

# 3. Diagramm speichern
plt.savefig('diagramm.png', format='png')
plt.show()

# 4. DataFrame erstellen und speichern
data = {
    'Zahl': list(range(10)),
    'Quadratzahlen': quadratzahlen,
    'Kubikzahlen': kubikzahlen
}

df = pd.DataFrame(data)
df.to_csv('zahlen.csv', index=False)

# 5. Anforderungen in requirements.txt speichern
with open('requirements.txt', 'w') as f:
    f.write("matplotlib\n")
    f.write("pandas\n")

print("Alle Aufgaben wurden erfolgreich ausgeführt!")