# Oefening 1: Je eerste eigen programma

> ± 30 minuten · individueel · maak een bestand `prijs.py`

Dit is de eerste keer dat je zelf een programma schrijft. We bouwen het in zes stappen op.
**Voer na élke stap uit.** Niet één keer op het einde: dan weet je niet meer waar het misging.

Je bouwt een prijsberekening met btw: je geeft een bedrag exclusief btw in, en het programma
toont wat de klant moet betalen.

---

## Stap 1: Vraag iets aan de gebruiker

```python
prijs_tekst = input("Prijs zonder btw: ")
print(prijs_tekst)
```

▶ Uitvoeren. Typ `100`. Je ziet `100` verschijnen.

## Stap 2: Kijk wat voor soort waarde je hebt

Voeg toe:

```python
print(type(prijs_tekst))
```

▶ Uitvoeren. Je ziet `<class 'str'>`. Dat is **tekst**, geen getal. Onthoud dit.

## Stap 3: Zet het om naar een getal

Voeg toe:

```python
prijs = float(prijs_tekst)
print(type(prijs))
```

▶ Uitvoeren. Nu staat er `<class 'float'>`. Vanaf hier kan je ermee rekenen.

## Stap 4: Reken de btw uit

Voeg toe:

```python
btw = prijs * 0.21
print(btw)
```

▶ Uitvoeren met `100`. Je ziet `21.0`.

## Stap 5: Bereken het totaal

Voeg toe:

```python
totaal = prijs + btw
print(totaal)
```

▶ Uitvoeren met `100`. Je ziet `121.0`.

## Stap 6: Toon het netjes

Vervang je drie losse `print`-regels door één nette weergave:

```python
print(f"Prijs zonder btw: {prijs} euro")
print(f"Btw (21%):        {btw} euro")
print(f"Te betalen:       {totaal} euro")
```

▶ Uitvoeren met `100`.

---

## Nu breken

Je programma werkt. Test het met de randgevallen uit les 2 en noteer wat er gebeurt:

| Invoer | Wat gebeurt er? | Crash of stille fout? |
|---|---|---|
| `100` | | |
| `12,50` | | |
| `0` | | |
| `-50` | | |
| `abc` | | |
| *(leeg, meteen Enter)* | | |

> Twee daarvan crashen niet. Welke, en waarom is dat erger?

## Klaar en tijd over?

- Toon het bedrag afgerond op twee cijfers: `{totaal:.2f}` in plaats van `{totaal}`.
- Vraag het btw-percentage ook aan de gebruiker in plaats van 21% vast te zetten.
