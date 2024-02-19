# 2) Erstellen Sie eine Ausgabe der Gehälter und Namen der Mitarbeiter in aufsteigender Reihenfolge.
# Die Funktion heisst print_salary mit dem Parameter dictionary.
def print_salery(dictionary):
    pass


# 3) Erstellen Sie eine Funktin remove...
def remove_user(user_and_passwords):
    username = input("Wie lautet der Benutzer?")
    safety_question = bool(input("Soll dieser Benutzer wirklich gelöscht werden? (True)"))

    if safety_question:
        if username in user_and_passwords:
            del user_and_passwords[username]
            print(f"Benutzer '{username}' wurde erfolgreich gelöscht.")
        else:
            print(f"Fehler! Benutzer '{username}' existiert nicht.")
    else:
        print("Error! Die Aktion wurde nicht bestätigt.")


def change_password(users_and_passwords):

    username = input("Wie lautet ihr Nutername?")
    old_password = input("Geben Sie ihr altes Password ein: ")

    # Überprüfen, ob der Benutzername im Dictionary vorhanden ist.
    if username in users_and_passwords:
        # Überprüfen, ob das eingegebene alte Passwort mit dem gespeicherten übereinstimmt
        if old_password == users_and_passwords[username]:
            while True:
                new_password = input("Geben Sie ihr neues Passwort ein: ")
                passwords = list(users_and_passwords.values())

                if new_password in passwords:
                    print("Dieses Passwort ist leider bereits vergeben, wählen Sie ein anderes.")
                else:
                    users_and_passwords[username] = new_password
                    print("Das Passwort wurde neu festgelegt.")
                    break
        else:#            
            print("Das eingegebene Passwort stimmt nicht mit dem aktuellen Passwort überein.")
    else:
        print(f"Benutzer '{username}' existiert nicht.")

def check_username(users_and_passwords):
    user_new = input("Geben Sie einen neuen Benutzer ein.")
        for user in users_and_passwords.keys():
            if user_new == user:
                raise Exception("Dieser Benutzer wird bereits verwendet.")




# 1) Erstellen Sie ein Dictionary mit Mitareitern und Gehalt.
employee_salary_dict = dict()

employee_salary_dict["Franz Mayer"] = 2324.5
employee_salary_dict["Hans Petersen"] = 3421.45
employee_salary_dict["Hanz Franz"] = 1421.45
employee_salary_dict["Hans Mayer"] = 5421.45
change_password(employee_salary_dict)
print_salery(employee_salary_dict)

