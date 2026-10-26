# Oefening 1: Je eerste functies

> ± 30 minuten · individueel · maak een bestand `functies.py`

Vijf functies. Test elke functie meteen door ze op te roepen en het resultaat te tonen.

**Regel voor alle vijf: gebruik `return`, geen `print()` binnenin.** De functie berekent iets;
het tonen doe je erbuiten.

---

## A: `verdubbel(getal)`

Geeft het dubbele terug.

```python
print(verdubbel(5))     # 10
print(verdubbel(2.5))   # 5.0
```

## B: `is_meerderjarig(leeftijd)`

Geeft `True` of `False` terug.

```python
print(is_meerderjarig(20))   # True
print(is_meerderjarig(17))   # False
print(is_meerderjarig(18))   # True
```

> Let op de grens. Test alle drie.

## C: `duurste(prijzen)`

Krijgt een lijst en geeft het hoogste bedrag terug.

```python
print(duurste([12.50, 8.00, 21.75]))   # 21.75
print(duurste([-3, -7, -1]))           # -1
```

> De tweede test is er niet voor niets. Denk aan les 4.

## D: `initialen(voornaam, achternaam)`

Geeft de initialen terug in hoofdletters, met punten.

```python
print(initialen("rob", "hofman"))    # R.H.
print(initialen("Sofie", "Peeters")) # S.P.
```

## E: `korting(bedrag, procent)`

Geeft het bedrag ná korting terug.

```python
print(korting(100, 10))    # 90.0
print(korting(50, 0))      # 50.0
```

---

## De controlevraag

Neem functie E en voer dit uit:

```python
resultaat = korting(100, 10)
print(resultaat + 5)
```

Krijg je `95.0`? Dan gebruikte je `return`.
Krijg je een foutmelding over `None`? Dan staat er een `print()` waar `return` hoort.

## Klaar en tijd over?

- **F**: `gemiddelde(getallen)` die ook werkt bij een **lege** lijst. Wat geef je dan terug?
  Er is geen fout antwoord, maar je moet kiezen. Noteer je keuze in een commentaarregel.
- **G**: `is_geldig_bedrag(tekst)` die `True` geeft als de tekst omgezet kan worden naar een
  getal. Tip: gebruik voorlopig `.replace(",", ".")` en kijk of alle tekens cijfers of punten zijn.
