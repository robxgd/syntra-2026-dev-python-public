"""DEMO 4: voorkomen in plaats van opvangen.

try/except vangt op wat misgaat.
Validatie zorgt dat het niet misgaat.

Je hebt allebei nodig, maar voor verschillende dingen.
"""

# ---------------------------------------------------------------------------
# 1. De randgevallenlijst van les 2 is nu je validatiecode
#
#    De zes vragen: nul · negatief · geen getal · komma · te groot · leeg.
#    Elk van die vragen wordt hier één controle.
# ---------------------------------------------------------------------------

def leeftijd_controleren(tekst):
    """Geef een foutmelding terug, of None als alles in orde is."""

    if tekst.strip() == "":                     # leeg
        return "Vul een leeftijd in."

    tekst = tekst.replace(",", ".")             # komma → punt

    try:
        leeftijd = float(tekst)
    except ValueError:                          # geen getal
        return "Dat is geen getal."

    if leeftijd < 0:                            # negatief
        return "Een leeftijd kan niet negatief zijn."

    if leeftijd > 130:                          # te groot
        return "Dat lijkt geen realistische leeftijd."

    return None                                 # alles in orde


# Testen zonder input():
for invoer in ["30", "", "abc", "-5", "200", "12,5"]:
    fout = leeftijd_controleren(invoer)
    if fout is None:
        print(f"{invoer!r:8} → in orde")
    else:
        print(f"{invoer!r:8} → {fout}")


# ---------------------------------------------------------------------------
# 2. Blijven vragen tot het klopt
# ---------------------------------------------------------------------------

# while True:
#     invoer = input("Leeftijd: ")
#     fout = leeftijd_controleren(invoer)
#     if fout is None:
#         leeftijd = float(invoer.replace(",", "."))
#         break
#     print(fout)
#
# print(f"Dank je. Je bent {leeftijd:.0f} jaar.")
#
# Haal dit commentaar weg en voer uit met wat onzin-invoer.
# Het programma blijft rustig doorvragen in plaats van te crashen.


# ---------------------------------------------------------------------------
# 3. Wanneer wat?
#
#   VALIDATIE     voor alles wat je kan controleren vóór je het gebruikt:
#                 gebruikersinvoer, waarden uit een bestand, parameters.
#
#   TRY/EXCEPT    voor alles wat pas tijdens het uitvoeren kan mislukken en
#                 waar je niets aan kan doen: een bestand dat verdwenen is,
#                 een netwerk dat wegvalt.
#
#   NIETS DOEN    voor je eigen bugs. Die moeten crashen, anders vind je ze nooit.
# ---------------------------------------------------------------------------
