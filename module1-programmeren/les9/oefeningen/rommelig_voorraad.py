"""Startbestand voor oefening 2: het voorraadoverzicht van de buurtwinkel.

Dit script werkt. Het toont de voorraad van drie artikelen en waarschuwt
wanneer er bijna niets meer ligt.

Jouw opdracht: haal dit uit elkaar en zet het weer in elkaar met een klasse.
De output moet er nadien LETTERLIJK hetzelfde uitzien. Voer dit bestand dus
eerst uit en bewaar wat er op het scherm komt. Dat is je vangnet.
"""


def voorraadwaarde(aantal, prijs):
    return aantal * prijs


def is_bijna_leeg(aantal, minimum=5):
    return aantal < minimum


def toon_artikel(naam, aantal, prijs):
    print(f"{naam:12} {aantal:3} stuks   {voorraadwaarde(aantal, prijs):8.2f} euro")
    if is_bijna_leeg(aantal):
        print(" " * 12 + "  bijna leeg, bestellen")


artikelen = [
    ("Melk", 24, 1.15),
    ("Brood", 3, 2.40),
    ("Kaas", 12, 4.75),
]

print("VOORRAAD BUURTWINKEL")
print("=" * 45)

for naam, aantal, prijs in artikelen:
    toon_artikel(naam, aantal, prijs)

print("=" * 45)
totaal = 0
for naam, aantal, prijs in artikelen:
    totaal = totaal + voorraadwaarde(aantal, prijs)
print(f"Totale voorraadwaarde: {totaal:.2f} euro")
