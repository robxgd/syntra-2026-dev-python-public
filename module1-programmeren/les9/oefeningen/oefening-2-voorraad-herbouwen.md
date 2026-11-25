# Oefening 2: Het voorraadoverzicht herbouwen

> ± 40 minuten · individueel · startbestand `rommelig_voorraad.py`

Dit is de hoofdopdracht van de avond. Het startbestand werkt: het toont de voorraad van drie
artikelen, waarschuwt wanneer er bijna niets meer ligt, en telt de totale waarde. Het probleem
is de vorm: `(naam, aantal, prijs)` wordt overal als losse tuple doorgegeven en dezelfde
berekening staat op twee plaatsen.

Jij gaat het herbouwen met een klasse. **De output moet er nadien letterlijk hetzelfde
uitzien.**

---

## Stap 0: Bewaar je vangnet

Voer `rommelig_voorraad.py` uit en kopieer wat er op het scherm komt naar een kladbestand of
een commentaarblok. Zonder dat vangnet kan je niet zien of je herbouw gelukt is.

Zo hoort het eruit te zien:

```
VOORRAAD BUURTWINKEL
=============================================
Melk          24 stuks      27.60 euro
Brood          3 stuks       7.20 euro
              bijna leeg, bestellen
Kaas          12 stuks      57.00 euro
=============================================
Totale voorraadwaarde: 91.80 euro
```

---

## Stap 1: Welke data hoort bij elkaar?

Vul in: welke drie dingen beschrijven samen één artikel?

| | |
|---|---|
| 1 | |
| 2 | |
| 3 | |

Als je die drie in één object stopt, welke methodes horen er dan bij? Kijk naar de drie
functies in het startbestand. Elke functie wordt een methode, behalve één.

> Welke functie heeft géén artikel nodig? Die blijft een gewone functie of verdwijnt in de
> methode van een ander. Denk aan `voorraadwaarde` en `toon_artikel`.

## Stap 2: Schrijf de klasse

Schrijf in een nieuw bestand `voorraad.py` de klasse `Artikel` met:

- `__init__` met `naam`, `aantal`, `prijs`
- `voorraadwaarde()` die `aantal * prijs` teruggeeft
- `is_bijna_leeg()` met een standaardgrens van 5
- `toon()` die exact dezelfde regel toont als het startbestand

Maak eerst één artikel en test het. Pas daarna verder.

## Stap 3: De lijst met objecten

Vervang de lijst met tuples door een lijst met `Artikel`-objecten. De drie artikelen zijn
dezelfde, met dezelfde aantallen en prijzen.

De lus wordt dan:

```python
for artikel in artikelen:
    artikel.toon()
```

Vergelijk met je vangnet. De regels moeten identiek zijn, inclusief de uitlijning en de
waarschuwing bij Brood.

## Stap 4: De totale waarde

Onderaan je bestand, dezelfde regel als in het startbestand:

```
Totale voorraadwaarde: 91.80 euro
```

> Let op: `91.80` komt uit een `sum` over `voorraadwaarde()`. Reken niet met een handmatig
> ingetypt getal, dan test je niets.

## Stap 5: Eén regel erbij

De winkelier wil er een artikel bij: `("Yoghurt", 8, 0.95)`. Hoeveel regels moet je aanpassen?

Vergelijk met het startbestand: daar pas je de lijst aan, en verder niets. Dat is hetzelfde
antwoord als in les 6. Tel het echt, en schrijf het op.

---

## Controle

| | ✓ |
|---|---|
| De output is letterlijk gelijk aan je vangnet | |
| `voorraadwaarde()` gebruikt `return`, niet `print()` | |
| `is_bijna_leeg()` heeft een standaardwaarde voor de grens | |
| Er staat nergens een losse tuple meer in je code | |
| De uitlijning van de bedragen is nog steeds goed | |

> Die laatste is niet vanzelfsprekend. Bij het herbouwen vergeten de meeste mensen de breedte
> van `f"{naam:12}"`, en dan schuift alles op. Je vangnet toont het meteen.

---

## Klaar en tijd over?

- **Stap 6**: voeg een methode `verkoop(aantal)` toe. Wat gebeurt er als je 10 verkoopt van een
  artikel waar er 3 liggen? Kies een aanpak en noteer waarom.
- **Stap 7**: zet de artikelen in een dictionary in plaats van een lijst, met de naam als
  sleutel. Wat wordt makkelijker, en wat wordt moeilijker? Eén zin is genoeg.
