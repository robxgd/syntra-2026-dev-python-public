"""DEMO 1: de drie soorten fouten, na de API-intro met PokéAPI."""

# ---------------------------------------------------------------------------
# 1. SYNTAXFOUT: draait niet, Python zegt meteen waar
#
#    Haal het commentaarteken weg. Het bestand start niet eens op.
#    VS Code onderstreept dit al vóór je uitvoert.
# ---------------------------------------------------------------------------

# print("hallo"


# ---------------------------------------------------------------------------
# 2. RUNTIMEFOUT: draait, crasht onderweg
#
#    De regels ervoor worden nog uitgevoerd. Dan stopt het.
# ---------------------------------------------------------------------------

print("Deze regel verschijnt nog")
# print(10 / 0)                 # ZeroDivisionError
print("Deze ook, zolang de vorige in commentaar staat")


# ---------------------------------------------------------------------------
# 3. LOGISCHE FOUT: draait, crasht niet, geeft het verkeerde antwoord
#
#    Geen foutmelding. Geen onderstreping in VS Code. Niets.
# ---------------------------------------------------------------------------

scores = [10, 20, 30]

totaal = 0
for score in scores:
    totaal = totaal + score

gemiddelde = totaal / 2          # moet len(scores) zijn

print(f"Gemiddelde: {gemiddelde}")      # 30.0, en dat is fout


# ---------------------------------------------------------------------------
# Samengevat:
#
#   syntaxfout    → je merkt het meteen, de editor onderstreept het
#   runtimefout   → je merkt het bij het uitvoeren
#   logische fout → je merkt het misschien nooit
#
# De hele avond gaat over die derde categorie, en over hoe je de tweede
# netjes opvangt.
# ---------------------------------------------------------------------------
