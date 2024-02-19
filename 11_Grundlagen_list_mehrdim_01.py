reak = list()

for i in range(10):
    row = list()
    index = 15

    while index > 0:
        row.append(index)

        index -= 1

    reak.append(row)

print(reak)

reak[0][2] = 1337
reak[1][2] = 1337

print(reak)