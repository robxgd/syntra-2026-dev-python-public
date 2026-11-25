"""DEMO 1: functies. Hiermee start je de les.

Blok per blok tonen en uitvoeren.
"""

# ---------------------------------------------------------------------------
# 1. Een functie is een stuk code met een naam
# ---------------------------------------------------------------------------

def groet():
    print("Hallo!")

groet()             # oproepen: nu pas gebeurt er iets
groet()             # en nog eens, zonder de code te herhalen


# ---------------------------------------------------------------------------
# 2. Met een parameter: dezelfde code, andere invoer
# ---------------------------------------------------------------------------

def groet_persoon(naam):
    print(f"Hallo {naam}!")

groet_persoon("Rob")
groet_persoon("Sofie")


# ---------------------------------------------------------------------------
# 3. print() versus return: DE verwarring van deze les
# ---------------------------------------------------------------------------

def btw_tonen(bedrag):
    print(bedrag * 0.21)        # toont het, geeft niets terug

def btw_berekenen(bedrag):
    return bedrag * 0.21        # geeft het terug, toont niets


btw_tonen(100)                  # 21.0 verschijnt op het scherm
btw_berekenen(100)              # er verschijnt NIETS

# Het verschil zie je pas als je ermee verder wil:
resultaat = btw_berekenen(100)
print(resultaat + 5)            # 26.0: je kan ermee rekenen

fout = btw_tonen(100)
print(fout)                     # None: er kwam niets terug

# Vuistregel: een functie die iets BEREKENT gebruikt return.
# print() zet je in de functie die de gebruiker iets TOONT.


# ---------------------------------------------------------------------------
# 4. Meerdere parameters
# ---------------------------------------------------------------------------

def totaalprijs(prijs, aantal, btw_procent):
    subtotaal = prijs * aantal
    btw = subtotaal * btw_procent / 100
    return subtotaal + btw

print(totaalprijs(10, 3, 21))       # 36.3
print(totaalprijs(2.50, 4, 6))      # 10.6

# Met de namen erbij (keyword-argumenten) maakt de volgorde niet meer uit:
print(totaalprijs(aantal=3, prijs=10, btw_procent=21))   # ook 36.3


# ---------------------------------------------------------------------------
# 5. Scope: wat binnen de functie leeft, blijft binnen
#
#    Haal het commentaarteken weg en laat het crashen.
# ---------------------------------------------------------------------------

def bereken():
    binnenin = 42
    return binnenin

print(bereken())        # 42
# print(binnenin)       # NameError: name 'binnenin' is not defined

# Dat is geen beperking maar een voordeel: je kan een variabele in een
# functie hernoemen zonder je zorgen te maken over de rest van je programma.


# ---------------------------------------------------------------------------
# 6. Een functie die een lijst verwerkt: les 4 en 5 in functievorm
# ---------------------------------------------------------------------------

def gemiddelde(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    return totaal / len(getallen)

print(gemiddelde([12, 15, 18]))     # 15.0
print(gemiddelde([1, 2, 3, 4]))     # 2.5

# Eén keer geschreven, overal bruikbaar. Dat is het punt van functies.
