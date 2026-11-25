"""DEMO 1: de rekening delen. Werkt prima, tot je er iets raars in gooit."""

bedrag = float(input("Totaalbedrag: "))
personen = int(input("Aantal personen: "))

per_persoon = bedrag / personen

print(f"Elk {per_persoon} euro")


# ---------------------------------------------------------------------------
# Vier gevallen:
#
#   1. bedrag 12.50 · personen 4    → 3.125 euro
#      Werkt. Maar 3,125 euro bestaat niet. Wie betaalt de halve cent?
#
#   2. bedrag 12,50 · personen 4    → ValueError
#      De komma. Iedereen in dit lokaal typt bedragen met een komma.
#
#   3. bedrag 12.50 · personen 0    → ZeroDivisionError
#      Delen door nul.
#
#   4. bedrag 12.50 · personen -4   → -3.125 euro
#      GEEN crash. Een negatief bedrag per persoon. Het programma zegt niets.
#
# Geval 2 en 3 merk je meteen. Geval 4 niet. Dat is waarom je randgevallen
# vooraf bedenkt in plaats van erop te wachten.
# ---------------------------------------------------------------------------
