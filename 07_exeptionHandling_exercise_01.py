# Aufgabe 1
#
# Erstellen Sie eine Funktion check_username mit dem Parameter users_and_passwords.
# Die Funktion prüft, ob ein Benutzername vorhanden ist, welcher der Anwender zuvor
# eingegeben hat. Falls der Benutzer nicht vorhanden ist, wird eine Exception geworfen.
def check_username(users_and_passwords):
    username = input("Geben Sie einen Benutzernamen ein: ")

    if username in users_and_passwords.keys():
        print("Benutzer vorhanden")
    else:
        raise KeyError("Benutzer " + username + " nicht gefunden")

# Aufgabe 2
#
# Erstellen Sie eine Funktion login_user mit dem Parameter users_and_passwords.
# Die Funktion ruft zuerst die Funktion check_username auf. Wird keine Exception ausgegeben,
# wird der Benutzername gespeichert und das Kennwort zu den Benutzernamen geprüft.


users_and_passwords = dict()
users_and_passwords["otto"] = "abcd1234"
users_and_passwords["franz"] = "qwert"
users_and_passwords["peter"] = "§Q$rgw3f098uzhbg"
users_and_passwords["sigfried"] = "qwert"

try:
    check_username(users_and_passwords)
except KeyError:
    print("Benutzer wurde nicht gefunden")