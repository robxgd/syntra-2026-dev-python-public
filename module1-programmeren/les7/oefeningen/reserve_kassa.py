"""Reservebestand voor oefening 3, voor wie geen huistaak mee heeft.

Dit programma werkt bij nette invoer en gaat onderuit bij alles daarbuiten.
Jouw opdracht: maak het robuust.
"""

print("=== KASSA ===")

naam = input("Productnaam: ")
prijs = float(input("Prijs per stuk: "))
aantal = int(input("Aantal: "))
korting_procent = float(input("Korting in procent: "))

subtotaal = prijs * aantal
korting = subtotaal * korting_procent / 100
totaal = subtotaal - korting

print(f"{aantal} x {naam}")
print(f"Subtotaal:  {subtotaal:.2f} euro")
print(f"Korting:    {korting:.2f} euro")
print(f"Te betalen: {totaal:.2f} euro")
