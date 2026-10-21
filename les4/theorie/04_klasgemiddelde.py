"""DEMO 4: de opdracht uit les 2, nu als werkend programma.

In les 2 verzamelden we op het bord: wat gaat erin, wat komt eruit,
wat kan misgaan. Die lijst was de specificatie. Nu bouwen we hem.
"""

# ===========================================================================
# BLOK A: wat er in les 2 op het bord stond
# ===========================================================================
#
# Opdracht: "Bereken de gemiddelde score van een klas."
#
# Wat gaat erin?    de scores, aantal onbekend
# Wat komt eruit?   één getal, afgerond op twee cijfers
# Wat kan misgaan?  nul scores · negatieve score · geen getal · komma ·
#                   score boven het maximum · lege invoer
#
# Stappen:
#   1. vraag hoeveel scores er zijn
#   2. lees ze één voor één in en bewaar ze in een lijst
#   3. tel ze op
#   4. deel door het aantal
#   5. toon het gemiddelde


# ===========================================================================
# BLOK B: dezelfde stappen, met code ertussen
# ===========================================================================

# 1. vraag hoeveel scores er zijn
aantal = int(input("Hoeveel scores? "))

# 2. lees ze één voor één in en bewaar ze in een lijst
scores = []
teller = 0
while teller < aantal:
    score = float(input(f"Score {teller + 1}: "))
    scores.append(score)
    teller = teller + 1

# 3. tel ze op
totaal = 0
for score in scores:
    totaal = totaal + score

# 4. deel door het aantal
gemiddelde = totaal / len(scores)

# 5. toon het gemiddelde
print(f"Aantal scores: {len(scores)}")
print(f"Gemiddelde:    {gemiddelde:.2f}")


# ---------------------------------------------------------------------------
# Live testen met de lijst van les 2:
#
#   3 scores: 12, 15, 18   → Gemiddelde 15.00
#   1 score:  14           → Gemiddelde 14.00
#   0 scores               → ZeroDivisionError: division by zero
#   score 12,5             → ValueError (de komma)
#   score abc              → ValueError
#   score -5               → wordt gewoon meegerekend, geen foutmelding
#   score 150              → wordt gewoon meegerekend, geen foutmelding
#
# Vijf van de zes randgevallen die ze in les 2 bedachten, gebeuren hier echt.
# We leren ze in les 7 opvangen; nu volstaat het dat de analyse klopte.
# ---------------------------------------------------------------------------
