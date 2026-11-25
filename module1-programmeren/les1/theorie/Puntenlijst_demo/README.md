# Puntenlijst demonstratie

Dit pakket hoort bij de les *Development harnesses*. Het voorbeeld gebruikt alleen lijsten (arrays), een `for`-lus en `if`/`elif`/`else`.

## De vraag

Een puntenlijst bevat de scores `[8, 10, 14, -1, 21, 7]`.

- Geldige scores liggen tussen 0 en 20, inclusief beide grenzen.
- Een geldige score van 10 of meer is geslaagd.
- Een geldige score onder 10 is niet geslaagd.
- Ongeldige scores komen alleen in de lijst `ongeldig`.
- De volgorde van de scores blijft behouden.

## Uitvoeren

Open een terminal in `starter` en voer `python3 punten.py` uit. De uitvoer is bewust fout:

```text
Geslaagd: [14, 21]
Niet geslaagd: [8, 10, -1, 7]
Ongeldig: []
```

Open daarna `reference` en voer hetzelfde commando uit. De uitvoer moet gelijk zijn aan `verwachte_uitvoer.txt`:

```text
Geslaagd: [10, 14]
Niet geslaagd: [8, 7]
Ongeldig: [-1, 21]
```

## Kern van de fout

De startversie gebruikt `punt > 10`, waardoor 10 verkeerd wordt ingedeeld. Zij controleert niet of een score tussen 0 en 20 ligt. Daardoor komt 21 ten onrechte bij de geslaagden en -1 bij de niet-geslaagden.

## Reserveaanpak

Zonder live AI-agent toon je eerst de uitvoer van `starter/punten.py`, daarna de wijziging in `reference/punten.py` en tot slot de correcte uitvoer. Alle leerpunten over context, acties en review blijven zichtbaar.
