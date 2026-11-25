"""DEMO 1: lijsten.

Tot nu had elke variabele één waarde. Een lijst houdt er meerdere vast.
"""

# ---------------------------------------------------------------------------
# 1. Een lijst maken en bekijken
# ---------------------------------------------------------------------------

scores = [12, 15, 9, 18, 14]

print(scores)           # [12, 15, 9, 18, 14]
print(len(scores))      # 5: hoeveel er in zitten


# ---------------------------------------------------------------------------
# 2. Eén element eruit halen: tellen begint bij NUL
# ---------------------------------------------------------------------------

print(scores[0])        # 12: de eerste
print(scores[1])        # 15: de tweede
print(scores[4])        # 14: de vijfde en laatste

print(scores[-1])       # 14, ook de laatste, van achter geteld
print(scores[-2])       # 18


# ---------------------------------------------------------------------------
# 3. De klassieke fout: len is 5, maar de laatste index is 4
#
#    Haal het commentaarteken weg en laat het crashen.
#    Dit heet een off-by-one. Je gaat hem nog vaak tegenkomen.
# ---------------------------------------------------------------------------

# print(scores[5])      # IndexError: list index out of range


# ---------------------------------------------------------------------------
# 4. Elementen toevoegen en verwijderen
# ---------------------------------------------------------------------------

scores.append(20)       # achteraan bijzetten
print(scores)           # [12, 15, 9, 18, 14, 20]

scores.remove(9)        # verwijder de WAARDE 9 (niet de positie 9)
print(scores)           # [12, 15, 18, 14, 20]

print(len(scores))      # 5


# ---------------------------------------------------------------------------
# 5. Een lege lijst is een geldige lijst
# ---------------------------------------------------------------------------

nog_geen_scores = []
print(nog_geen_scores)  # []
print(len(nog_geen_scores))  # 0

# Onthou dit. In les 2 vonden jullie "wat als er nul zijn?" als randgeval.
# Zo ziet dat eruit. Straks zie je wat er dan misgaat.
