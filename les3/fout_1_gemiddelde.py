"""FOUT 1: dit programma draait. Het antwoord klopt niet.

Voer uit met 10, 20 en 30. Er zou 20.0 moeten uitkomen.
Wat komt eruit? En waarom?
"""

score1 = float(input("Score 1: "))
score2 = float(input("Score 2: "))
score3 = float(input("Score 3: "))

gemiddelde = score1 + score2 + score3 / 3

print(f"Het gemiddelde is {gemiddelde}")
