# Oefening 2: Boodschappenlijst

> ± 35 minuten · individueel · maak een bestand `boodschappen.py`

De opdracht van de avond. Je schrijft hem volgens de werkwijze van de module:
**eerst de stappen als commentaar, dan pas code.**

---

## De opdracht

> Vraag hoeveel producten er zijn. Vraag daarna per product de prijs.
> Toon op het einde: het aantal producten, het totaalbedrag, de duurste prijs,
> en het gemiddelde per product.

## Stap 1: Analyse

Maak `boodschappen.py` en zet bovenaan, als commentaarregels, vóór je iets typt:

- Wat gaat erin?
- Wat komt eruit?
- Wat kan er misgaan? Loop de zes vragen af: nul · negatief · geen getal · komma ·
  te groot · leeg.

## Stap 2: Stappen opschrijven

Zet **alleen commentaarregels** in je bestand. Iets in deze vorm:

```python
# 1. vraag hoeveel producten er zijn
# 2. lees de prijzen één voor één in en bewaar ze in een lijst
# 3. tel de prijzen op
# 4. zoek de duurste prijs
# 5. bereken het gemiddelde
# 6. toon aantal, totaal, duurste en gemiddelde
```

▶ Uitvoeren. Er gebeurt niets. Dat klopt.

## Stap 3: Code ertussen

Vul stap voor stap in. Voer uit na elke stap die je toevoegt.

Je hebt nodig:
- een `while`-lus om de prijzen in te lezen (hetzelfde patroon als het klasgemiddelde uit de les)
- een lege lijst en `.append()`
- een `for`-lus per berekening, of één `for`-lus die alles tegelijk doet

## Stap 4: Testen

| Invoer | Verwacht |
|---|---|
| 3 producten: `10`, `20`, `30` | totaal 60.00 · duurste 30.00 · gemiddelde 20.00 |
| 1 product: `5.50` | totaal 5.50 · duurste 5.50 · gemiddelde 5.50 |
| 2 producten: `12.99`, `12.99` | totaal 25.98 · duurste 12.99 · gemiddelde 12.99 |

Toon bedragen met `{bedrag:.2f}`, anders krijg je regels als `25.979999999999997`.

## Stap 5: Breken

Test deze vijf gevallen en noteer als commentaar wat er gebeurt. **Nog niet oplossen**.
Dat is les 7.

- 0 producten
- prijs `12,99`
- prijs `abc`
- prijs `-5`
- aantal `-2`

> Eén van deze vijf crasht niet. Welke, en wat toont je programma dan?

## Klaar en tijd over?

- Toon ook de goedkoopste prijs.
- Toon hoeveel producten duurder zijn dan het gemiddelde.
- Vraag per product ook een naam, en toon welk product het duurste is.
