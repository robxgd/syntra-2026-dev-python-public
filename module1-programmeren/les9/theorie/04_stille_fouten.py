"""DEMO 4: de vier fouten die iedereen maakt.

Alle vier draaien door, of crashen met een melding die je niet meteen
thuisbrengt. Haal de commentaartekens weg om ze te zien.
"""


class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        return sum(self.punten) / len(self.punten)


# ---------------------------------------------------------------------------
# FOUT 1: self vergeten in de definitie
#
#    Python geeft de eerste parameter altijd het object mee. Zonder self
#    belandt het object in "naam" en de echte naam in "punten".
# ---------------------------------------------------------------------------

class Fout1:
    def __init__(naam, punten):         # geen self
        print(f"aangemaakt met: {naam}")


# fout = Fout1("Sofie", [14, 12])       # TypeError: __init__() takes 2 positional
                                        # arguments but 3 were given

# De melding zegt "3 argumenten, 2 verwacht". Je gaf er toch twee? Het derde
# is het object zelf. Wie dat weet, leest de melding in één keer.
#
# VS Code onderlijnt self al vóór je het bestand uitvoert, met dezelfde
# melding. Zo zie je de fout zonder te draaien.



# ---------------------------------------------------------------------------
# FOUT 2: de haakjes vergeten bij het aanroepen
# ---------------------------------------------------------------------------

sofie = Cursist("Sofie", [14, 12, 18])

print(sofie.gemiddelde())       # 14.666666666666666
print(sofie.gemiddelde)         # <bound method Cursist.gemiddelde of ...>

# Geen crash, geen foutmelding. Je print de methode in plaats van het
# resultaat, en in een groter programma zoek je je rot.


# ---------------------------------------------------------------------------
# FOUT 3: print() in plaats van return in een methode
#
#    Exact dezelfde fout als in les 6, nu binnen een klasse.
# ---------------------------------------------------------------------------

class Fout3:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten

    def gemiddelde(self):
        print(sum(self.punten) / len(self.punten))      # print, geen return


ahmed = Fout3("Ahmed", [9, 11, 7])
ahmed.gemiddelde()                  # 9.0 verschijnt
# print(ahmed.gemiddelde() + 1)     # TypeError: NoneType + int

# Het getal staat op het scherm, dus het lijkt te werken. Tot je ermee
# verder wil rekenen.


# ---------------------------------------------------------------------------
# FOUT 4: een lijst als standaardwaarde
#
#    De standaardwaarde wordt één keer gemaakt, bij het definiëren van de
#    klasse, en daarna door alle objecten gedeeld.
# ---------------------------------------------------------------------------

class Fout4:
    def __init__(self, naam, punten=[]):        # deelbaar
        self.naam = naam
        self.punten = punten


a = Fout4("Sofie")
b = Fout4("Ahmed")

a.punten.append(14)

print(a.punten)     # [14]
print(b.punten)     # [14]: Ahmed heeft plots ook een punt

# De oplossing: None als standaardwaarde, en dan een nieuwe lijst maken.

class Goed4:
    def __init__(self, naam, punten=None):
        self.naam = naam
        self.punten = punten if punten is not None else []


c = Goed4("Sofie")
d = Goed4("Ahmed")
c.punten.append(14)

print(c.punten)     # [14]
print(d.punten)     # []: zoals het moet


# ---------------------------------------------------------------------------
# Onthouden
#
#    self nooit vergeten, ook niet in __init__.
#    Aanroepen met haakjes, anders krijg je de methode zelf.
#    return in een methode die iets berekent, print in een methode die toont.
#    Nooit een lijst of dictionary als standaardwaarde, gebruik None.
# ---------------------------------------------------------------------------
