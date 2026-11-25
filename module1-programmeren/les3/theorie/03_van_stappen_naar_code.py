"""DEMO 3: de werkwijze van de module: eerst de stappen, dan de code.

Het commentaar blijft staan als de code er is. Dat is geen slordigheid;
het is de structuur van je programma, in gewone taal.
"""

# ===========================================================================
# BLOK A: wat we op het bord zetten VOOR er code komt
# ===========================================================================
#
# Opdracht van de klant:
#   "Bereken de toegangsprijs. Kinderen onder 12 betalen 6 euro,
#    volwassenen 12 euro, 65-plussers 9 euro."
#
# Wat gaat erin?    de leeftijd van de bezoeker
# Wat komt eruit?   de prijs in euro
# Wat kan misgaan?  geen getal · negatief · leeg · een komma · heel groot
#
# Stappen:
#   1. vraag de leeftijd
#   2. zet de invoer om naar een geheel getal
#   3. bepaal het tarief op basis van de leeftijd
#   4. toon de prijs


# ===========================================================================
# BLOK B: dezelfde stappen, nu met code ertussen
# ===========================================================================

# 1. vraag de leeftijd
leeftijd_tekst = input("Hoeveel jaar is de bezoeker? ")

# 2. zet de invoer om naar een geheel getal
leeftijd = int(leeftijd_tekst)

# 3. bepaal het tarief op basis van de leeftijd
if leeftijd < 12:
    prijs = 6
elif leeftijd >= 65:
    prijs = 9
else:
    prijs = 12

# 4. toon de prijs
print(f"De toegangsprijs is {prijs} euro.")


# ---------------------------------------------------------------------------
# Na afloop live testen met de randgevallen van les 2:
#
#   11 → 6     12 → 12     64 → 12     65 → 9      (de grenzen)
#   -5 → 6     ← een leeftijd van min vijf krijgt kindertarief. Geen foutmelding.
#   abc → ValueError: invalid literal for int() with base 10: 'abc'
#   leeg → ValueError
#
# De grenzen (11/12 en 64/65) zijn waar beginners het vaakst één naast zitten.
# ---------------------------------------------------------------------------


