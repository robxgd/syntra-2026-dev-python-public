"""DEMO 2: dictionaries.

Een lijst zoekt op VOLGORDE: scores[0], scores[1]...
Een dictionary zoekt op SLEUTEL: voorraad["appel"].

Blok per blok tonen en uitvoeren.
"""

# ---------------------------------------------------------------------------
# 1. Aanmaken en opzoeken
# ---------------------------------------------------------------------------

voorraad = {"appel": 12, "peer": 5, "banaan": 0}

print(voorraad)                 # {'appel': 12, 'peer': 5, 'banaan': 0}
print(voorraad["appel"])        # 12
print(len(voorraad))            # 3: aantal sleutels


# ---------------------------------------------------------------------------
# 2. Een sleutel die niet bestaat, crasht
#
#    Haal het commentaarteken weg en toon het.
# ---------------------------------------------------------------------------

# print(voorraad["kiwi"])       # KeyError: 'kiwi'


# ---------------------------------------------------------------------------
# 3. .get() crasht niet
# ---------------------------------------------------------------------------

print(voorraad.get("kiwi"))         # None: bestaat niet
print(voorraad.get("kiwi", 0))      # 0, met een terugvalwaarde
print(voorraad.get("appel", 0))     # 12

# Let op het verschil met blok 2: .get() geeft stilletjes iets terug.
# Handig, maar je merkt dus NIET dat de sleutel ontbrak.

print("kiwi" in voorraad)           # False: expliciet controleren


# ---------------------------------------------------------------------------
# 4. Toevoegen en wijzigen: dezelfde schrijfwijze
# ---------------------------------------------------------------------------

voorraad["kiwi"] = 8            # bestaat niet → wordt toegevoegd
voorraad["appel"] = 15          # bestaat wel  → wordt overschreven
print(voorraad)                 # {'appel': 15, 'peer': 5, 'banaan': 0, 'kiwi': 8}

# Dat is een valkuil: een tikfout in de sleutel voegt stil een nieuw
# product toe in plaats van het bestaande te wijzigen.
voorraad["Appel"] = 99          # hoofdletter A → een ANDER product
print(voorraad)


# ---------------------------------------------------------------------------
# 5. Verwijderen
# ---------------------------------------------------------------------------

del voorraad["Appel"]
print(voorraad)


# ---------------------------------------------------------------------------
# 6. Doorlopen met een lus
# ---------------------------------------------------------------------------

# Alleen de sleutels:
for product in voorraad:
    print(product)

# Sleutel én waarde: dit gebruik je het vaakst:
for product, aantal in voorraad.items():
    print(f"{product}: {aantal} stuks")


# ---------------------------------------------------------------------------
# 7. Lus + conditie, zoals in les 4
# ---------------------------------------------------------------------------

for product, aantal in voorraad.items():
    if aantal == 0:
        print(f"{product} is uitverkocht")
