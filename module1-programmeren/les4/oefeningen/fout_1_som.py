"""FOUT 1: dit programma draait. Het totaal klopt niet.

De lijst telt op tot 60. Wat komt eruit? En waarom?
"""

prijzen = [10, 20, 30]

totaal = 0
for prijs in prijzen:
    totaal = totaal + prijs

print(f"Totaal: {totaal}")
