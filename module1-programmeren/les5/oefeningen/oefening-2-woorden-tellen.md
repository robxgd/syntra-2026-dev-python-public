# Oefening 2: Woorden tellen

> ± 25 minuten · individueel · maak een bestand `tellen.py`

Je bouwt het patroon dat je in deze module het vaakst nodig hebt: **voorkomens tellen met
een dictionary**.

Begin met:

```python
zin = "de kat zat op de mat en de kat sliep"
```

---

## A: Splitsen

Maak een lijst van de woorden en toon hoeveel woorden er zijn.

> Verwacht: `10`

## B: Tellen

Bouw een dictionary waarin elk woord een sleutel is en het aantal keer dat het voorkomt
de waarde. Toon de dictionary.

> Verwacht: `{'de': 3, 'kat': 2, 'zat': 1, 'op': 1, 'mat': 1, 'en': 1, 'sliep': 1}`

Probeer het eerst zelf met het accumulator-patroon uit de demo, vóór je verderleest.

!!! tip "Vastgelopen? Het patroon"

    ```python
    tellingen = {}
    for woord in woorden:
        tellingen[woord] = tellingen.get(woord, 0) + 1
    ```

    Lees die middelste regel hardop: *pak de huidige stand voor dit woord (of 0 als het er nog
    niet was) tel er één bij, en zet het terug.*

> Probeer eens wat er gebeurt als je `.get(woord, 0)` vervangt door `tellingen[woord]`.
> Welke fout krijg je, en waarom?

## C: Hoeveel verschillende woorden?

Toon hoeveel **unieke** woorden er zijn.

> Verwacht: `7`

## D: Alleen de herhalingen

Toon per woord dat **meer dan één keer** voorkomt een regel:

```
de komt 3 keer voor
kat komt 2 keer voor
```

## E: Het meest voorkomende woord

Zoek het woord dat het vaakst voorkomt en toon het met zijn aantal.

> Verwacht: `de` met `3`

Gebruik hetzelfde accumulator-patroon als in les 4, maar onthoud nu **twee** dingen:
de beste sleutel én de beste waarde.

---

## Nu breken

Vervang de zin door deze en voer opnieuw uit:

```python
zin = "De kat zat op de mat. De KAT sliep."
```

Kijk naar je telling voor `de`.

| Vraag | Jouw antwoord |
|---|---|
| Hoe vaak telt jouw programma `de`? | |
| Hoe vaak zou het moeten zijn? | |
| Wat veroorzaakt het verschil? | |

Er zijn twee oorzaken. Vind je ze allebei?

## Klaar en tijd over?

- Los de twee oorzaken op. Tip: `.lower()` en `.replace(".", "")`.
- Tel niet de woorden maar de **letters** van de zin.
