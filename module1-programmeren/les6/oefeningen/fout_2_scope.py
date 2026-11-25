"""FOUT 2: dit programma crasht.

Bedoeling: het totaal berekenen en daarna tonen.
De variabele `totaal` bestaat toch? Lees de foutmelding.
"""


def tel_op(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal


tel_op([10, 20, 30])

print(f"Totaal: {totaal}")
