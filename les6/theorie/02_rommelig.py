"""DEMO 2: het script dat we samen gaan opruimen.

Dit werkt. Voer het uit: het toont een correct rapport.

Dezelfde code staat drie keer, één keer per regio. Dat is wat we gaan opsplitsen.
De opgeruimde versie staat in 03_opgeruimd.py.
"""

verkopen_noord = [120.50, 85.00, 200.00, 45.75]
verkopen_zuid = [310.00, 95.50, 120.00]
verkopen_west = [75.25, 180.00, 240.50, 60.00, 95.00]

print("VERKOOPRAPPORT")
print("=" * 40)

totaal_noord = 0
for bedrag in verkopen_noord:
    totaal_noord = totaal_noord + bedrag
gemiddelde_noord = totaal_noord / len(verkopen_noord)
hoogste_noord = verkopen_noord[0]
for bedrag in verkopen_noord:
    if bedrag > hoogste_noord:
        hoogste_noord = bedrag
print("Regio Noord")
print(f"  Aantal verkopen: {len(verkopen_noord)}")
print(f"  Totaal:          {totaal_noord:.2f} euro")
print(f"  Gemiddelde:      {gemiddelde_noord:.2f} euro")
print(f"  Hoogste:         {hoogste_noord:.2f} euro")

totaal_zuid = 0
for bedrag in verkopen_zuid:
    totaal_zuid = totaal_zuid + bedrag
gemiddelde_zuid = totaal_zuid / len(verkopen_zuid)
hoogste_zuid = verkopen_zuid[0]
for bedrag in verkopen_zuid:
    if bedrag > hoogste_zuid:
        hoogste_zuid = bedrag
print("Regio Zuid")
print(f"  Aantal verkopen: {len(verkopen_zuid)}")
print(f"  Totaal:          {totaal_zuid:.2f} euro")
print(f"  Gemiddelde:      {gemiddelde_zuid:.2f} euro")
print(f"  Hoogste:         {hoogste_zuid:.2f} euro")

totaal_west = 0
for bedrag in verkopen_west:
    totaal_west = totaal_west + bedrag
gemiddelde_west = totaal_west / len(verkopen_west)
hoogste_west = verkopen_west[0]
for bedrag in verkopen_west:
    if bedrag > hoogste_west:
        hoogste_west = bedrag
print("Regio West")
print(f"  Aantal verkopen: {len(verkopen_west)}")
print(f"  Totaal:          {totaal_west:.2f} euro")
print(f"  Gemiddelde:      {gemiddelde_west:.2f} euro")
print(f"  Hoogste:         {hoogste_west:.2f} euro")

print("=" * 40)
eindtotaal = totaal_noord + totaal_zuid + totaal_west
print(f"Eindtotaal: {eindtotaal:.2f} euro")
