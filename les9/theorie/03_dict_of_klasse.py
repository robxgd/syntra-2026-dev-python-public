"""DEMO 3: wanneer een dictionary, wanneer een klasse.

Een dictionary kan dezelfde data houden. Het verschil is waar het gedrag staat.
"""

# ---------------------------------------------------------------------------
# 1. Dezelfde cursist, als dictionary
# ---------------------------------------------------------------------------

cursist = {"naam": "Sofie", "punten": [14, 12, 18]}

print(cursist["naam"])
print(sum(cursist["punten"]) / len(cursist["punten"]))

# Werkt. Maar de berekening staat buiten de data, en elke keer opnieuw.
# Schrijf je "gemideld" in plaats van "gemiddelde", dan krijg je een KeyError
# en zegt Python niets over wat je bedoelde.


# ---------------------------------------------------------------------------
# 2. Dezelfde cursist, als object
# ---------------------------------------------------------------------------

class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        return sum(self.punten) / len(self.punten)

    def toon(self):
        print(f"{self.naam}: {self.gemiddelde():.1f}")


sofie = Cursist("Sofie", [14, 12, 18])
sofie.toon()                    # Sofie: 14.7

# De berekening zit in de klasse. Eén keer geschreven, overal dezelfde.


# ---------------------------------------------------------------------------
# 3. Een lijst met objecten
#
#    Hier wint de klasse het van de dictionary: één regel in de lus.
# ---------------------------------------------------------------------------

cursisten = [
    Cursist("Sofie", [14, 12, 18]),
    Cursist("Ahmed", [9, 11, 7]),
    Cursist("Lena", [17, 16, 15]),
]

for cursist in cursisten:
    cursist.toon()

# Sofie: 14.7
# Ahmed: 9.0
# Lena: 16.0

# Eén regel in de lus. De data en het gedrag reizen samen: je moet niet weten
# hoe een gemiddelde berekend wordt om er een te tonen.


# ---------------------------------------------------------------------------
# 4. Van een lijst met dictionaries naar een lijst met objecten
# ---------------------------------------------------------------------------

ruwe_data = [
    {"naam": "Sofie", "punten": [14, 12, 18]},
    {"naam": "Ahmed", "punten": [9, 11, 7]},
]

print()
for rij in ruwe_data:
    tijdelijk = Cursist(rij["naam"], rij["punten"])
    tijdelijk.toon()

# Dit is hoe je bijna altijd begint: ruwe data (uit een bestand of een API)
# omzetten naar objecten, en dan met objecten verder werken.


# ---------------------------------------------------------------------------
# Onthouden
#
#    Dictionary: data zonder gedrag. Prima voor een tabel, een JSON-blok,
#    een simpele telling.
#
#    Klasse: data met gedrag dat bij die data hoort, en diezelfde berekening
#    op veel exemplaren.
#
#    Wordt je dictionary een vaste vorm met dezelfde berekeningen erover,
#    dan is dat een klasse die nog geen klasse is.
# ---------------------------------------------------------------------------
