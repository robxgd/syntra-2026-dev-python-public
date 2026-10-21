# Oplossing: Gebruik get met 0 als standaard voor onbekende producten.

voorraad = {"appel": 12, "peer": 5, "banaan": 0}

boodschappenlijst = ["appel", "kiwi", "peer"]

for product in boodschappenlijst:
    aantal = voorraad.get(product, 0)
    print(f"{product}: {aantal} stuks")
