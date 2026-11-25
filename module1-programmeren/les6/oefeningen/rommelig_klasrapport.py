"""Startbestand voor oefening 2: dit script werkt, maar is rommelig.

Voer het eerst uit en noteer de output. Die output moet ná je opruiming
nog exact hetzelfde zijn.
"""

wiskunde = [14, 12, 18, 9, 16]
frans = [11, 15, 13, 8]
labo = [17, 19, 15, 12, 18, 14]

print("KLASRAPPORT")
print("-" * 35)

totaal_wiskunde = 0
for punt in wiskunde:
    totaal_wiskunde = totaal_wiskunde + punt
gem_wiskunde = totaal_wiskunde / len(wiskunde)
geslaagd_wiskunde = 0
for punt in wiskunde:
    if punt >= 10:
        geslaagd_wiskunde = geslaagd_wiskunde + 1
print("Wiskunde")
print(f"  Leerlingen: {len(wiskunde)}")
print(f"  Gemiddelde: {gem_wiskunde:.1f}")
print(f"  Geslaagd:   {geslaagd_wiskunde}")

totaal_frans = 0
for punt in frans:
    totaal_frans = totaal_frans + punt
gem_frans = totaal_frans / len(frans)
geslaagd_frans = 0
for punt in frans:
    if punt >= 10:
        geslaagd_frans = geslaagd_frans + 1
print("Frans")
print(f"  Leerlingen: {len(frans)}")
print(f"  Gemiddelde: {gem_frans:.1f}")
print(f"  Geslaagd:   {geslaagd_frans}")

totaal_labo = 0
for punt in labo:
    totaal_labo = totaal_labo + punt
gem_labo = totaal_labo / len(labo)
geslaagd_labo = 0
for punt in labo:
    if punt >= 10:
        geslaagd_labo = geslaagd_labo + 1
print("Labo")
print(f"  Leerlingen: {len(labo)}")
print(f"  Gemiddelde: {gem_labo:.1f}")
print(f"  Geslaagd:   {geslaagd_labo}")

print("-" * 35)
