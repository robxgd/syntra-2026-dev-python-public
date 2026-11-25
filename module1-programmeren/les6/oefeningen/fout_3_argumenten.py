"""FOUT 3: dit programma draait. Het antwoord klopt niet.

korting(100, 10) zou 90.0 moeten geven: honderd euro min tien procent.
Wat komt eruit? En waarom crasht het niet?
"""


def korting(procent, bedrag):
    return bedrag - (bedrag * procent / 100)


resultaat = korting(100, 10)

print(f"Na korting: {resultaat} euro")
