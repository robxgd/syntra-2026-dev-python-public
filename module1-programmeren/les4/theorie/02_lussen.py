"""DEMO 2: lussen.

Een lus doet dezelfde bewerking op veel dingen, zonder copy-paste.
"""

scores = [12, 15, 9, 18, 14]


# ---------------------------------------------------------------------------
# 1. Zonder lus: zo zou je het moeten schrijven
# ---------------------------------------------------------------------------

print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])


# ---------------------------------------------------------------------------
# 2. Met lus: hetzelfde, ongeacht hoeveel er zijn
# ---------------------------------------------------------------------------

for score in scores:
    print(score)

# Lees dit als: "voor elke score in scores, doe het volgende."
# Alles wat INGESPRONGEN staat, hoort bij de lus.


# ---------------------------------------------------------------------------
# 3. Inspringen bepaalt wat er bij de lus hoort
# ---------------------------------------------------------------------------

for score in scores:
    print(f"Score: {score}")
print("Klaar")              # staat NIET ingesprongen → gebeurt één keer

for score in scores:
    print(f"Score: {score}")
    print("Klaar")          # WEL ingesprongen → gebeurt vijf keer


# ---------------------------------------------------------------------------
# 4. range(): tellen zonder lijst
# ---------------------------------------------------------------------------

for i in range(5):
    print(i)                # 0 1 2 3 4: begint bij 0, stopt VOOR de 5

for i in range(1, 6):
    print(i)                # 1 2 3 4 5: van 1 tot en met 5


# ---------------------------------------------------------------------------
# 5. enumerate(), als je én de plaats én de waarde nodig hebt
# ---------------------------------------------------------------------------

for plaats, score in enumerate(scores, start=1):
    print(f"Leerling {plaats}: {score}")


# ---------------------------------------------------------------------------
# 6. Lus + conditie: hier klikt het meestal
# ---------------------------------------------------------------------------

for score in scores:
    if score >= 14:
        print(f"{score}: geslaagd")
    else:
        print(f"{score}: niet geslaagd")


# ---------------------------------------------------------------------------
# 7. while: herhalen zolang iets waar is
# ---------------------------------------------------------------------------

teller = 0
while teller < 3:
    print(f"Ronde {teller}")
    teller = teller + 1     # ZONDER deze regel stopt het nooit

print("Klaar")


# ---------------------------------------------------------------------------
# 8. De oneindige lus
#
#    Haal het commentaar weg, voer uit, en stop met Ctrl+C in de terminal.
# ---------------------------------------------------------------------------

# teller = 0
# while teller < 3:
#     print("dit stopt nooit")
