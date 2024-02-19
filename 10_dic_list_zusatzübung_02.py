from datetime import datetime
# -------------------------------------------------------------------------------------------
    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList? (fertig)
        # Aufgabe 1/ Ein Dictionary?
    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss. (fertig)
    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit. (fertig)
# -------------------------------------------------------------------------------------------


def add_user_to_list(list_of_user_objects):
    user_object = dict()

    user_object["username"] = input("Bitte geben Sie den Benutzernamen ein: ")
    user_object["username"] = input("Bitte geben Sie das Password ein: ")
    user_object["valid"] = True
    user_object["e-mail"] = "lord@kelvin.org"
    user_object["password_changed"] = datetime.now()

    list_of_user_objects.append(user_object)
    return


# -------------------------------------------------------------------------------------------
# Aufgabe 4:
# Erstellen Sie eine Funktion checkYear mit dem Parameter listOfUserObjects.
# Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten. (fertig)
# Aufgabe 5:
# Implementieren Sie nun die Funktion für die Aufgabe 4. Alle Benutzer seit dem
# Jahr 2022 ihr Kennwort nicht geändert haben, werden deaktiviert, in dem der Key valid
# den Value False erhält. (fertig)
# -------------------------------------------------------------------------------------------

def checkYear(list_of_user_objects):
    for user in list_of_user_objects:
        password_changed_year = user["passwordChanged"].year
        if password_changed_year < 2022:
            user["valid"] = False


# Aufgabe 6:
    # Erstellen Sie eine Funktion setValid mit dem Parameter listOfUserObjects.
    # Der Parameter beinhaltet eine Liste mit allen Benutzerobjekten.(fertig)
    # Gehen Sie alle Benutzer der Liste des Parameter durch. Jeder Benutzer, welcher
    # deaktivert wurde (siehe Aufgabe 5) erhält ein neues Passwort. Das Passwort gibt der
    # Anwender über einen input ein. Zudem wird der Value für den valid-Key auf True gesetzt. (Fertig)
# -------------------------------------------------------------------------------------------

def setValid(listOfUserObjects):
    for user in listOfUserObjects:
        if "valid" in user:
            if user["valid"] is False:
                user["password"] = input("Geben Sie das neue Password ein: ")
                user["valid"] = True


# -------------------------------------------------------------------------------------------
    # Aufgabe 7:
    # Prüfen Sie, mittels der Funktion checkMailAdresses(), ob doppelte E-Mail-Adressen vorliegen.
# -------------------------------------------------------------------------------------------
def checkMailAdresses(userList):
    for i, userObject in userList:
        for j in range(i + 1, len(userList)):
            if userObject["e-mail"] == userList[j]["e-mail"]:
                print("Diese E-Mail ist doppelt: ", userObject["e-mail"])

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

# Test

# add_user_to_list(userList)
checkYear(userList)
