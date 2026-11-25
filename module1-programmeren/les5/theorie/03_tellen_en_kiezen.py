"""DEMO 3: tellen met een dictionary, en de keuze lijst-of-dictionary.

Blok 1 is het patroon dat ze het vaakst nodig hebben.
Blok 2 en 3 beantwoorden de vraag "wanneer neem ik wat?".
"""

# ---------------------------------------------------------------------------
# 1. Voorkomens tellen: hét dictionary-patroon
# ---------------------------------------------------------------------------

zin = "de kat zat op de mat en de kat sliep"
woorden = zin.split()

tellingen = {}                                      # VOOR de lus
for woord in woorden:
    tellingen[woord] = tellingen.get(woord, 0) + 1  # BINNEN
print(tellingen)                                    # NA

# Lees die middelste regel hardop:
#   "pak de huidige stand voor dit woord (of 0 als het er nog niet was),
#    tel er één bij op, en zet het terug."
#
# Zonder .get() zou de eerste keer een KeyError geven.

for woord, aantal in tellingen.items():
    if aantal > 1:
        print(f"{woord} komt {aantal} keer voor")


# ---------------------------------------------------------------------------
# 2. Dezelfde vraag met twee lijsten: het kan, maar het is lastig
# ---------------------------------------------------------------------------

namen = ["Jan", "Ali", "Sofie"]
scores = [12, 18, 15]

# "Welke score heeft Sofie?": je moet eerst haar positie zoeken:
gezocht = "Sofie"
for plaats, naam in enumerate(namen):
    if naam == gezocht:
        print(f"{gezocht} heeft {scores[plaats]}")

# En je moet zelf bewaken dat beide lijsten even lang blijven.
# Voegt iemand een naam toe zonder score, dan klopt alles daarna niet meer.


# ---------------------------------------------------------------------------
# 3. Dezelfde vraag met een dictionary: één regel
# ---------------------------------------------------------------------------

resultaten = {"Jan": 12, "Ali": 18, "Sofie": 15}

print(resultaten["Sofie"])          # 15

# De vuistregel:
#   zoek je op VOLGORDE of loop je alles af?   → lijst
#   zoek je op NAAM, code of sleutel?          → dictionary


# ---------------------------------------------------------------------------
# 4. De grootste zoeken in een dictionary
#
#    Zelfde accumulator-patroon als les 4, maar nu onthoud je twee dingen:
#    de beste sleutel én de beste waarde.
# ---------------------------------------------------------------------------

beste_naam = ""
beste_score = 0

for naam, score in resultaten.items():
    if score > beste_score:
        beste_naam = naam
        beste_score = score

print(f"Hoogste: {beste_naam} met {beste_score}")   # Ali met 18

# Zelfde valkuil als les 4: beste_score = 0 gaat fout zodra alle
# waarden negatief kunnen zijn.
