import random

# 1) Modelliere das Förderband als Liste
coveyor_belt = [" "] * 10

liquprice = "Lakrize"
cherry = "Kirsche"
strawberry = "Erdbeere"
cola_bottle = "Cola-Flasche"
empty = "Keine Packung in den Karton gefallen"


# Zusätzliche Aufgabe: Zufällige Wahl von Süßigkeiten
def place_random_item(candy_flavors, delivery):
    global coveyor_belt
    random_variety = random.choice(candy_flavors)
    items_or_empty = [candy_flavors + " "]
    for x in range(0, len(delivery)-1):
        random_element = random.choice(items_or_empty)
        place_item(random_element)
        drop_item(delivery)


# 2) Erstelle eine Funktion place_item
def place_item(item_space):
    global coveyor_belt
    coveyor_belt.insert(0, item_space)


# 3) Erstelle eine Funktion drop_item
def drop_item(delivery):
    global coveyor_belt
    if coveyor_belt:
        first_sweet_on_the_belt = coveyor_belt[0]
        variety_name = coveyor_belt.pop(0)
        delivery.append(first_sweet_on_the_belt)
        if variety_name != " ":
            print(f"{variety_name} in den Karton gefallen")
        else:
            print("Keine Packung in den Karton gefallen")
    else:
        print("Das Förderband ist leer.")


# Testen
def test(candy_flavors, delivery):
    global coveyor_belt
    print("Test: ")

    place_item(candy_flavors[0])
    place_item(candy_flavors[1])
    place_item(candy_flavors[2])
    place_item(" ")

    # Aktuellen Zustand des Förderbands ausgeben
    print("Aktuelles Förderband:", coveyor_belt)

    # Eine Runde Förderband-Rotation durchführen
    print("Eine Runde Förderband-Rotation durchführen: ")
    drop_item(delivery)

    # Aktuellen Zustand des Förderbands und den Karton ausgeben
    print("Aktuelles Förderband:", coveyor_belt)
    print("Aktueller Inhalt des Kartons:", delivery)


# Zusätzlich: Abfrage Programmwahl/ Verpackungsgröße
def main():
    global coveyor_belt
    candy_flavors = [cherry, strawberry, cola_bottle, liquprice]
    counter = 0
    test_choice = input("Möchten Sie eine Testlieferung verpacken? (True/False)")

    if test_choice:
        package_size = 10
    else:
        package_size = input("Wie groß soll die Lieferung sein? (in Stück)")
    delivery = [] * package_size

    if test_choice:
        test(candy_flavors, delivery)
    else:
        print("Die Lieferung wird automatisch verpackt.")
        while counter < package_size:
            place_random_item(candy_flavors, delivery)
            counter += 1


main()