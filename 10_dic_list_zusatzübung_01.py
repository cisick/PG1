# -------------------------------------------------------------------------------------------
    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList? (fertig)
        # Aufgabe 1/ Ein Dictionary?
    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss. (fertig)
    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit. (fertig)
# -------------------------------------------------------------------------------------------
from datetime import datetime

def addUserToList(listOfUserObjects):
    userObject = dict() # {}
    # zu 2)
    userObject["username"] = input("Bitte geben Sie den Benutzernahmen ein: ")
    userObject["password"] = input("Bitte geben Sie das Password ein: ")
    userObject["valid"] = True
    # zu 3)
    userObject["passwordChanged"] = datetime.now()
    userObject["e-mail"] = "lord@kelvin.org"

    listOfUserObjects.append(userObject)
# -------------------------------------------------------------------------------------------
    # Aufgabe 4:
    # Erstellen Sie eine Funktion checkYear mit dem Parameter listOfUserObjects.
    # Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten. (fertig)
    # Aufgabe 5:
    # Implementieren Sie nun die Funktion für die Aufgabe 4. Alle Benutzer seit dem
    # Jahr 2022 ihr Kennwort nicht geändert haben, werden deaktiviert, in dem der Key valid
    # den Value False erhält. (fertig)
# -------------------------------------------------------------------------------------------
def checkYear(listOfUserObjects):
    # zu 5)
    for userObject in listOfUserObjects:
        if "passwordChanged" in userObject:
            password_changed_year = userObject["passwordChanged"].year
            if password_changed_year < 2022:
                userObject["valid"] = False
# -------------------------------------------------------------------------------------------
    # Aufgabe 6:
    # Erstellen Sie eine Funktion setValid mit dem Parameter listOfUserObjects.
    # Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten.(fertig)
    # Gehen Sie alle Benutzer der Liste des Parameter durch. Jeder Benutzer, welcher
    # deaktivert wurde (siehe Aufgabe 5) erhält ein neues Passwort. Das Passwort gibt der
    # Anwender über einen input ein. Zudem wird der Value für den valid-Key auf True gesetzt. (Fertig)
# -------------------------------------------------------------------------------------------
def setValid(listOfUserObjects):
    for userObject in listOfUserObjects:
        if "valid" in userObject:
            if userObject["valid"] == False:
                userObject["password"] = input("Geben Sie ein neues Password ein: ")
                userObject["valid"] = True
# -------------------------------------------------------------------------------------------
    # Aufgabe 7:
    # Prüfen Sie, mittels der Funktion checkMailAdresses(), ob doppelte E-Mail-Adressen vorliegen.
# -------------------------------------------------------------------------------------------
def checkMailAdresses(listOfUserObjects):
    counter = 1

    for userObject in listOfUserObjects:
        for i in range(counter, len(listOfUserObjects), 1):
            if userObject["e-mail"] == listOfUserObjects[i]["e-mail"]:
                print("Diese E-Mail ist doppelt:", userObject["e-mail"])

        counter += 1

# -------------------------------------------------------------------------------------------
    # In dem folgenden Bereich nehmen Sie keine Änderungen vor!
    # Testdaten:
# -------------------------------------------------------------------------------------------
userList = list()

user = dict()
user["username"] = "peter.meyer"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "jule@meyer.de"

userList.append(user)

user = dict()
user["username"] = "franz.huber"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "hubi@gmx.de"

userList.append(user)

user = dict()
user["username"] = "julia.meyer"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "jule@meyer.de"

userList.append(user)

user = dict()
user["username"] = "otto.schulze"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "otto@schulze.de"

userList.append(user)

user = dict()
user["username"] = "gerd.mueller"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "otto@schulze.de"

userList.append(user)

user = dict()
user["username"] = "lui.hansel"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "lui@hansel.de"

userList.append(user)

# -------------------------------------------------------------------------------------------
    # Ab hier können Sie Ihre Lösungen testen:
# -------------------------------------------------------------------------------------------
checkYear(userList)

print("Viel Erfolg!")