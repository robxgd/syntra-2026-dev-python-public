"""FOUT 1: dit programma crasht, maar niet waar je zou denken.

De functie lijkt te werken: er verschijnt 21.0 op het scherm.
Toch crasht regel 14. Waarom?
"""


def btw_berekenen(bedrag):
    print(bedrag * 0.21)


btw = btw_berekenen(100)

print(f"De btw bedraagt {btw + 0} euro")
