"""DEMO 3a: "Klanten krijgen 10% korting vanaf 100 euro."

Lezing A: 10% op het hele bedrag, zodra je 100 haalt.
Draai dit naast 03_korting_b.py. Zelfde zin, ander programma, ander bedrag.
"""

bedrag = 120.00

korting = bedrag * 0.10
te_betalen = bedrag - korting

print(f"Bedrag:     {bedrag} euro")
print(f"Korting:    {korting} euro")
print(f"Te betalen: {te_betalen} euro")
