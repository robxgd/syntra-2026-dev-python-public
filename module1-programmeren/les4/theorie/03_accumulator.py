"""DEMO 3: het accumulator-patroon.

Vier bewerkingen die er verschillend uitzien maar hetzelfde patroon volgen:

    1. maak een variabele klaar VOOR de lus
    2. pas hem aan BINNEN de lus
    3. gebruik hem NA de lus
"""

scores = [12, 15, 9, 18, 14]


# ---------------------------------------------------------------------------
# 1. Optellen
# ---------------------------------------------------------------------------

totaal = 0                      # VOOR
for score in scores:
    totaal = totaal + score     # BINNEN
print(f"Totaal: {totaal}")      # NA  → 68


# ---------------------------------------------------------------------------
# 2. Tellen hoeveel er aan een voorwaarde voldoen
# ---------------------------------------------------------------------------

geslaagd = 0
for score in scores:
    if score >= 14:
        geslaagd = geslaagd + 1
print(f"Geslaagd: {geslaagd}")  # → 3


# ---------------------------------------------------------------------------
# 3. De grootste zoeken
# ---------------------------------------------------------------------------

grootste = scores[0]            # begin met de EERSTE, niet met 0
for score in scores:
    if score > grootste:
        grootste = score
print(f"Grootste: {grootste}")  # → 18

# Waarom niet grootste = 0?
# Omdat dat fout gaat zodra alle waarden negatief zijn:
temperaturen = [-3, -7, -1, -9]

fout = 0
for t in temperaturen:
    if t > fout:
        fout = t
print(f"Fout antwoord: {fout}")     # → 0, en 0 staat niet in de lijst

goed = temperaturen[0]
for t in temperaturen:
    if t > goed:
        goed = t
print(f"Goed antwoord: {goed}")     # → -1


# ---------------------------------------------------------------------------
# 4. Filteren: een nieuwe lijst opbouwen
# ---------------------------------------------------------------------------

geslaagden = []                     # VOOR
for score in scores:
    if score >= 14:
        geslaagden.append(score)    # BINNEN
print(f"Geslaagden: {geslaagden}")  # NA  → [15, 18, 14]


# ---------------------------------------------------------------------------
# 5. Het gemiddelde: optellen en delen
# ---------------------------------------------------------------------------

totaal = 0
for score in scores:
    totaal = totaal + score

gemiddelde = totaal / len(scores)
print(f"Gemiddelde: {gemiddelde}")  # → 13.6

# En nu het randgeval uit les 2:
lege_lijst = []
# totaal = 0
# for score in lege_lijst:
#     totaal = totaal + score
# print(totaal / len(lege_lijst))   # ZeroDivisionError: commentaar weghalen
#
# In les 2 stond "wat als er nul zijn?" op het bord. Hier gebeurt het.
