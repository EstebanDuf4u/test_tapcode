# NE PAS TOUCHER
positives = ['Euphorie', 'Joie', 'Admiration', 'Empathie']
negatives = ['Malaise', 'Peur', 'Honte', 'Inquiétude']
emotions = ['Euphorie', 'Malaise', 'Honte', 'Curiosité', 'Attente', 'Malaise', 'Euphorie', 'Peur', 'Honte', 'Empathie', 'Observation', 'Admiration', 'Malaise', 'Observation', 'Observation', 'Malaise', 'Observation', 'Peur', 'Joie', 'Malaise', 'Curiosité', 'Malaise', 'Attente']
# NE PAS TOUCHER

cpositives = 0
cnegatives = 0
for emotion in emotions:
    if emotion in positives:
        cpositives += 1
    elif emotion in negatives:
        cnegatives += 1

result = str(cpositives) + "_" + str(cnegatives)
print(result)