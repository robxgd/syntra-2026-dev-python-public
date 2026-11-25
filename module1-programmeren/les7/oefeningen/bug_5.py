"""BUG 5: logische fout. Dit programma crasht NIET.

Bedoeling: tellen hoeveel leerlingen geslaagd zijn (12 of meer op 20).
Er zijn er vier geslaagd. Wat telt het programma?
"""

punten = [14, 8, 12, 17, 9, 15]

geslaagd = 0
for punt in punten:
    if punt > 12:
        geslaagd = geslaagd + 1

print(f"Aantal geslaagd: {geslaagd}")
