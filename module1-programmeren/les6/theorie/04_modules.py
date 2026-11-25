"""DEMO 4: code over meerdere bestanden.

Voer DIT bestand uit. Het gebruikt de functies uit prijzen.py.
Let op: prijzen.py moet in dezelfde map staan.
"""

# ---------------------------------------------------------------------------
# 1. Importeren: haal de functies uit het andere bestand
# ---------------------------------------------------------------------------

import prijzen

print(prijzen.btw_berekenen(100))       # 21.0
print(prijzen.met_btw(100))             # 121.0
print(prijzen.met_btw(100, 6))          # 106.0: ander percentage
print(prijzen.korting_toepassen(100, 10))   # 90.0


# ---------------------------------------------------------------------------
# 2. Of importeer alleen wat je nodig hebt
# ---------------------------------------------------------------------------

from prijzen import met_btw

print(met_btw(50))                      # 60.5: nu zonder "prijzen." ervoor


# ---------------------------------------------------------------------------
# 3. Standaardwaarden voor parameters
#
#    In prijzen.py staat: def btw_berekenen(bedrag, procent=21)
#    Geef je het percentage niet mee, dan wordt 21 gebruikt.
# ---------------------------------------------------------------------------

print(prijzen.btw_berekenen(200))       # 42.0: standaard 21%
print(prijzen.btw_berekenen(200, 6))    # 12.0: expliciet 6%


# ---------------------------------------------------------------------------
# 4. if __name__ == "__main__"
#
#    Zet dit onderaan een bestand dat je ZOWEL wil kunnen uitvoeren
#    ALS importeren. Wat erin staat, draait alleen bij rechtstreeks uitvoeren.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Dit bestand is rechtstreeks uitgevoerd.")

# Importeert iemand dit bestand, dan verschijnt die regel niet.
# Handig om testcode bij je functies te zetten zonder dat ze
# meedraait als een ander bestand jouw functies gebruikt.
