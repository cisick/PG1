# Aufgabe 4
# Erstellen Sie eine Funktion, welche die Ankunftszeit für ein Fahrzeug sowie
# das Kennzeichen setzt.
import datetime


def setArrival(car_park):
    level = int(input("Ebene?")) - 1
    row = int(input("Reihe?")) - 1
    lot = int(input("Parkplatz?")) - 1

    car_park[level][row][lot]["arrival"] = datetime.datetime.now()
    car_park[level][row][lot]["license plate"] = input("Kennzeichen")

# Aufgabe 1
# Erstellen Sie eine mehrdimensionale Liste für ein Parkhaus (car_park).
# Das Parkhaus besteht aus:
# - drei Ebenen (level)
# - pro Ebene fünf Reihen (row)
# - jede Reihe hat 20 Parkplätze (lot)

# Aufgabe 3
# Erstellen Sie für jeden Parkplatz ein Wörterbuch, welches folgende
# Schlüsselwörter hat:
# - Ankunftszeit (arrival)
# - Abfahrtszeit (departure)
# - Kennzeichen (license plate)

car_park = list()

for _ in range(3):
    level = list()

    for _ in range(5):
        row = list()

        for _ in range(20):
            lot = dict()

            lot["arrival"] = None
            lot["departure"] = None
            lot["license plate"] = None

            row.append(lot)

        level.append(row)

    car_park.append(level)

setArrival(car_park)

# Aufgabe 2
# Berechnen Sie die Anzahl an Parkplätzen des Parkhauses zur Laufzeit.

# Aufgabe 5
# Für die Anzeige der freien Parkplätze werden nun die Parkplätze gezählt,
# welche keine gesetzte Kennzeichen haben.

counter = 0
counter_free = 0
for level in car_park:
    for row in level:
        for lot in row:
            counter += 1

            if lot["license plate"]:
                counter_free += 1

print("Anzahl Parkplätze:", counter)
print("Belegte Parkplätze:", counter_free)

print(car_park)