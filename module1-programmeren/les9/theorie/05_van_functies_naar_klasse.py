"""DEMO 5: het rapport van les 6, nu met een klasse.

Les 6 loste dit op met vier functies en een lijst per regio. Hier komt dezelfde
uitkomst uit een klasse. Vergelijk het met demo/03_opgeruimd.py uit les 6.
"""

# ---------------------------------------------------------------------------
# 1. Wat er in les 6 stond, in het kort
#
#    totaal_van(bedragen)       -> functie met een lijst als parameter
#    gemiddelde_van(bedragen)   -> functie met een lijst als parameter
#    toon_regio(naam, bedragen) -> functie met twee parameters
#
#    Elke functie krijgt de data opnieuw aangereikt. Dat werkt, en het is
#    oneindig beter dan het rommelige script. Maar de regio is nergens een
#    ding: het is een naam in een variabele en een lijst ernaast.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 2. Dezelfde berekeningen, nu binnen een klasse
# ---------------------------------------------------------------------------

class Regio:
    def __init__(self, naam, bedragen):
        self.naam = naam
        self.bedragen = bedragen

    def totaal(self):
        return sum(self.bedragen)

    def gemiddelde(self):
        return self.totaal() / len(self.bedragen)

    def hoogste(self):
        return max(self.bedragen)

    def toon(self):
        print(f"Regio {self.naam}")
        print(f"  Aantal verkopen: {len(self.bedragen)}")
        print(f"  Totaal:          {self.totaal():.2f} euro")
        print(f"  Gemiddelde:      {self.gemiddelde():.2f} euro")
        print(f"  Hoogste:         {self.hoogste():.2f} euro")


# ---------------------------------------------------------------------------
# 3. De objecten, en het rapport
# ---------------------------------------------------------------------------

regios = [
    Regio("Noord", [120.50, 85.00, 200.00, 45.75]),
    Regio("Zuid", [310.00, 95.50, 120.00]),
    Regio("West", [75.25, 180.00, 240.50, 60.00, 95.00]),
    Regio("Oost", [310.00, 99.50, 100.00])
]

print("VERKOOPRAPPORT")
print("=" * 40)

for regio in regios:
    regio.toon()

print("=" * 40)
eindtotaal = sum(regio.totaal() for regio in regios)
print(f"Eindtotaal: {eindtotaal:.2f} euro")

# Dezelfde output als in les 6. Andere vorm, zelfde resultaat: dat is de test.


# ---------------------------------------------------------------------------
# 4. Het vierde verkoopgebied
#
#    In les 6: twee regels (de lijst en één toon_regio(...)).
#    Hier: één regel, want de lijst met objecten staat er al.
# ---------------------------------------------------------------------------

# regios.append(Regio("Oost", [88.00, 132.40]))

print()
print("De klant wil een vierde regio: één regel erbij, en de lus print hem mee.")


# ---------------------------------------------------------------------------
# Onthouden
#
#    Een klasse bundelt de data (naam, bedragen) met de berekeningen die
#    erbij horen. Je geeft de bedragen niet meer door aan elke functie: het
#    object heeft ze al.
#
#    Bij één losse berekening is een functie prima. Zodra je dezelfde data
#    door drie of vier functies sleept, is dat een klasse die nog geen klasse
#    is.
#
#    Dit is de vorm die je nodig hebt om bestaande code met klassen te lezen.
# ---------------------------------------------------------------------------
