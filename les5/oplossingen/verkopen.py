# Analyse: invoer is een lijst product;prijs;aantal, uitvoer een verkooprapport.
# Aannames: drie velden, geldige getallen, niet-negatieve prijzen en aantallen.
# Taken: must: regels splitsen en omzetten; must: stuks en omzet verzamelen;
# must: totaal tonen; should: hoogste omzet zoeken; could: sorteren.
# Definition of Done:
# [x] Herhaalde producten worden samengevoegd.
# [x] Stuks zijn 8, 1, 6 en 1 voor appel, brood, melk en kaas.
# [x] Totale omzet is 23.50 euro.
# [x] Appel heeft de hoogste omzet: 9.60 euro.
# [x] Bedragen verschijnen met twee decimalen.

verkopen = [
    "appel;1.20;3", "brood;2.50;1", "melk;1.10;2",
    "appel;1.20;5", "kaas;4.80;1", "melk;1.10;4",
]

stuks = {}
omzet = {}
totaal = 0

for regel in verkopen:
    velden = regel.split(";")
    naam = velden[0]
    prijs = float(velden[1])
    aantal = int(velden[2])

    stuks[naam] = stuks.get(naam, 0) + aantal
    omzet[naam] = omzet.get(naam, 0) + prijs * aantal
    totaal = totaal + prijs * aantal

for naam, bedrag in omzet.items():
    print(f"{naam}: {stuks[naam]} stuks, {bedrag:.2f} euro")

print(f"Totale omzet: {totaal:.2f} euro")

beste_naam = ""
beste_omzet = 0
for naam, bedrag in omzet.items():
    if bedrag > beste_omzet:
        beste_naam = naam
        beste_omzet = bedrag
print(f"Hoogste omzet: {beste_naam} ({beste_omzet:.2f} euro)")
