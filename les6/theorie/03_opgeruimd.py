"""DEMO 3: hetzelfde rapport, opgeruimd.

Voer beide uit (dit en 02_rommelig.py): de output is identiek. Dat is de test.

52 coderegels werden er 35, maar zeg er niet bij dat opsplitsen "korter"
maakt. Mét de docstrings erbij is dit bestand zelfs lánger.

Het punt is niet lengte. Het punt is dat "verander het gemiddelde in een
mediaan" nu één plaats is in plaats van drie.
"""


def totaal_van(bedragen):
    """Tel alle bedragen op."""
    totaal = 0
    for bedrag in bedragen:
        totaal = totaal + bedrag
    return totaal


def gemiddelde_van(bedragen):
    """Bereken het gemiddelde bedrag."""
    return totaal_van(bedragen) / len(bedragen)


def hoogste_van(bedragen):
    """Zoek het hoogste bedrag."""
    hoogste = bedragen[0]
    for bedrag in bedragen:
        if bedrag > hoogste:
            hoogste = bedrag
    return hoogste


def toon_regio(naam, bedragen):
    """Toon het rapportblok voor één regio."""
    print(f"Regio {naam}")
    print(f"  Aantal verkopen: {len(bedragen)}")
    print(f"  Totaal:          {totaal_van(bedragen):.2f} euro")
    print(f"  Gemiddelde:      {gemiddelde_van(bedragen):.2f} euro")
    print(f"  Hoogste:         {hoogste_van(bedragen):.2f} euro")


verkopen_noord = [120.50, 85.00, 200.00, 45.75]
verkopen_zuid = [310.00, 95.50, 120.00]
verkopen_west = [75.25, 180.00, 240.50, 60.00, 95.00]

print("VERKOOPRAPPORT")
print("=" * 40)

toon_regio("Noord", verkopen_noord)
toon_regio("Zuid", verkopen_zuid)
toon_regio("West", verkopen_west)

print("=" * 40)
eindtotaal = totaal_van(verkopen_noord) + totaal_van(verkopen_zuid) + totaal_van(verkopen_west)
print(f"Eindtotaal: {eindtotaal:.2f} euro")


# ---------------------------------------------------------------------------
# De klant wil een vierde regio. Hoeveel regels pas je aan?
#
#   rommelig:  ongeveer 20 regels kopiëren en overal de naam aanpassen
#   opgeruimd: twee regels: de lijst, en één toon_regio(...)
#
# Dát is waarom je opsplitst. Niet omdat het korter is.
# ---------------------------------------------------------------------------
