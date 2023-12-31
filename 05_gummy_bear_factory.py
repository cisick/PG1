import random

def place_item(conveyor, item):
    conveyor[0] = item


def drop_item(conveyor, delivery):
    if conveyor[9]:
        print(conveyor[9], "in den Karton gefallen.")
        delivery.append(conveyor[9])
    else:
        print("Keine Packung in den Karton gefallen.")

    for i in range(9, 0, -1):
        conveyor[i] = conveyor[i - 1]
    conveyor[0] = ""

    print("Die Lieferung enthält: ", len(delivery), " Süßigkeiten.")
    print(delivery)
    print("Der Status des Förderbands ist: ")
    print(conveyor)
    print("########### Eine Runde ################")


def select_random_sweet(sweet_or_empty):
    return random.choice(sweet_or_empty)


conveyor_band = [""] * 10
delivery = []


sweets_or_empty = ["Kirsche", "Cola", "Sauer", "Goldbärchen", "Lakritze", "Burger", "Schnecken", "Schocki", ""]
random_sweets_or_empty = ""
print("                                                         ")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
test = input("Möchten Sie das Förderband testen? (True/ False)")

if test == "True":
    delivery_max = 10
else:
    delivery_max = int(input("Wie groß soll die Lieferung sein?"))

while True:
    if len(delivery) < delivery_max:
        random_sweets_or_empty = select_random_sweet(sweets_or_empty)
        place_item(conveyor_band, random_sweets_or_empty)
        drop_item(conveyor_band, delivery)
    else:
        print("------------------------------")
        print("Die Lieferung ist verpackt.")
        print("Die Lieferung enthält: ", len(delivery), " Süßigkeiten.")
        print(delivery)
        break
