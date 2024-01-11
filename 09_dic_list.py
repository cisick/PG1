from datetime import datetime


def setDateTime():
    year = int("Geburtsjahr: ")
    month = int("Monat: ")
    day = int("Tag: ")
    return datetime(year, month, day)


def addUserToList(listOfUserObjects):
    userObject = dict()

    userObject["prename"] = input("Vorname: ")
    userObject["lastname"] = input("Nachname: ")
    userObject["e-mail"] = input("E-Mail: ")
    userObject["password"] = input("Password: ")
    userObject["valid"] = True
    userObject["birthday"] = setDateTime()


