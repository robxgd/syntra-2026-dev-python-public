"""FOUT 1: dit programma crasht.

Bedoeling: van elk product tonen hoeveel er in voorraad zijn.
Voor producten die er niet zijn, moet er 0 komen.

Voer uit en lees de foutmelding. Welke sleutel ontbreekt?
"""

voorraad = {"appel": 12, "peer": 5, "banaan": 0}

boodschappenlijst = ["appel", "kiwi", "peer"]

for product in boodschappenlijst:
    aantal = voorraad[product]
    print(f"{product}: {aantal} stuks")
