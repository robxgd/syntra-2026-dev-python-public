"""DEMO: code die draait, er goed uitziet, en toch fout is.


Let op: verzonnen functies
(`lijst.add()`, `random.pick()`) crashen meteen en zijn dus onschuldig. Je
merkt ze op het moment zelf. Code die stilletjes het verkeerde antwoord geeft,
merkt niemand op, en die gaat mee tot in productie.

We voeren enkele voorbeelden uit:
"""


# ---------------------------------------------------------------------------
# Een functie zoals een AI-assistent ze zou voorstellen bij de vraag
# "schrijf een functie die het gemiddelde van een lijst getallen berekent".
#
# Ze is niet verzonnen. Ze is niet lelijk. Ze werkt zelfs. Meestal.
# ---------------------------------------------------------------------------

def gemiddelde(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    return totaal / len(getallen)


# --- TEST 1: het gelukkige geval -------------------------------------------
# Dit werkt. Hier stoppen de meeste mensen met testen. Dat is de fout.

print("Test 1:", gemiddelde([10, 20, 30]))          # → 20.0  ✅


# --- TEST 2: de lege lijst -------------------------------------------------
# Haal het commentaarteken weg en voer uit.
# → ZeroDivisionError: division by zero
#
# Dit soort fouten zouden we moeten zien aankomen:
# len([]) is 0, en delen door 0 kan niet. Dit is "redeneren over code",
#  waar les 2 helemaal over gaat.

# print("Test 2:", gemiddelde([]))                  # → 💥 crash


# --- TEST 3: DE BELANGRIJKSTE ----------------------------------------------
# Haal het commentaarteken weg en voer uit.

# print("Test 3:", gemiddelde(["10", "20", "30"]))

# Wat gebeurt er?

# Dus toch een crash. Goed. Maar bekijk nu deze variant:

def gemiddelde_variant(getallen):
    totaal = ""
    for getal in getallen:
        totaal = totaal + getal
    return len(totaal) / len(getallen)


print("Test 3b:", gemiddelde_variant(["10", "20", "30"]))
#
# → 2.0
#
# GEEN crash. Een keurig getal. Volledig fout.
# Het gemiddelde van 10, 20 en 30 is 20, niet 2.
# Waarom krijgen we 2 terug?
# Dít is waarom "het draait" nooit betekent "het klopt".


# ---------------------------------------------------------------------------
# DE DRIE MANIEREN OM AI-OUTPUT TE VALIDEREN
#
# Regel voor deze opleiding, en voor het examen:
#   Code die je niet kan uitleggen, lever je niet in.
# ---------------------------------------------------------------------------
