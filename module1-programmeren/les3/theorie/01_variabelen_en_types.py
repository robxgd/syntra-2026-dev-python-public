"""DEMO 1: variabelen en types. Hiermee start je de les.

Doorloop dit van boven naar beneden, blok per blok. Voer na elk blok uit.
Verwijder de blokken die je nog niet wil tonen niet, laat ze staan en scroll.
"""

# ---------------------------------------------------------------------------
# 1. Een variabele is een naam die naar een waarde verwijst
# ---------------------------------------------------------------------------

prijs = 12.50
print(prijs)

# De naam mag je opnieuw gebruiken. De oude waarde is dan weg.
prijs = 15.00
print(prijs)

# Rechts wordt eerst berekend, dan pas toegekend.
prijs = prijs + 5
print(prijs)            # 20.0


# ---------------------------------------------------------------------------
# 2. Vier types die je deze module nodig hebt
# ---------------------------------------------------------------------------

aantal = 3              # int: geheel getal
prijs = 12.50           # float: kommagetal
naam = "Rob"            # str: tekst
betaald = True          # bool: waar of niet waar

print(type(aantal))     # <class 'int'>
print(type(prijs))      # <class 'float'>
print(type(naam))       # <class 'str'>
print(type(betaald))    # <class 'bool'>


# ---------------------------------------------------------------------------
# 3. Hetzelfde teken doet iets anders per type
# ---------------------------------------------------------------------------

print(3 + 4)            # 7: optellen
print("3" + "4")        # 34: aan elkaar plakken
print("ha" * 3)         # hahaha: herhalen

# En sommige combinaties kunnen gewoon niet:
# print("3" + 4)        # TypeError: commentaarteken weghalen en tonen


# ---------------------------------------------------------------------------
# 4. Omzetten tussen types
# ---------------------------------------------------------------------------

tekst = "42"
getal = int(tekst)
print(getal + 1)        # 43

print(float("12.50"))   # 12.5
print(str(42) + " euro")

# Lukt de omzetting niet, dan crasht het meteen:
# print(int("42a"))     # ValueError: tonen
# print(int("12,50"))   # ValueError: de komma. Belangrijkste van de avond.


# ---------------------------------------------------------------------------
# 5. input() geeft ALTIJD tekst terug. Nooit een getal.
#
#    Dit is de belangrijkste regel van deze les. Vier gevallen: alleen het
#    eerste crasht, de andere drie geven stilletjes het verkeerde antwoord.
# ---------------------------------------------------------------------------

leeftijd = "30"         # dit is wat input() teruggeeft bij invoer 30

# print(leeftijd + 1)   # TypeError: can only concatenate str (not "int") to str

aantal = "3"
print(aantal * 3)       # 333: niet 9

antwoord = "10"
print(antwoord == 10)   # False: tekst is niet gelijk aan een getal

a = "5"
b = "7"
print(a + b)            # 57: niet 12


# De oplossing: zet meteen om bij het inlezen.
#
#   leeftijd = int(input("Hoeveel jaar ben je? "))
#   prijs    = float(input("Prijs: "))
#
# Vanaf hier gebruikt elke oefening invoer. Zonder deze omzetting loopt alles vast.
