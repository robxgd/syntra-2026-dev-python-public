"""BUG 4: runtimefout in een functie.

Bedoeling: per klant het gemiddelde bestelbedrag tonen.
De eerste klant lukt. De tweede niet. Lees de traceback van onder naar boven.
"""


def gemiddeld_bedrag(bestellingen):
    totaal = 0
    for bedrag in bestellingen:
        totaal = totaal + bedrag
    return totaal / len(bestellingen)


klanten = {
    "Peeters": [45.00, 32.50, 61.00],
    "Janssens": [],
    "De Smet": [120.00],
}

for naam, bestellingen in klanten.items():
    print(f"{naam}: {gemiddeld_bedrag(bestellingen):.2f} euro")
