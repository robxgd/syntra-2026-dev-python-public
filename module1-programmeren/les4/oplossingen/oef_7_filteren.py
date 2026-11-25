"""OPLOSSING 7: een nieuwe lijst opbouwen."""

punten = [14, 8, 17, 5, 12, 9, 19]

geslaagd = []
gebuisd = []

for punt in punten:
    if punt >= 10:
        geslaagd.append(punt)
    else:
        gebuisd.append(punt)

print(f"Geslaagd: {geslaagd}")
print(f"Aantal geslaagd: {len(geslaagd)}")
print(f"Gebuisd: {gebuisd}")
