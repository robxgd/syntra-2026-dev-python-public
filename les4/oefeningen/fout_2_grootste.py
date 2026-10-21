"""FOUT 2: dit programma draait. Bij deze lijst klopt het antwoord zelfs.

Voer het eerst uit zoals het staat: je krijgt 24. Correct.

Vervang dan de lijst door de wintertemperaturen op de tweede regel
(wissel de commentaartekens om) en voer opnieuw uit.
Er zou -1 moeten uitkomen. Wat komt eruit?
"""

# temperaturen = [12, 18, 7, 21, 15, 9, 24]
temperaturen = [-3, -7, -1, -9]

# hoogste = 0
hoogste = temperaturen[0]

for temperatuur in temperaturen[1:]:
    print(f"we vergelijken {hoogste} met {temperatuur}")
    if temperatuur > hoogste:
        hoogste = temperatuur

print(f"Hoogste temperatuur: {hoogste}")
