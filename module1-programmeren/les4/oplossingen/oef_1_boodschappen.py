"""OPLOSSING 1: een lijst maken en aanpassen."""

boodschappen = ["melk", "brood", "kaas", "appels"]

print(boodschappen[0])          # melk
print(boodschappen[-1])         # appels
print(len(boodschappen))        # 4

boodschappen.append("eieren")
boodschappen.remove("brood")    # verwijdert de WAARDE "brood"

print(boodschappen)             # ['melk', 'kaas', 'appels', 'eieren']
