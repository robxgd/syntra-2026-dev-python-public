"""FOUT 2: dit programma draait. De telling klopt niet.

Bedoeling: tellen hoe vaak elk woord voorkomt.

"de" komt drie keer voor in de zin. Wat toont het programma?
En waarom staat er bij élk woord hetzelfde?
"""

zin = "de kat zat op de mat en de kat sliep"
woorden = zin.split()

for woord in woorden:
    tellingen = {}
    tellingen[woord] = tellingen.get(woord, 0) + 1

print(tellingen)
