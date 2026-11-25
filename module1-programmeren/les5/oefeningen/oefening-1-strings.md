# Oefening 1: Werken met tekst

> ± 25 minuten · individueel · maak een bestand `tekst.py`

Begin je bestand met deze regel:

```python
zin = "  De snelle bruine vos springt over de luie hond  "
```

Let op de spaties vooraan en achteraan. Die zitten er expres in.

Voer uit na elke opdracht.

---

## A: Opkuisen

Haal de spaties vooraan en achteraan weg en toon de zin.

> Verwacht: `De snelle bruine vos springt over de luie hond`

## B: Tellen

Toon hoeveel **tekens** de opgekuiste zin telt, en hoeveel **woorden**.

> Verwacht: `46` tekens, `9` woorden

## C: Eerste en laatste woord

Toon het eerste en het laatste woord van de zin.

> Verwacht: `De` en `hond`

## D: Alles in hoofdletters

Toon de zin in hoofdletters, en daarna in kleine letters.

## E: Zoeken

Controleer of het woord `vos` in de zin zit, en of `kat` erin zit. Toon `True` of `False`.

> Verwacht: `True` en `False`

## F: Elk woord op een eigen regel

Toon elk woord op een aparte regel, met een nummer ervoor:

```
1. De
2. snelle
3. bruine
...
```

> Tip: `enumerate(woorden, start=1)` uit les 4.

---

## De valkuil

Test dit eens:

```python
antwoord = "  JA  "
print(antwoord == "ja")
```

Waarom is dat `False`? En wat moet je toevoegen om het `True` te maken?

Dit is geen strikvraag. Elke keer dat je straks gebruikersinvoer vergelijkt, loop je hiertegen aan.

## Klaar en tijd over?

- Toon alleen de woorden die langer zijn dan vier letters.
- Toon de zin achterstevoren op woordniveau (`hond luie de over ...`).
  Tip: `.split()`, dan `[::-1]`, dan `" ".join(...)`.
