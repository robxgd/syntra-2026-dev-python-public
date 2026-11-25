# Oefening 1: Vier keer hetzelfde patroon

> ± 30 minuten · individueel · maak een bestand `analyse.py`

Vier opdrachten op dezelfde lijst. Ze zien er verschillend uit, maar volgen alle vier
hetzelfde patroon:

1. maak een variabele klaar **vóór** de lus
2. pas hem aan **binnen** de lus
3. gebruik hem **na** de lus

Begin je bestand met deze regel:

```python
temperaturen = [12, 18, 7, 21, 15, 9, 24]
```

Voer uit na elke opdracht.

---

## A: Tel ze op

Bereken het totaal van alle temperaturen en toon het.

> Verwacht: `106`

## B: Bereken het gemiddelde

Deel het totaal door het aantal. Gebruik `len()`, **niet** het getal 7. Waarom niet?
Voeg een achtste temperatuur toe aan de lijst en voer opnieuw uit; dan weet je het.

> Verwacht met zeven waarden: `15.142857142857142`
> Toon het netter met `{gemiddelde:.1f}`

## C: Zoek de hoogste

Zoek de hoogste temperatuur.

> Verwacht: `24`

⚠️ Begin **niet** met `hoogste = 0`. Begin met `hoogste = temperaturen[0]`.
Test daarna je programma met deze lijst:

```python
temperaturen = [-3, -7, -1, -9]
```

> Verwacht: `-1`. Krijg je `0`, dan zit de fout in je startwaarde.

## D: Tel de warme dagen

Tel hoeveel temperaturen 15 of hoger zijn.

> Verwacht: `4`

---

## Klaar en tijd over?

- **E**: bouw een nieuwe lijst met alleen de warme dagen erin. Gebruik `.append()`.
- **F**: zoek ook de laagste temperatuur.
- **G**: toon per temperatuur een regel: `12 graden (koel` of `21 graden) warm`.
