"""DEMO 3b: "Klanten krijgen 10% korting vanaf 100 euro."

Lezing B: 10% op het deel bóven 100.
Zelfde zin als 03_korting_a.py, ander programma, 10 euro verschil.

Allebei verdedigbaar. Geen van beide is fout. De zin was fout.
"""

bedrag = 120.00

deel_boven_100 = bedrag - 100
korting = deel_boven_100 * 0.10
te_betalen = bedrag - korting

print(f"Bedrag:     {bedrag} euro")
print(f"Korting:    {korting} euro")
print(f"Te betalen: {te_betalen} euro")
