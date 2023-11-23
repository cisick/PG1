
# Durch die Funktion place_item werden Packungen auf den Beginn des Förderbands gelegt. Der Inhalt der Packung wird
# durch einen String definiert.
def place_item(conveyor, item):
    # Der erste Speicherplatz des Förderbands (Index 0) wird als Anfang des Förderbandes definiert
    conveyor[0] = item


# Simulation des Auswurfs des Förderbandes in eine Kiste.
def drop_item(conveyor):
    # Zuerst werden alle Elemente der Liste um einen Index verschoben. Dies Simuliert das Verfahren des Förderbandes.

    print(conveyor)

    if conveyor[9]:
        print(conveyor[9], "in den Karton gefallen.")
    else:
        print("Keine Packung in den Karton gefallen.")

    for i in range(9, 0, -1):
        conveyor[i] = conveyor[i - 1]
        # print(conveyor[i], "von Index", i - 1, "nach Index", i, "verschoben.")

    # Je nach Zustand des Ende des Förderbands wird ein anderer Text ausgegeben.


# Variable für das Förderband mit zehn Einheiten. Der Einheitentyp wird als String gespeichert. Leere Förderplätze
# werden über einen leeren String gekennzeichnet. Zu Begin ist das ganze Förderband leer.
conveyor_band = [""] * 10

place_item(conveyor_band, "Kirsche")
drop_item(conveyor_band)
place_item(conveyor_band, "Cola")
drop_item(conveyor_band)
place_item(conveyor_band, "")
drop_item(conveyor_band)
place_item(conveyor_band, "Sauer")
drop_item(conveyor_band)
place_item(conveyor_band, "Goldbärchen")
drop_item(conveyor_band)
place_item(conveyor_band, "Lakritze")
drop_item(conveyor_band)
place_item(conveyor_band, "Burger")
drop_item(conveyor_band)
place_item(conveyor_band, "Schnecken")
drop_item(conveyor_band)
place_item(conveyor_band, "Schocki")
drop_item(conveyor_band)
place_item(conveyor_band, "Cola")
drop_item(conveyor_band)
place_item(conveyor_band, "Lakritze")
drop_item(conveyor_band)
place_item(conveyor_band, "Goldbärchen")
drop_item(conveyor_band)
place_item(conveyor_band, "Goldbärchen")
drop_item(conveyor_band)
drop_item(conveyor_band)
place_item(conveyor_band, "Lakritze")
drop_item(conveyor_band)
place_item(conveyor_band, "")
drop_item(conveyor_band)
place_item(conveyor_band, "Cola")
drop_item(conveyor_band)
place_item(conveyor_band, "")
drop_item(conveyor_band)
place_item(conveyor_band, "Cola")
drop_item(conveyor_band)