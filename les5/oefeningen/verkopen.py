"""Startbestand voor oefening 3: het verkooprapport.

Kopieer deze lijst naar je eigen bestand, of werk verder in dit bestand.
Elke regel is: productnaam;prijs per stuk;aantal verkocht
"""

verkopen = [
    "appel;1.20;3",
    "brood;2.50;1",
    "melk;1.10;2",
    "appel;1.20;5",
    "kaas;4.80;1",
    "melk;1.10;4",
]

# Zo haal je één regel uit elkaar:
regel = verkopen[0]
velden = regel.split(";")

print(velden)                   # ['appel', '1.20', '3']
print(velden[0])                # appel        (tekst)
print(float(velden[1]))         # 1.2          (kommagetal: omzetten!)
print(int(velden[2]))           # 3            (geheel getal: omzetten!)

# Vanaf hier is het aan jou.
