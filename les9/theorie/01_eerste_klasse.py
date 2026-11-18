"""DEMO 1: je eerste klasse.

Een klasse is een blauwdruk. Een object is wat je daarmee maakt.
"""

# ---------------------------------------------------------------------------
# 1. Zonder klasse: losse variabelen die bij elkaar horen
# ---------------------------------------------------------------------------

naam_1 = "Sofie"
punten_1 = [14, 12, 18]

naam_2 = "Ahmed"
punten_2 = [9, 11, 7]

print(naam_1, punten_1)
print(naam_2, punten_2)

student_1 = {"naam": "sofie", "punten": [14, 12, 18]}
print(student_1["naam"], student_1["punten"])

# Twee cursisten, en nu al vier variabelen. Bij tien cursisten zijn het er
# twintig, en dan vergeet je er gegarandeerd één.


# ---------------------------------------------------------------------------
# 2. De blauwdruk: een klasse
#
#    class Cursist begint met een hoofdletter. De ingebouwde types die je al
#    kent (str, list, dict) zijn kleine letters, maar dat zijn uitzonderingen:
#    eigen klassen schrijf je met een hoofdletter.
#    __init__ loopt automatisch zodra je een object maakt.
#    self is "dit object", het exemplaar dat je aan het maken bent.
# ---------------------------------------------------------------------------

class Cursist:
    def __init__(self, naam, punten):
        self.naam = naam
        self.punten = punten


# ---------------------------------------------------------------------------
# 3. Objecten maken: de blauwdruk invullen
# ---------------------------------------------------------------------------

sofie = Cursist("Sofie", [14, 12, 18])
ahmed = Cursist("Ahmed", [9, 11, 7])

print(sofie.naam)       # Sofie
print(ahmed.naam)       # Ahmed
print(sofie.punten)     # [14, 12, 18]

print(type(sofie))
# De naam staat na de punt, zonder haakjes: het is data, geen methode.


# ---------------------------------------------------------------------------
# 4. Elk object heeft zijn eigen data
#
#    Twee objecten uit dezelfde klasse delen niets. Dat is precies het punt.
# ---------------------------------------------------------------------------

sofie.punten.append(16)

print(sofie.punten)     # [14, 12, 18, 16]
print(ahmed.punten)     # [9, 11, 7]: onaangeroerd

# Ook een attribuut aanpassen gaat met een punt:

ahmed.naam = "Ahmed B."
print(ahmed.naam)       # Ahmed B.


# ---------------------------------------------------------------------------
# Onthouden
#
#    klasse  = de blauwdruk (Cursist)
#    object  = één exemplaar (sofie, ahmed)
#    self    = de naam die de klasse gebruikt voor "dit exemplaar"
#
#    Klasnamen met een hoofdletter (Cursist), variabelen met een kleine letter
#    (sofie). Dat is de afspraak die iedereen volgt.
# ---------------------------------------------------------------------------
