def my_value_check(value):
    try:
        value_as_int = int(value)
    except ValueError:
        raise ValueError

    if value_as_int > 100 or value_as_int < 0:
        raise OverflowError("Value is not in range.")

    print("Value is in range")

try:
    my_value_check("a")

except ValueError:
    print("Das war keine Ganzzahl")
except OverflowError:
    print("Zahl ist außerhalb des Wertebereichs")
except:
    print("Hier ist etwas Anderes falsch gelaufen.")
finally:
    print("Dieser Teil wird auf jeden Fall ausgeführt.")