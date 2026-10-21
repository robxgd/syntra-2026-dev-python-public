"""DEMO 2: een foutmelding lezen.

Voer dit uit en lees de volledige foutmelding van onder naar boven.
"""


def gemiddelde_van(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    return totaal / len(getallen)


def toon_rapport(naam, getallen):
    gem = gemiddelde_van(getallen)
    print(f"{naam}: gemiddelde {gem:.1f}")


toon_rapport("Wiskunde", [14, 12, 18])
toon_rapport("Frans", [])


# ---------------------------------------------------------------------------
# Wat er verschijnt:
#
#   Traceback (most recent call last):
#     File ".../02_traceback_lezen.py", line 21, in <module>
#       toon_rapport("Frans", [])
#     File ".../02_traceback_lezen.py", line 16, in toon_rapport
#       gem = gemiddelde_van(getallen)
#     File ".../02_traceback_lezen.py", line 12, in gemiddelde_van
#       return totaal / len(getallen)
#   ZeroDivisionError: division by zero
#
# Lees het zo:
#
#   1. ONDERSTE REGEL EERST: dat is wat er misging.
#      ZeroDivisionError: division by zero
#
#   2. DE REGEL DAARBOVEN: dat is waar het misging.
#      regel 12, in gemiddelde_van, bij return totaal / len(getallen)
#
#   3. PAS DAN NAAR BOVEN: dat is hoe je daar geraakt bent.
#      regel 21 riep toon_rapport aan, die riep gemiddelde_van aan.
#
# Veel mensen lezen alleen de eerste regel ("Traceback...") en haken af.
# Begin altijd onderaan.
#
# Merk ook op dat het EERSTE rapport nog gelukt is. De crash zit in het tweede.
#
# De tekens ~~~~^^^^ onder een regel wijzen het exacte STUK van die regel aan
# dat crashte. Hier: len(getallen). Handig bij lange regels met veel bewerkingen.
# ---------------------------------------------------------------------------
