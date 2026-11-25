punten = [8, 10, 14, -1, 21, 7]

geslaagd = []
niet_geslaagd = []
ongeldig = []

for punt in punten:
    if punt > 10:
        geslaagd.append(punt)
    else:
        niet_geslaagd.append(punt)

print("Geslaagd:", geslaagd)
print("Niet geslaagd:", niet_geslaagd)
print("Ongeldig:", ongeldig)
