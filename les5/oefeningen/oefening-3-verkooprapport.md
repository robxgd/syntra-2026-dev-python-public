# Oefening 3: Verkooprapport

> ± 40 minuten · individueel · start van `verkopen.py`

De hoofdopdracht van de avond, en de eerste die groot genoeg is om te ontsporen.
Daarom bakenen we hem eerst af.

---

## De opdracht

> Je krijgt een lijst met verkoopregels in de vorm `product;prijs;aantal`.
> Maak een rapport dat toont: de totale omzet, per product het aantal verkochte stuks
> en de omzet, en welk product het meeste heeft opgebracht.

## Stap 1: Splits de opdracht op (3 tot 6 taken)

Maak `verkopen.py` en zet bovenaan, als commentaarregels: wat de aparte stukken zijn.
Niet in code, in gewone taal, één regel per taak.

## Stap 2: Must, should, could

Je hebt veertig minuten. Markeer bij elke taak, ook als commentaar, of hij **must**
(zonder dit is het rapport waardeloos), **should** (hoort erbij, maar kan later) of
**could** (leuk als er tijd over is) is.

> Wie alles tegelijk wil, heeft op het einde niets werkend. Kies je must-lijst en begin daar.

## Stap 3: Definition of Done

Wanneer is deze opdracht af? Zet als commentaar vier tot zes punten die je op het einde afvinkt.

> "Het draait" is geen punt. "De totale omzet klopt met de hand nagerekend" wel.

## Stap 4: Bouwen

Je hebt nodig:

- een `for`-lus over `verkopen`
- `.split(";")` om elke regel uit elkaar te halen
- `float()` en `int()` om de velden om te zetten
- **twee** dictionaries: één voor het aantal stuks per product, één voor de omzet per product
- het telpatroon van oefening 2: `dict[sleutel] = dict.get(sleutel, 0) + waarde`

## Stap 5: Controleren

Reken met de hand na en vergelijk:

| Product | Stuks | Omzet |
|---|---|---|
| appel | 8 | 9.60 |
| brood | 1 | 2.50 |
| melk | 6 | 6.60 |
| kaas | 1 | 4.80 |
| **Totaal** | | **23.50** |

Hoogste omzet: `appel`.

> Toon bedragen met `{bedrag:.2f}`. Zonder dat krijg je regels als `6.6000000000000005`.

## Stap 6: Loop je Definition of Done af

Vink je punten uit stap 3 af. Wat niet klaar is, is niet klaar. Dat is geen schande, dat is
je scope die klopte of niet.

---

## Klaar en tijd over? (dit waren je "could"-taken)

- Toon het product met de **meeste stuks** (niet de hoogste omzet). Is dat hetzelfde product?
- Voeg een regel toe voor een product met aantal `0` en kijk wat er gebeurt.
- Sorteer het rapport van hoogste naar laagste omzet.
- Voeg een verkoopregel toe met een fout formaat, bv. `"kaas;4.80"` (aantal ontbreekt).
  Wat gebeurt er? Nog niet oplossen. Dat is les 7.
