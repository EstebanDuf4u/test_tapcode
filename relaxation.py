# NE PAS TOUCHER
events = [11, 5, 15, 10, 13, 7, 8, 4, 9, 14, 11, 6, 8, 5, 7, 14, 11, 7, 12, 10, 3]
# NE PAS TOUCHER

etat = 0
state = ""

for event in events:
    etat += event

    if etat >= 10 and etat <= 15:
        etat = etat - 6

        state = state + "R"

    elif etat >= 15 and etat <= 20:
        etat = etat - 9

        state = state + "M"

    elif etat >= 20:
        etat = etat - 12

        state = state + "Y"


print(state)


