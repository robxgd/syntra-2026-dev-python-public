"""Voor oefening 2: de debugger.

Dit programma berekent de eindscore van elke deelnemer:
de som van zijn drie rondes, plus een bonus van 5 als hij in alle
drie de rondes 10 of meer scoorde.

Met de hand nagerekend hoort er dit uit te komen:

    Ali:  12 + 15 + 15 = 42, alle rondes >= 10  → bonus  → 47
    Bo:    9 +  8 + 10 = 27, ronde 1 is 9       → geen   → 27
    Cem:  14 + 16 + 15 = 45, alle rondes >= 10  → bonus  → 50

Voer het uit. Ali klopt. De rest niet.

Zoek de fout MET DE DEBUGGER, zet een breakpoint en kijk per ronde
naar de waarde van `totaal`. Geen print() in deze oefening.
"""

deelnemers = {
    "Ali": [12, 15, 15],
    "Bo": [9, 8, 10],
    "Cem": [14, 16, 15],
}

totaal = 0
alles_minstens_tien = True

for naam, rondes in deelnemers.items():

    for punt in rondes:
        totaal = totaal + punt
        if punt < 10:
            alles_minstens_tien = False

    if alles_minstens_tien:
        totaal = totaal + 5

    print(f"{naam}: {totaal}")
