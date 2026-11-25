"""DEMO 1: strings. Hiermee start je de les.

Blok per blok tonen en uitvoeren.
Kernidee: tekst is ook een reeks. Alles wat je met een lijst kon, kan hier ook.
"""

zin = "Python is een programmeertaal"


# ---------------------------------------------------------------------------
# 1. Een string gedraagt zich als een lijst van letters
# ---------------------------------------------------------------------------

print(len(zin))         # 29
print(zin[0])           # P: tellen begint bij nul, net als bij lijsten
print(zin[-1])          # l: laatste teken

for letter in "Python":
    print(letter)       # P y t h o n, elk op een regel


# ---------------------------------------------------------------------------
# 2. Maar: een string kan je NIET wijzigen
#
#    Haal het commentaarteken weg en laat het crashen.
# ---------------------------------------------------------------------------

# zin[0] = "J"          # TypeError: 'str' object does not support item assignment

# Je maakt altijd een NIEUWE string:
nieuw = "J" + zin[1:]
print(nieuw)            # Jython is een programmeertaal


# ---------------------------------------------------------------------------
# 3. split(): van één string naar een lijst
# ---------------------------------------------------------------------------

woorden = zin.split()
print(woorden)          # ['Python', 'is', 'een', 'programmeertaal']
print(len(woorden))     # 4

# Splitsen op iets anders dan een spatie:
regel = "appel;1.20;3"
velden = regel.split(";")
print(velden)           # ['appel', '1.20', '3']
print(velden[0])        # appel
print(float(velden[1])) # 1.2: vergeet het omzetten niet


# ---------------------------------------------------------------------------
# 4. join(): van een lijst terug naar één string
# ---------------------------------------------------------------------------

print(" ".join(woorden))        # Python is een programmeertaal
print(", ".join(woorden))       # Python, is, een, programmeertaal


# ---------------------------------------------------------------------------
# 5. strip(): spaties vooraan en achteraan weghalen
# ---------------------------------------------------------------------------

invoer = "  Rob  "
print(f"[{invoer}]")            # [  Rob  ]
print(f"[{invoer.strip()}]")    # [Rob]

# Waarom dit telt: gebruikers typen spaties. Zonder strip() is
# "rob" niet gelijk aan "rob ", en zoek jij een uur naar de fout.
print("rob" == "rob ")          # False
print("rob" == "rob ".strip())  # True


# ---------------------------------------------------------------------------
# 6. Handige bewerkingen
# ---------------------------------------------------------------------------

print(zin.upper())              # PYTHON IS EEN PROGRAMMEERTAAL
print(zin.lower())              # python is een programmeertaal
print(zin.replace("Python", "Java"))
print("Python" in zin)          # True
print("java" in zin)            # False: let op de hoofdletters
print("java" in zin.lower())    # False, want de zin bevat "python", niet "java"


# ---------------------------------------------------------------------------
# 7. Vergelijken doe je meestal na lower() én strip()
# ---------------------------------------------------------------------------

antwoord = "  JA  "
print(antwoord == "ja")                     # False
print(antwoord.strip().lower() == "ja")     # True

# Dit is het patroon voor elke gebruikersinvoer die je vergelijkt.
