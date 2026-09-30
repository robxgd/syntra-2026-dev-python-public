"""FOUT 4: dit programma draait. Kinderen betalen het volle pond.

Bedoeling: onder 12 betaal je 6 euro, 65-plus betaalt 9 euro, de rest 12 euro.

Voer uit met leeftijd 10. Er zou 6 moeten uitkomen.
Wat komt eruit? Er verschijnt geen enkele foutmelding.
"""

leeftijd = int(input("Hoeveel jaar is de bezoeker? "))

if leeftijd < 65:
    prijs = 12
elif leeftijd < 12:
    prijs = 6
else:
    prijs = 9

print(f"De toegangsprijs is {prijs} euro.")
