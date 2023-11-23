parking_space = [5]

def main():
    while True:
        choice_parking = input("1) Wagen abstellen 2) Wagen abholen")

        if choice_parking == 1:
            set_parkingspace()
        elif choice_parking == 2:
            free_parkingspace()
        else:
            print("Die Eingabe war nicht korrekt. Bitte geben Sie eine der möglichen Auswahlmöglichkeiten ein: ")
            continue


def set_parkingspace():
    while True:
        license_plate = input("Wie lautet Ihr Kennzeichen?")
        parking_lot_number = int(input("Wie lautet Ihre Parkplatznummer?"))

        if len(parking_space[parking_lot_number - 1]) == 0:
            parking_space[parking_lot_number - 1] = license_plate
        else:
            print("Auf diesem Parkplatz steht bereits ein Auto. \n Bitte suchen Sie sich einen anderen Parkplatz aus.")
            continue


def free_parkingspace():
    parking_lot_number = input("Ich hoffe Sie hatten einen schönen Aufenthalt. \nWie lautet Ihre Parkplatznummer?")
    parking_space[parking_lot_number - 1] = ""
