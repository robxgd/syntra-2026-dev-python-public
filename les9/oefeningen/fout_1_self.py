"""FOUT 1: dit programma crasht met een melding over het aantal argumenten.

Je gaf twee argumenten mee. Python zegt dat het er drie kreeg.
Lees de melding en repareer.
"""


class Cursist:
    def __init__(naam, punten):
        self.naam = naam
        self.punten = punten


sofie = Cursist("Sofie", [14, 12, 18])

print(f"{sofie.naam}: {len(sofie.punten)} punten")
