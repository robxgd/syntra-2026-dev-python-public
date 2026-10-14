"""OPLOSSING 4: tellen met een conditie."""

punten = [12, 7, 15, 9, 18, 10, 4, 14]

geslaagd = 0
gebuisd = 0
even = 0

for punt in punten:
    if punt >= 10:
        geslaagd = geslaagd + 1
    else:
        gebuisd = gebuisd + 1

    # Aparte if: een punt kan geslaagd EN even zijn
    if punt % 2 == 0:
        even = even + 1

print(f"Geslaagd: {geslaagd}")
print(f"Gebuisd: {gebuisd}")
print(f"Even getallen: {even}")
