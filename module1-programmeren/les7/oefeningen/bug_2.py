"""BUG 2: syntaxfout, iets subtieler dan bug 1.

Voer uit en lees de foutmelding letterlijk. Ze vertelt je precies
wat er ontbreekt, zonder omwegen.

Deze fout maak je vooral bij lange regels. Wat is de gewoonte die
hem voorkomt?
"""

prijzen = [12.50, 8.00, 21.75

totaal = 0
for prijs in prijzen:
    totaal = totaal + prijs

print(f"Totaal: {totaal}")
