# NE PAS TOUCHER
projets = ['2023-10-16;30', '2023-12-08;29', '2023-10-13;30', '2024-03-13;33', '2024-02-16;12', '2023-12-15;40', '2023-10-05;31', '2023-11-29;38', '2023-12-28;14']
# NE PAS TOUCHER




# NE PAS TOUCHER
projets = ['2023-10-16;30', '2023-12-08;29', '2023-10-13;30', '2024-03-13;33', '2024-02-16;12', '2023-12-15;40', '2023-10-05;31', '2023-11-29;38', '2023-12-28;14']
# NE PAS TOUCHER


def parse_date(projet):
    date_str, duree = projet.split(';')
    annee, mois, jour = map(int, date_str.split('-'))
    return annee, mois, jour, int(duree)


def jour_dans_annee(annee, mois, jour):
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # année bissextile
    if annee == 2024:
        jours_par_mois[1] = 29

    total = 0
    for m in range(mois - 1):
        total += jours_par_mois[m]

    total += jour
    return total


def datetodaynumber(annee, mois, jour):
    # base = 2023-09-01
    base = jour_dans_annee(2023, 9, 1)

    if annee == 2023:
        return jour_dans_annee(annee, mois, jour) - base

    elif annee == 2024:
        # jours restants de 2023
        jours_2023 = jour_dans_annee(2023, 12, 31) - base

        return jours_2023 + jour_dans_annee(2024, mois, jour)


def project_by_date(projets):
    projets_par_date = []
    for projet in projets:
        annee, mois, jour, duree = parse_date(projet)
        date_num = datetodaynumber(annee, mois, jour)
        projets_par_date.append((date_num, duree))
    return sorted(projets_par_date)


def project_intervals(projets):
    intervals = []

    for projet in project_by_date(projets):
        debut, duree = projet
        fin = debut + duree - 1
        intervals.append((debut, fin))

    return intervals


def surcharges(intervals):
    surcharge = 0

    # trouver le plus petit début
    # trouver le plus grand fin
    min_debut = min(debut for debut, _ in intervals)
    max_fin = max(fin for _, fin in intervals)

    for jour in range(min_debut, max_fin + 1):
        nb = 0

        for debut, fin in intervals:
            if debut <= jour <= fin:
                nb += 1

        if nb >= 2:
            surcharge += nb - 1

    return surcharge

def projet_interals_procrastination(projets):
    intervals = []

    for debut , duree in project_by_date(projets):
        nouvelle_duree = duree + duree //10
        fin = debut + nouvelle_duree - 1
        intervals.append((debut, fin))

    return intervals


normal = surcharges(project_intervals(projets))
procrastination = surcharges(projet_interals_procrastination(projets))
print(str(normal) + "_" + str(procrastination))