# -------------------------------------------------------------------------------------------
# Aufgabe 1 (x Punkte)
# Erstellen Sie eine Funktion printUserObject mit dem Parameter userObject.
# Der Parameter enthält ein dict, welches in der Funktion addUserToList
# definiert wurde.
# Geben Sie alle Keys und Values des dicts in folgender Darstellung aus:
# Vorname: Lord
# Nachname: Kelvin
# ...
# Den Geburtstag des Users geben Sie im folgenden Format aus: yyyy-mm-dd (fertig)
# -------------------------------------------------------------------------------------------
from datetime import datetime

def setDatetime():
    year = int(input("Geburtsjahr: "))
    month = int(input("Monat: "))
    day = int(input("Tag: "))

    return datetime(year, month, day)

def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["prename"] = input("Vorname: ")
    userObject["lastname"] = input("Nachname: ")
    userObject["e-mail"] = "lord@kelvin.org"
    userObject["password"] = "SehrSicher"
    userObject["valid"] = True
    userObject["birthday"] = setDatetime()

    listOfUserObjects.append(userObject)

def printUserObject(userObject): # 1 Punkt
    # Variante 1
    print("Vorname:", userObject["prename"])
    print("Nachname:", userObject["lastname"])
    print("e-mail:", userObject["e-mail"])
    print("password:", userObject["password"])

    date = userObject["birthday"]
    date_as_string = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    print("Geburtstag", date_as_string)

    # Variante 2
    for key in userObject.keys():
        print(key + ":", userObject[key])

# -------------------------------------------------------------------------------------------
    # Aufgabe 2 (xx Punkten)
    # Implementieren Sie die Rückgabe aller aktiven Benutzer als Liste von Strings.
    # Jeder String hat dabei das Format "Nachname, Vorname".
    # Ein Benutzer ist dann Aktiv, wenn der Value zum Key "valid" True ist. (fertig)
# -------------------------------------------------------------------------------------------
def checkValidUsers(listOfUserObjects):
    validUsers = list()
    for userObject in listOfUserObjects:
        if userObject["valid"]: # oder if item["valid"] == True:
            validUsers.append(userObject["lastname"] + ", " + userObject["prename"])
    return validUsers

# -------------------------------------------------------------------------------------------
    # Aufgabe 3 (xx Punkte)
    # Implementieren Sie die Eingabe eines Benutzernamens durch den Anwender.
    # Ist der Benutzername in der Liste der Benutzer vorhanden, arbeiten Sie
    # mit dem gefundenen Objekts weiter. Andernfalls geben Sie eine Fehler-
    # meldung aus. Der Benutzername entspricht der E-Mail-Adresse. (fertig)
# -------------------------------------------------------------------------------------------
def changePassword(listOfUserObjects):
    username = input("Geben Sie den Benutzernamen ein: ")
    user = None

    for userObject in listOfUserObjects:
        if userObject["e-mail"] == username:
            user = userObject
            break

    if user == None:
        print("Unbekannter Benutzer")
        return

# -------------------------------------------------------------------------------------------
    # Aufgabe 4 (xx Punkte)
    # Der Benutzer wird nun zur Eingabe eines neuen Passworts aufgefordert.
    # Das Passwort darf nicht von einem anderen Benutzer in der Liste ver-
    # wendet werden. Wird ein doppeltes Passwort vergeben, muss ein neues
    # Passwort eingegeben werden. Die Eingabe des Passworts wiederholt sich
    # so lange, bis das neue Passwort erfolgreich gesetzt wird.
# -------------------------------------------------------------------------------------------
    user["password"] = input("Geben Sie das neue Passwort ein: ")
    for userObject in listOfUserObjects:
        if (userObject["password"] == user["password"] and userObject["e-mail"] != user["e-mail"]):
            print("Passwort bereits vorhanden.")

            while userObject["password"] == user["password"]:
                user["password"] = input("Geben Sie das neue Passwort ein: ")


# Main-File
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
print("TEST")
printUserObject(listOfUserObjects[0])

validUsers = checkValidUsers(listOfUserObjects)
print(validUsers)

for fullname in validUsers:
    print(fullname)
#printUserObject(listOfUserObjects[0])