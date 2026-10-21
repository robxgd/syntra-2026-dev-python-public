# Oplossing: Maak de dictionary één keer aan, vóór de lus.

zin = "de kat zat op de mat en de kat sliep"
woorden = zin.split()

tellingen = {}
for woord in woorden:
    tellingen[woord] = tellingen.get(woord, 0) + 1

print(tellingen)
