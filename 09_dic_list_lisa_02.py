from datetime import datetime
# Aufgabe 1 (x Punkte)
# Erstellen Sie eine Funktion printUserObject mit dem Parameter userObject. (fertig)
# Der Parameter enthält ein dict, welches in der Funktion addUserToList
# definiert wurde.
# Geben Sie alle Keys und Values des dicts in folgender Darstellung aus:
# Vorname: Lord
# Nachname: Kelvin
# ...
# Den Geburtstag des Users geben Sie im folgenden Format aus: yyyy-mm-dd

def setDatetime():
    year = int(input("Geburtsjahr: "))
    month = int(input("Monat: "))
    day = int(input("Tag: "))

    return datetime(year, month, day)


def printUserObject(userObject):

    print("Vorname: ", userObject["prename"])
    print("Nachname: ", userObject["lastname"])
    print("E-mail: ", userObject["e-mail"])
    print("Password: ", userObject["password"])
    print("Gültig: ", userObject["valid"])

    date = userObject["birthday"]
    date_as_string = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    print("Geburtstag: ", date_as_string)

    return


def addUserToList(listOfUserObjects):
    userObject = dict()  # {}
    userObject["prename"] = input("Wie ist dein Vorname? ")
    userObject["lastname"] = input("Wie ist dein Nachname? ")
    userObject["e-mail"] = input("Wie ist deine E-Mail Adresse? ")
    userObject["password"] = input("Wie soll dein Password lauten? ")
    userObject["valid"] = True
    userObject["birthday"] = setDatetime()
    listOfUserObjects.append(userObject)
    return


# In diesem Bereich nichts ändern!
listOfUserObjects = list() # []

userObject = dict()  # {}
userObject["prename"] = "Hans"
userObject["lastname"] = "Peter"
userObject["e-mail"] = "hans@peter.org"
userObject["password"] = "SehrSicher"
userObject["valid"] = True
userObject["birthday"] = datetime(2023, 12, 24)

listOfUserObjects.append(userObject)

userObject = dict()  # {}
userObject["prename"] = "Franz"
userObject["lastname"] = "Meyer"
userObject["e-mail"] = "franzi@web.de"
userObject["password"] = "aefew!"
userObject["valid"] = True
userObject["birthday"] = datetime(2000, 10, 2)

listOfUserObjects.append(userObject)

# Ab hier können Sie Ihr Programm testen
addUserToList(listOfUserObjects)
addUserToList(listOfUserObjects)
printUserObject(listOfUserObjects[0])
