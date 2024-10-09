# Hausaufgabe: Erweiterte Datenvisualisierung und Speicherung
## Aufgabe 1: Hinzufügen einer weitere Datenreihe
1. Ziel: Erweitere das bestehende Python-Skript (vom Beispiel: https://github.com/ts-24-08/python-venv-pip), sodass  die Kubikzahlen (z.B. 1³, 2³, 3³, …) für die Zahlen 0 bis 9 anzeigt.
2. Anweisungen:
- Füge eine  Liste hinzu, die die Kubikzahlen von 0 bis 9 berechnet.
- Zeichne die beiden Datensätze (Quadratzahlen und Kubikzahlen) in dasselbe Diagramm.
- Verwende eine Legende, um die beiden Datenreihen klar zu identifizieren.
## Aufgabe 2: Speichern des Diagramms als Bild
1. Ziel: Speichere das erstellte Diagramm als Bilddatei (z.B. im PNG-Format), sodass du es später verwenden oder teilen kannst.Tipp: Recherchiere auf der Matplotlib-Dokumentationsseite nach den Funktionen.
2. Anweisungen:
- Anstatt das Diagramm nur anzuzeigen, speichere es mit der savefig() Methode.
- Füge den Dateinamen und das Format in den Befehl ein.
## Zusatzaufgabe: Aufgabe 3: Verwende eine zweite Bibliothek für Datenanalyse (Pandas)
1. Ziel: Installiere die Bibliothek Pandas, um Daten einfacher zu handhaben, und speichere die berechneten Werte in einer CSV-Datei.
2. Anweisungen:
- Installiere Pandas in der virtuellen Umgebung.
- Füge die Bibliothek Pandas in dein Skript ein und erstelle ein DataFrame mit den Zahlen 0 bis 9, deren Quadraten und deren Kubikzahlen.
- Speichere diese Daten in einer CSV-Datei namens zahlen.csv.
## Aufgabe 4: Anforderungen in requirements.txt speichern
1. Ziel: Halte alle verwendeten Bibliotheken in einer requirements.txt Datei fest, damit dein Projekt leicht reproduzierbar ist.
2. Anweisungen:
- Aktualisiere deine requirements.txt Datei, um sicherzustellen, dass sowohl matplotlib als auch pandas in der Liste der installierten Pakete enthalten sind.
- Verwende einen Befehl, um die requirements.txt Datei zu aktualisieren
## Aufgabe 5: Ergänze die gitignore-Datei
1. Ziel: Verhindere, dass sensible oder temporäre Dateien in das Git-Repository gelangen.
2. Anweisungen:
- Füge die Datei zahlen.csv und alle PNG-Dateien, die durch das Skript erstellt werden, zur .gitignore Datei hinzu.
- Überprüfe, ob die Dateien nicht mehr im Repository enthalten sind.
