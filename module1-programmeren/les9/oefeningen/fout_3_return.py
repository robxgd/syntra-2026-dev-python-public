"""FOUT 3: dit programma crasht op een rare plaats.

Het toont eerst een naam, en crasht dan met een melding over NoneType.
De oorzaak staat niet op de regel waar het misgaat.
"""


class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def totaal(self):
        return sum(self.punten)


class Klas:
    def __init__(self, cursisten):
        self.cursisten = cursisten

    def beste(self):
        beste = self.cursisten[0]
        for cursist in self.cursisten:
            if cursist.totaal() > beste.totaal():
                beste = cursist
        print(beste.naam)


klas = Klas([
    Cursist("Sofie", [14, 12, 18]),
    Cursist("Ahmed", [9, 11, 7]),
])

winnaar = klas.beste()

print(f"Beste cursist: {winnaar[0]}")
