# NE PAS TOUCHER
forme = 17
concentration = 19
sommeil = 12
humeur = 18
equations = ['SC:2S2H3C2F', 'SN:5C3H4F1S', 'FM:7C4F9S6H', 'FF:2H4S4C5F', 'SI:4H2C5S5F', 'PT:3H2F5S4C']
repas = ['SI', 'FM', 'FF', 'PT', 'FF', 'FF', 'SI', 'SC', 'SN', 'PT', 'FF', 'FM', 'FM', 'SI', 'SC', 'SN', 'SN', 'SC', 'SN', 'SC', 'SI', 'FM', 'SN', 'FM', 'PT', 'SI', 'SC', 'FF', 'SC', 'FM', 'SC']
# NE PAS TOUCHER

dico = {}

for eq in equations:
    code, effets = eq.split(":")
    dico[code] = effets

for rep in repas:
    effets = dico[rep]

    if rep in ["SC", "SN", "FM"]:
        signe = 1
    else:
        signe = -1

    i = 0
    while i < len(effets):
        valeur = int(effets[i])
        lettre = effets[i + 1]

        if lettre == "F":
            forme = forme + signe * valeur
            if forme < 5:
                forme = 5
            if forme > 25:
                forme = 25

        elif lettre == "C":
            concentration = concentration + signe * valeur
            if concentration < 5:
                concentration = 5
            if concentration > 25:
                concentration = 25

        elif lettre == "H":
            humeur = humeur + signe * valeur
            if humeur < 5:
                humeur = 5
            if humeur > 25:
                humeur = 25

        elif lettre == "S":
            sommeil = sommeil + signe * valeur
            if sommeil < 5:
                sommeil = 5
            if sommeil > 25:
                sommeil = 25

        i = i + 2

print(forme * concentration * humeur * sommeil)