# Oefening 2: Beslisboom voor verzendkosten

> ± 35 minuten · individueel · maak een bestand `verzending.py`

Nu schrijf je zelf een programma mét beslissingen. En je doet het in de volgorde van de
module: **eerst de stappen als commentaar, dan pas code.**

---

## De opdracht

> Een webshop rekent verzendkosten:
> - onder 25 euro: 5,95 euro verzending
> - vanaf 25 euro: 2,95 euro verzending
> - vanaf 50 euro: gratis verzending
>
> Toon het bestelbedrag, de verzendkosten en het totaal.

## Stap 1: Analyse (als commentaar)

Zet dit eerst als commentaarregels bovenaan `verzending.py`, vóór je één regel code schrijft:

- Wat gaat erin?
- Wat komt eruit?
- Wat kan er misgaan?

## Stap 2: Stappen opschrijven

Maak `verzending.py` en zet er **alleen commentaarregels** in. Iets in deze vorm:

```python
# 1. vraag het bestelbedrag
# 2. zet de invoer om naar een kommagetal
# 3. bepaal de verzendkosten
# 4. bereken het totaal
# 5. toon bedrag, verzendkosten en totaal
```

▶ Uitvoeren. Er gebeurt niets. Dat klopt, het zijn alleen opmerkingen.

## Stap 3: Code ertussen

Vul nu onder elke commentaarregel de code in. Voer uit na elke stap die je toevoegt.

Voor stap 3 heb je `if` / `elif` / `else` nodig. Let op de **volgorde**: Python stopt bij de
eerste voorwaarde die klopt.

## Stap 4: Testen op de grenzen

De grenzen zijn waar het bijna altijd misgaat. Test deze acht bedragen en vergelijk met de
verwachte verzendkosten:

| Bedrag | Verwachte verzending |
|---|---|
| `10` | 5.95 |
| `24.99` | 5.95 |
| `25` | 2.95 |
| `25.01` | 2.95 |
| `49.99` | 2.95 |
| `50` | 0 |
| `50.01` | 0 |
| `0` | 5.95 |

> Klopt `25` en `50` niet? Dan staat er ergens `>` waar `>=` hoort. Dat heet een
> off-by-one-fout en je gaat hem nog vaak tegenkomen.

## Stap 5: Rare invoer

Test ook `-10`, `abc` en leeg. Noteer als commentaar wat er gebeurt. Je hoeft het **nog niet
op te lossen**, netjes opvangen leren we in les 7. Nu volstaat het dat je wéét dat het gebeurt.

## Klaar en tijd over?

- Voeg toe: bestellingen boven 500 euro krijgen ook gratis verzending én een melding
  "grote bestelling".
- Toon een regel "Je bent nog X euro verwijderd van gratis verzending" wanneer dat van
  toepassing is.
