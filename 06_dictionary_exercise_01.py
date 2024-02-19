# Übung Gehaltsliste

def employee_salary_search(name_salary_dictionary, comfirm):
    while True:
        name = employee_name()
        if name in name_salary_dictionary:
            print("Das Gehalt von ", name, "beträgt ", name_salary_dictionary[name], " €")
            break
        else:
            print("Der Name ist nicht in der Gehaltsliste vorhanden. Bitte versuchen Sie es erneut.")
            add_new_employee = input("Möchten Sie den Angestellten anlegen?(", comfirm[0], "/", comfirm[4], ")")
            if add_new_employee == comfirm[0] or add_new_employee == comfirm[1]or add_new_employee == comfirm[2] or add_new_employee == comfirm[3]:
                add_employee(name_salary_dictionary, name)
                break
            else:
                continue

# comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
def add_employee(name_salary_dictionary, employee):
    while True:
        name_salary_dictionary[employee] = input("Wie lautet das Gehalt des Angestellten?")

        print("Der Benutzer wurde angelegt.")
        add_emploee_repeat = input("Überprüfen Sie ihre gespeicherte Eingabe bitte: " + name_salary_dictionary[employee] + "\n" + "Ist die Eingabe richtig?")
        if add_emploee_repeat == comfirm[0] or add_emploee_repeat == comfirm[1] or add_emploee_repeat == comfirm[2] or add_emploee_repeat == comfirm[3]:
            break

    print("Das Dictionary hat folgende keys: ")
    print(name_salary_dictionary.keys())

# comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
def employee_change_salary(name_salary_dictionary, comfirm):
    while True:
        employee = employee_name()
        name_salary_dictionary[employee] = float(input("Das neue Gehalt: "))
        print("Das neue Gehalt wurde auf: ", name_salary_dictionary[employee], " € festgelegt.")
        change_salary_repeat = input("Ist die Eingabe richtig? (", comfirm[2],"/", comfirm[6]")")
        if change_salary_repeat == comfirm[2] or change_salary_repeat == comfirm[3]:
            break

# comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
def delete_employee(name_salary_dictionary, comfirm):
    while True:
        name = employee_name()

        if name in name_salary_dictionary:
            name_salary_dictionary.pop(name)
            break
        else:
            print("Dieser Name kann nicht entfernt werden, da er im Dictionary nicht vorhanden ist. ")
            option_continue = input("Möchten Sie es noch einmal versuchen? (", comfirm[4], "/", comfirm[6], ")")
            if option_continue == comfirm[4] or option_continue == comfirm[5]:
                break
# comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
def sum_salary(salary_dic):
    sum = 0.0
    for salary in salary_dic.values():
        sum += salary
    return sum
# comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
def employee_name():
    employee = input("Geben Sie den Vornamen und Nachnamen der Person an, "
                 "dessen Gehalt Sie suchen. \n Beispiel: (Max Mustermann)")
    return employee


# main-Programm
# Key Name, Wert Gehalt
salary_list = {
    "Max Mustermann": 60000,
    "Anna Schmidt": 55000,
    "Michael Müller": 62000,
    "Sarah Fischer": 58000,
    "David Wagner": 60000,
    "Laura Becker": 57000,
    "Paul Schmitt": 59000,
    "Jenny Weber": 60000,
    "Markus Schulz": 63000,
    "Sophie Zimmermann": 56000,
    "Tom Koch": 61000,
    "Julia Richter": 59000,
    "Kevin Berger": 60000,
    "Lisa Hoffmann": 57000,
    "Martin Lehmann": 62000,
    "Nina Klein": 58000,
    "Tim Bauer": 60000,
    "Vanessa Wolf": 59000,
    "Janine Lange": 60000,
    "Felix Arnold": 61000
}
while True:
    comfirm = ["Ja", "ja","J", "j", "Nein", "nein", "N", "n"]
    menu = int(input(" (1) Gehalt eines Mitarbeiters suchen\n (2) Gehalt eines Mitarbeiters ändern\n "
                       "(3) Mitarbeiter hinzufügen\n (4) Mitarbeiter löschen\n (5) Ausgabe der Gehaltsliste\n (6) Programm beenden"))
    print("-------------------------------------------------")

    if menu == 1:
        employee_salary_search(salary_list, comfirm)
    elif menu == 2:
        employee_change_salary(salary_list,comfirm)
    elif menu == 3:
        name = employee_name()
        if salary_list[name]:
            add_employee(salary_list, name)
    elif menu == 4:
        delete_employee(salary_list)
    elif menu == 5:
        print("Ausgabe der gesamten Gehaltsliste:", salary_list)
        print("-------------------------------------------------")
    elif menu == 6:
        break


