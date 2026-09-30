"""FOUT 2: dit programma draait. De klant betaalt te veel.

Voer uit met bedrag 100 en korting 10.
Er zou 90.0 moeten uitkomen. Wat komt eruit?
"""

bedrag = float(input("Bedrag: "))
korting_procent = float(input("Korting in procent: "))

korting = bedrag * korting_procent / 100
te_betalen = bedrag + korting

print(f"Korting:    {korting} euro")
print(f"Te betalen: {te_betalen} euro")
