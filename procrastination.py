# NE PAS TOUCHER
projets = ['2023-10-16;30', '2023-12-08;29', '2023-10-13;30', '2024-03-13;33', '2024-02-16;12', '2023-12-15;40', '2023-10-05;31', '2023-11-29;38', '2023-12-28;14']
# NE PAS TOUCHER

def parse_projet(projet):
    date_str, score_str = projet.split(';')
    year, month, day = map(int, date_str.split('-'))
    score = int(score_str)
    parsed_projet = [year, month, day, score]
    return (year, month, day), score
print(parse_projet(projets[0]))
def calculate_end():
    year
