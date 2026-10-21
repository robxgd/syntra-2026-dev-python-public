"""DEMO 3: fouten opvangen met try/except.

Blok per blok tonen en uitvoeren.
"""

# ---------------------------------------------------------------------------
# 1. Zonder opvangen: één verkeerde invoer en het programma is weg
# ---------------------------------------------------------------------------

# leeftijd = int(input("Leeftijd: "))       # typ "abc" → ValueError, klaar
# print(f"Volgend jaar: {leeftijd + 1}")


# ---------------------------------------------------------------------------
# 2. Met try/except: het programma blijft leven
# ---------------------------------------------------------------------------

tekst = "abc"

try:
    leeftijd = int(tekst)
    print(f"Volgend jaar: {leeftijd + 1}")
except ValueError:
    print("Dat is geen geldig getal.")

# Lees het als: "probeer dit; gaat het mis met een ValueError, doe dan dat."


# ---------------------------------------------------------------------------
# 3. Wees SPECIFIEK over wat je opvangt
# ---------------------------------------------------------------------------

def deel(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(deel(10, 2))          # 5.0
print(deel(10, 0))          # None: netjes opgevangen


# ---------------------------------------------------------------------------
# 4. De kale except:: waarom dat een slecht idee is
#
#    Hieronder zit een TIKFOUT: getalen in plaats van getallen.
#    Dat is een NameError, een echte bug in jouw code.
#    De kale except vangt hem op en verstopt hem.
# ---------------------------------------------------------------------------

getallen = [10, 20, 30]

try:
    gemiddelde = sum(getalen) / len(getallen)       # tikfout!
except:
    gemiddelde = 0

print(f"Gemiddelde: {gemiddelde}")      # 0, en niemand weet waarom

# Het programma meldt niets. Het antwoord is gewoon fout.
# Zo raak je een bug kwijt die je nooit meer terugvindt.


# ---------------------------------------------------------------------------
# 5. Hetzelfde, maar specifiek: nu zie je de echte fout
#
#    Haal het commentaar weg en toon de NameError.
# ---------------------------------------------------------------------------

# try:
#     gemiddelde = sum(getalen) / len(getallen)
# except ZeroDivisionError:
#     gemiddelde = 0
# print(gemiddelde)

# Regel: vang alleen op wat je VERWACHT en waar je iets zinnigs mee doet.
# Al de rest mag crashen: dat is hoe je bugs vindt.


# ---------------------------------------------------------------------------
# 6. Meerdere soorten fouten apart opvangen
# ---------------------------------------------------------------------------

def veilig_delen(tekst_a, tekst_b):
    try:
        a = float(tekst_a)
        b = float(tekst_b)
        return a / b
    except ValueError:
        return "Geef twee getallen in."
    except ZeroDivisionError:
        return "Delen door nul kan niet."

print(veilig_delen("10", "2"))      # 5.0
print(veilig_delen("tien", "2"))    # Geef twee getallen in.
print(veilig_delen("10", "0"))      # Delen door nul kan niet.
