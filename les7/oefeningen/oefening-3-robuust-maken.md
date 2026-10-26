# Oefening 3: Maak je eigen programma robuust

> ± 35 minuten · individueel · je **huistaak** van les 6
> Niets mee? Gebruik `reserve_kassa.py` uit deze map.

Je programma werkt bij nette invoer. Vanavond zorg je dat het niet meer omvalt bij onnette
invoer, en dat het iets zinnigs zegt in plaats van een foutmelding.

---

## Stap 1: Breek het eerst

Neem je testtabel uit de huistaak erbij, of maak er nu een. Test je programma met minstens
deze zes categorieën en noteer wat er gebeurt:

| Categorie | Wat ik intypte | Wat er gebeurde |
|---|---|---|
| leeg (meteen Enter) | | |
| tekst waar een getal hoort | | |
| een komma in een bedrag | | |
| nul | | |
| negatief | | |
| onrealistisch groot | | |

## Stap 2: Voorkomen of opvangen?

Voor elk geval uit stap 1, beslis:

- **Voorkomen (validatie)**: je controleert de waarde vóór je hem gebruikt en vraagt opnieuw.
- **Opvangen (`try`/`except`)**: je laat het misgaan en handelt de fout netjes af.
- **Laten crashen**: dit is een fout in jouw code, geen gebruikersfout. Die moet zichtbaar blijven.

| Geval | Voorkomen / opvangen / laten crashen | Waarom |
|---|---|---|
| leeg | | |
| tekst | | |
| komma | | |
| nul | | |
| negatief | | |
| te groot | | |

## Stap 3: Bouw het in

Werk van boven naar beneden door je programma. Voer na elke toevoeging opnieuw uit met
je testtabel.

Bruikbare stukken uit de demo's van vanavond:

- `../theorie/03_try_except.py` blok 6: meerdere fouten apart opvangen
- `../theorie/04_validatie.py` blok 1: een controlefunctie die een foutmelding of `None` teruggeeft
- `../theorie/04_validatie.py` blok 2: blijven vragen tot het klopt

## Stap 4: Twee regels waar je je aan houdt

1. **Geen kale `except:`.** Vang op wat je verwacht: `except ValueError`, `except ZeroDivisionError`.
   Een kale `except:` verstopt je eigen tikfouten.
2. **Een foutmelding die de gebruiker begrijpt.** Niet `ValueError`, wel
   *"Vul een bedrag in met een punt, bijvoorbeeld 12.50."*

## Stap 5: Controle

| | ✓ |
|---|---|
| Alle zes categorieën uit stap 1 geven nu een nette melding of worden voorkomen | |
| Er staat nergens een kale `except:` | |
| Elke foutmelding is begrijpelijk voor iemand die geen Python kent | |
| Het programma werkt nog steeds correct bij normale invoer | |

> Die laatste is niet vanzelfsprekend. Test na al je aanpassingen nog één keer met gewone,
> correcte waarden.

---

## De no-AI ronde (laatste 20 minuten)

**Laptops dicht wat AI betreft: geen Copilot, geen Claude, geen Codex.**

Ik loop rond en vraag je bij een stuk van je eigen code:

- Wat doet deze regel?
- Waarom heb je hier gekozen voor validatie in plaats van `try`/`except`?
- Wat gebeurt er als ik hier een komma intyp?

Dit is exact wat er op 25 november gebeurt, alleen dan met punten erop. Vandaag is het
gratis oefenen.
