"""FOUT 3: dit programma draait en geeft het juiste antwoord.

Voer het uit: gemiddelde 15.0. Klopt.

Voeg dan een zesde score toe aan de lijst, bijvoorbeeld 21,
en voer opnieuw uit. Nu klopt het niet meer. Waarom?
"""

scores = [12, 15, 9, 18, 21]

totaal = 0
for score in scores:
    totaal = totaal + score

gemiddelde = totaal / 5

print(f"Gemiddelde: {gemiddelde}")
