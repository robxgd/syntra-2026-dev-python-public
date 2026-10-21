# Oefening 3: Repareer de fout

> ± 25 minuten · individueel · vier bestanden in deze map

Vier programma's. Alle vier zijn ze **syntactisch correct**: Python heeft geen enkel bezwaar
tegen wat er staat. Toch doen ze niet wat ze zouden moeten doen.

## Werkwijze per bestand

1. **Lees** het programma. Schrijf als commentaarregel op wat je denkt dat er misgaat.
   **Doe dit vóór je uitvoert.**
2. **Voer uit** met de testwaarden die bovenaan het bestand staan.
3. **Noteer als commentaar** wat er echt misging, en of je hypothese klopte.
4. **Repareer** het.
5. **Voer opnieuw uit** om te controleren.

Stap 1 is de belangrijkste. Wie meteen begint te veranderen tot het toevallig werkt, leert niets.

---

| Bestand | Testwaarden | Zou moeten geven |
|---|---|---|
| `fout_1_gemiddelde.py` | 10, 20, 30 | 20.0 |
| `fout_2_korting.py` | bedrag 100, korting 10 | 90.0 |
| `fout_3_toegang.py` | leeftijd 12 | `Te jong` |
| `fout_4_tarief.py` | leeftijd 10 | 6 euro |

## Eén ervan is anders

Drie van deze vier programma's **draaien gewoon door** en geven een verkeerd antwoord.
Eén crasht met een foutmelding.

Welke crasht? En waarom is dat eigenlijk het minst erge geval van de vier?

## Klaar en tijd over?

Neem `fout_4_tarief.py` en test het met leeftijd `11`, `12`, `64`, `65` en `-3`.
Ook ná je reparatie. Kloppen alle vijf?
