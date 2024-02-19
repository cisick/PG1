# Aufgabe 1:
# Erstellen Sie eine Funktion addBookToShelf mit dem
# Parameter shelf.
#
# Die Funktion fügt ein neues Buch in ein Fach des
# Bücherregals ein. Dazu fragt es den Anwender nach der
# Reihe und der Lücke sowie dem Buchtitel.

# Aufgabe 2:
# Erweitern Sie Aufgabe 1 um eine Prüfung der Eingabewerte
# für die Reihe und Lücke, damit die Eingabe in einem gültigen
# Bereich liegt.

def addBookToShelf(shelf):
    row = int(input("Welche Reihe?")) - 1
    gap = int(input("Welche Lücke?")) - 1
    title = input("Buchtitel? ")

    if row >= len(shelf) or row < 0:
        raise IndexError("Reihe ungültig")
    elif gap >= len(shelf[row]) or gap < 0:
        raise IndexError("Lücke ungültig")
    elif shelf[row][gap] is not None:
        raise OverflowError("Hier steht schon ein Buch.")
    else:
        shelf[row][gap] = title

# Aufgabe 3:
# Die Funktion aus Aufgabe 1 wirft nun eine Exeption, wenn ein Fehler,
# wie in Aufgabe 2 beschrieben, auftritt.
# Die Exeption wird von Ihrem Quelltext zum Testen abgefangen und der
# Benutzer kann entsprechend reagieren.

shelf = list()

# Create a bookshelf with 10 rows and 30 books per row.
for i in range(10):
    row = list()

    for j in range(30):
        row.append(None)

    shelf.append(row)

# Access the shelf:
print(shelf)

# Access the 3rd row
#print(shelf[2])

# Access the 4th book in 3rd row
#print(shelf[2][3])

# Set book samples
shelf[2][3] = "Rich dad poor dad"
shelf[3][1] = "Eigene KI-Anwendungen programmieren"
shelf[4][4] = "Gregs Tagebuch (Teil 3)"
shelf[1][4] = "Mathematische Formeln und Definitionen"

print(shelf)

try:
    addBookToShelf(shelf)
except IndexError:
    print(IndexError.__)
except OverflowError:
    print("Andere Fehlermeldung")
finally:
    print("Buchhandlung geschlossen...")

print(shelf)
