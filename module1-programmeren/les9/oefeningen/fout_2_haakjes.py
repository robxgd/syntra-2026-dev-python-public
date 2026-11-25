"""FOUT 2: dit programma crasht niet. Het toont onzin.

Er zou een gemiddelde moeten staan. Repareer, en zoek vooral waarom je geen
enkele foutmelding kreeg.
"""


class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        return sum(self.punten) / len(self.punten)


sofie = Cursist("Sofie", [14, 12, 18])

print(f"Gemiddelde: {sofie.gemiddelde}")
