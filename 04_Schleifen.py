run = True

while run == True:
        gender = input("Geben Sie Ihr Geschlecht (m/w/d) ein: ")

        if gender == "m" or gender == "d" or gender == "w":
            break
        else:
            print("Eingabe unzulässig.")
print("Sie haben als Geschlecht ", gender, " gewählt.")
