"""Kassa, voor de randgevallenjacht (oefening 2).

Dit script werkt. Jouw opdracht is niet om het te herstellen,
maar om invoer te vinden waar het op onderuit gaat.
"""

prijs = float(input("Prijs per stuk: "))
aantal = int(input("Aantal: "))
korting_procent = float(input("Korting in procent: "))

subtotaal = prijs * aantal
korting = subtotaal * korting_procent / 100
totaal = subtotaal - korting

print(f"Subtotaal:  {subtotaal} euro")
print(f"Korting:    {korting} euro")
print(f"Te betalen: {totaal} euro")
