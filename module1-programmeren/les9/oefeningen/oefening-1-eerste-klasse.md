# Oefening 1: Je eerste klasse

> ± 30 minuten · individueel · maak een bestand `artikel.py`

Vijf stappen, allemaal in hetzelfde bestand. Test na elke stap door het bestand uit te voeren.
Je typt niets tijdens het uitvoeren: alle gegevens staan bovenaan in het bestand.

---

## A: De klasse `Artikel`

Schrijf een klasse `Artikel` met een `__init__` die drie dingen onthoudt: `naam`, `aantal` en
`prijs`. Maak daarna twee objecten en print van elk de naam.

```python
class Artikel:
    ...
    # schrijf hier __init__

appel = Artikel("Appel", 40, 0.35)
peer = Artikel("Peer", 12, 0.60)

print(appel.naam)      # Appel
print(peer.naam)       # Peer
```

> Vergeet `self` niet, in de definitie én bij elk attribuut. Dat is de fout die je vanavond
> het vaakst gaat maken.

## B: Een methode `voorraadwaarde()`

Zet een methode in de klasse die `aantal * prijs` teruggeeft. Geen `print()` binnenin: het is
dezelfde regel als in les 6.

```python
print(f"{appel.voorraadwaarde():.2f}")    # 14.00
print(f"{peer.voorraadwaarde():.2f}")     # 7.20
```

> Zonder `:.2f` krijg je voor de peer `7.199999999999999`. Dat is geen fout van jou, dat is
> hoe Python met kommagetallen werkt (les 3). Afronden bij het tonen, niet bij het rekenen.

## C: Een methode `is_bijna_leeg()`

Geeft `True` als het aantal kleiner is dan 5, anders `False`. Geef de grens een
**standaardwaarde** van 5, zodat je ze ook anders kan meegeven.

```python
print(appel.is_bijna_leeg())     # False
print(peer.is_bijna_leeg())      # False
print(peer.is_bijna_leeg(20))    # True
```

> Kijk naar de derde test. Met een standaardwaarde werkt de methode ook zonder dat je iets
> meegeeft, en met een andere grens als je dat wel doet.

## D: Een methode `toon()`

Toont één regel, met de naam links uitgelijnd en de waarde met twee cijfers na de komma:

```python
appel.toon()     # Appel           14.00 euro
peer.toon()      # Peer             7.20 euro
```

> De breedte tussen de naam en het bedrag is jouw keuze, zolang de bedragen onder elkaar staan.
> `f"{naam:12}"` uit les 5 is wat je zoekt.

## E: Een lijst met objecten

Maak een lijst met de twee objecten, en toon ze allebei met een `for`-lus.

```python
artikelen = [appel, peer, Artikel("Melk", 3, 1.15)]

for artikel in artikelen:
    artikel.toon()
```

> Eén regel in de lus. Je hoeft niet te weten hoe `toon()` werkt om `toon()` te gebruiken.
> Dat is het hele punt van een klasse.

---

## Klaar en tijd over?

- **F**: voeg een methode `verkoop(aantal)` toe die het aantal vermindert. Wat gebeurt er als je
  meer verkoopt dan er ligt? Kies: een foutmelding, of nooit onder nul zakken. Noteer je keuze
  in een commentaarregel.
- **G**: maak een tweede klasse `Klant` met `naam` en een lege lijst `gekocht`. Dat is de
  oefening met de standaardwaarde uit de les: `gekocht=None` in de `__init__`, en dan een
  nieuwe lijst maken. Probeer het eerst fout, en kijk wat er gebeurt als je twee klanten maakt.
