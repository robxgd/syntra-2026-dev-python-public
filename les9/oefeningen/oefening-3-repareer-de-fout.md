# Oefening 3: Repareer de fout

> ± 20 minuten · individueel · drie bestanden in deze map

Drie kapotte programma's. Eén crasht met een melding, één crasht niet maar toont onzin, één
crasht op een plaats die niets met de oorzaak te maken heeft.

Werk ze in deze volgorde, en voer na elke reparatie opnieuw uit.

---

## 1. `fout_1_self.py`

```
TypeError: Cursist.__init__() takes 2 positional arguments but 3 were given
```

Je gaf er twee. Waar komt het derde vandaan?

> Denk terug aan de les: bij een object roept Python de methode aan met het object erbij.

## 2. `fout_2_haakjes.py`

Geen foutmelding. Op het scherm staat iets als:

```
Gemiddelde: <bound method Cursist.gemiddelde of <__main__.Cursist object at 0x7f...>>
```

Wat je print is de methode zelf, niet wat ze teruggeeft.

> Dit is de gevaarlijkste van de drie: het programma draait, dus niets waarschuwt je.

## 3. `fout_3_return.py`

Eerst verschijnt een naam, dan:

```
TypeError: 'NoneType' object is not subscriptable
```

De fout staat op de laatste regel, de oorzaak staat in de klasse. Zoek de methode die iets
toont waar ze iets moest teruggeven.

> Dit is exact dezelfde fout als `fout_1_geen_return.py` uit les 6, nu binnen een klasse.
> De vorm is nieuw, de fout niet.

---

## Controle

| | ✓ |
|---|---|
| Alle drie de bestanden draaien zonder foutmelding | |
| `fout_2_haakjes.py` toont een getal in plaats van een methode | |
| `fout_3_return.py` toont de naam van de beste cursist twee keer, zonder crash | |
| Je kan in één zin zeggen wat er in elk bestand fout was | |

---

## Klaar en tijd over?

`fout_3_return.py` print de naam nu twee keer: één keer binnen de methode, één keer buiten.
Haal de `print()` uit de methode en laat alleen de buitenste over. Dat is de opruiming die je
in les 6 leerde: tonen gebeurt buiten de berekening.
