"""Een module: een bestand met functies die andere bestanden kunnen gebruiken.

Dit bestand doe je NIET rechtstreeks uitvoeren. Het wordt geïmporteerd
door 04_modules.py.

Probeer het toch eens uit te voeren: er gebeurt niets zichtbaars.
Dat klopt: er staan alleen definities in, geen oproepen.
"""


def btw_berekenen(bedrag, procent=21):
    """Bereken de btw over een bedrag. Standaard 21 procent."""
    return bedrag * procent / 100


def met_btw(bedrag, procent=21):
    """Geef het bedrag inclusief btw."""
    return bedrag + btw_berekenen(bedrag, procent)


def korting_toepassen(bedrag, procent):
    """Trek een kortingspercentage van het bedrag af."""
    return bedrag - (bedrag * procent / 100)
