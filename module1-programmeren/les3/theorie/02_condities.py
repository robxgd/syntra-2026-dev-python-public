"""DEMO 2: beslissingen nemen.

Blok per blok tonen en uitvoeren.
"""

# ---------------------------------------------------------------------------
# 1. Vergelijken levert True of False op
# ---------------------------------------------------------------------------

print(5 > 3)            # True
print(5 == 3)           # False
print(5 != 3)           # True
print(5 >= 5)           # True

# Let op: == vergelijkt, = kent toe. Dit is een klassieke verwarring.


# ---------------------------------------------------------------------------
# 2. if / elif / else
# ---------------------------------------------------------------------------

leeftijd = 30

if leeftijd < 18:
    print("Jeugdtarief")
elif leeftijd < 65:
    print("Volwassentarief")
else:
    print("Seniorentarief")


# ---------------------------------------------------------------------------
# 3. De VOLGORDE van elif bepaalt alles
#
#    Hieronder staat dezelfde bedoeling, maar met de takken omgedraaid.
#    Een kind van 10 krijgt nu het volwassentarief, en niets crasht.
# ---------------------------------------------------------------------------

leeftijd = 10

if leeftijd < 65:
    print("FOUT: Volwassentarief")     # 10 is inderdaad < 65, dus deze wint
elif leeftijd < 18:
    print("Jeugdtarief")               # wordt nooit bereikt

# Python leest van boven naar beneden en stopt bij de eerste tak die klopt.
# Zet daarom altijd de smalste voorwaarde eerst.


# ---------------------------------------------------------------------------
# 4. and / or / not
# ---------------------------------------------------------------------------

leeftijd = 20
student = True

if leeftijd < 26 and student:
    print("Studentenkorting")

if leeftijd < 18 or leeftijd >= 65:
    print("Verlaagd tarief")

if not student:
    print("Geen studentenkorting")


# ---------------------------------------------------------------------------
# 5. Nesten kan, maar elif leest beter
# ---------------------------------------------------------------------------

punten = 72

# Zo schrijven beginners het:
if punten >= 50:
    if punten >= 70:
        if punten >= 85:
            print("Onderscheiding")
        else:
            print("Voldoende, ruim")
    else:
        print("Voldoende")
else:
    print("Onvoldoende")

# Zelfde logica, plat:
if punten >= 85:
    print("Onderscheiding")
elif punten >= 70:
    print("Voldoende, ruim")
elif punten >= 50:
    print("Voldoende")
else:
    print("Onvoldoende")
