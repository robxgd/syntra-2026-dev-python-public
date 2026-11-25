# Oefening 2: Ruim dit script op

> ± 40 minuten · individueel · werk in `rommelig_klasrapport.py`

Dit script werkt. Het is alleen drie keer bijna hetzelfde.

---

## Stap 0: Leg je vangnet

Voer het script uit en **bewaar de output**. Kopieer ze naar een tekstbestand, of maak een
schermafbeelding.

Na elke wijziging voer je opnieuw uit en vergelijk je met dit origineel. Wijkt er iets af,
dan weet je meteen dat je laatste wijziging fout was.

> Dit is de belangrijkste stap. Zonder vangnet ben je aan het gokken.

## Stap 1: Zoek de herhaling

Kijk naar de drie blokken. Wat is per blok exact hetzelfde, en wat verschilt?

| | Antwoord |
|---|---|
| Wat verschilt per blok? | |
| Welke berekeningen komen drie keer voor? | |

## Stap 2: Eén functie tegelijk

Begin met de makkelijkste: het optellen.

1. Schrijf `def totaal_van(punten):` met een `return`.
2. Vervang **alleen het eerste blok** door een oproep van je functie.
3. ▶ Uitvoeren en vergelijken met je vangnet.
4. Pas als het klopt: doe hetzelfde voor blok twee en drie.

Herhaal dit voor:

- `totaal_van(punten)`
- `gemiddelde_van(punten)`
- `aantal_geslaagd(punten)`

> Doe **niet** alles tegelijk. Eén functie, uitvoeren, vergelijken. Dan de volgende.

## Stap 3: Het printblok

De drie printblokken zijn ook identiek op de naam na. Maak er één functie van:

```python
def toon_vak(naam, punten):
    ...
```

Daarna moet je hoofdprogramma nog ongeveer dit zijn:

```python
toon_vak("Wiskunde", wiskunde)
toon_vak("Frans", frans)
toon_vak("Labo", labo)
```

## Stap 4: Controle

| Controle | ✓ |
|---|---|
| De output is exact identiek aan mijn vangnet | |
| Er staat nergens nog dezelfde berekening twee keer | |
| Elke functie heeft een naam die zegt wat ze doet | |
| Elke functie gebruikt `return` (behalve `toon_vak`, die toont) | |

## Stap 5: De echte test

De directeur wil er een vierde vak bij: `nederlands = [13, 16, 11, 14]`.

Hoeveel regels moet je nu toevoegen? Tel ze. Vergelijk met hoeveel het er waren geweest
in het originele script.

> Dít is waarom je opsplitst. Niet omdat het korter wordt. Dat wordt het vaak niet eens.

## Klaar en tijd over?

- Voeg een functie `hoogste_van(punten)` toe en toon het hoogste punt per vak.
- Voeg onderaan een regel toe met het gemiddelde over álle vakken samen.
- Zet je functies in een apart bestand `rapportfuncties.py` en importeer ze.
