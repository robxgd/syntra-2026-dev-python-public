"""DEMO 5: waarom sommige dingen anders geschreven worden.

Geen klassen schrijven vanavond. Het doel: de twee schrijfwijzen herkennen,
niet meer verward raken.
"""

# ---------------------------------------------------------------------------
# 1. Twee schrijfwijzen die ze al de hele module gebruiken
# ---------------------------------------------------------------------------

tekst = "python"
lijst = [3, 1, 2]

print(len(tekst))           # functie:  len(iets)
print(tekst.upper())        # methode:  iets.upper()

print(len(lijst))           # functie
lijst.append(4)             # methode
print(lijst)


# ---------------------------------------------------------------------------
# 2. Het verschil
#
#    len(x): een losse functie. Werkt op van alles: tekst, lijst, dict.
#    x.upper(): een methode. Hoort BIJ het type en werkt alleen daarop.
# ---------------------------------------------------------------------------

print("abc".upper())        # werkt: strings hebben upper()
# print([1, 2].upper())     # AttributeError: 'list' object has no attribute 'upper'

# Haal dat commentaarteken weg en toon de foutmelding. Ze gaan hem tegenkomen.


# ---------------------------------------------------------------------------
# 3. Elk type heeft zijn eigen set methodes
# ---------------------------------------------------------------------------

# strings:      .upper() .lower() .strip() .split() .replace() .startswith()
# lijsten:      .append() .remove() .sort() .count() .index()
# dictionaries: .get() .items() .keys() .values()

getallen = [5, 3, 9, 1]
getallen.sort()
print(getallen)             # [1, 3, 5, 9]

woorden = ["peer", "appel", "kiwi"]
woorden.sort()
print(woorden)              # ['appel', 'kiwi', 'peer']: alfabetisch


# ---------------------------------------------------------------------------
# 4. Hoe kom je erachter welke methodes iets heeft?
# ---------------------------------------------------------------------------

# In VS Code: typ de variabele, dan een punt, en wacht op de lijst.
# Of vraag het aan Python zelf:

print(type(woorden))        # <class 'list'>

# En dan zoek je "python list methods" op in de documentatie.


# ---------------------------------------------------------------------------
# Wat ze hieruit moeten meenemen:
#
#   "Data met bijhorend gedrag." Een string weet zelf hoe hij hoofdletters
#   maakt. Een lijst weet zelf hoe hij sorteert.
#
#   Klassen (je eigen types maken) komt in een latere module.
# ---------------------------------------------------------------------------
