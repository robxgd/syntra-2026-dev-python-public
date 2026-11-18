"""DEMO 2: gedrag hoort bij de data.

Een methode is een functie die in de klasse staat. Ze werkt op self.
"""

# ---------------------------------------------------------------------------
# 1. Een methode met return
#
#    Zelfde regel als in les 6: berekenen doet return, tonen doet print.
# ---------------------------------------------------------------------------

class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        return sum(self.punten) / len(self.punten)


sofie = Cursist("Sofie", [14, 12, 18])
print(sofie.gemiddelde())       # 14.666666666666666

# Binnen de klasse lees je de data via self.punten, niet via sofie.punten.
# De klasse weet niet dat het object straks sofie heet.


# ---------------------------------------------------------------------------
# 2. Een methode die de data wijzigt
# ---------------------------------------------------------------------------

class Cursist2:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        return sum(self.punten) / len(self.punten)

    def voeg_punt_toe(self, punt):
        self.punten.append(punt)

    def is_geslaagd(self, grens=10):
        return self.gemiddelde() >= grens


ahmed = Cursist2("Ahmed", [9, 11, 7])
print(ahmed.gemiddelde())       # 9.0
print(ahmed.is_geslaagd())      # False

ahmed.voeg_punt_toe(16)
print(ahmed.gemiddelde())       # 10.75
print(ahmed.is_geslaagd())      # True

# Twee keer False, dan twee keer True: de methode leest de data van dit
# object, op het moment dat je ze aanroept.


# ---------------------------------------------------------------------------
# 3. Het verschil tussen data en een methode: de haakjes
# ---------------------------------------------------------------------------

print(ahmed.naam)               # Ahmed: data, geen haakjes
print(ahmed.gemiddelde)         # <bound method ...>: de methode zelf
print(ahmed.gemiddelde())       # 10.75: nu voer je ze uit

# Vergeet je de haakjes, dan print je de methode in plaats van het resultaat.
# Dat is geen fout die crasht, je ziet alleen onzin op het scherm. Precies
# het soort stille fout van les 7.


# ---------------------------------------------------------------------------
# 4. self is dit object, niet het vorige
# ---------------------------------------------------------------------------

sofie2 = Cursist2("Sofie", [14, 12, 18])
print(sofie2.gemiddelde())      # 14.666666666666666
print(ahmed.gemiddelde())       # 10.75

# Dezelfde methode, twee verschillende antwoorden. self wijst bij elke
# oproep naar het object voor de punt.


# ---------------------------------------------------------------------------
# Onthouden
#
#    Een methode is een functie met self vooraan.
#    self.attribuut leest of wijzigt de data van dít object.
#    Methode aanroepen: object.methode(), met haakjes.
# ---------------------------------------------------------------------------
