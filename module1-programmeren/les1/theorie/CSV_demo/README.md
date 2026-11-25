# CSV-importer demonstratie

Dit pakket hoort bij de les *Development harnesses* van 7 oktober 2026. Het is materiaal voor de docent; studenten hoeven niets uit te voeren.

In `PROMPTS.md` staan kant-en-klare prompts en bespreekpunten voor alle vijf werkvormen.

## Benodigdheden

- Python 3.10 of nieuwer
- Geen externe packages of internetverbinding

## Startversie

Ga naar `starter` en voer uit:

```bash
python3 -m unittest -v
```

Verwachte uitkomst: 5 tests, waarvan 2 slagen en 3 falen. De lege CSV-regel wordt als fout geteld en foutmeldingen missen een fysiek regelnummer.

## Referentie-uitwerking

Ga naar `reference` en voer hetzelfde commando uit. Verwachte uitkomst: 5 geslaagde tests.

De uitwerking slaat lege rijen over, gebruikt `csv.reader.line_num` voor het fysieke regelnummer, en maakt een onderscheid tussen datumfouten, bedragfouten en een verkeerd aantal kolommen.

## Prompt voor een lokale coding agent

> Pas `import_orders` aan zodat lege CSV-regels worden genegeerd en fouten het fysieke regelnummer vermelden. Houd de publieke functie gelijk. Draai de tests en toon de diff. Wijzig de tests niet zonder eerst uit te leggen waarom.

Open de map `starter` als repository of project. Laat de agent lezen en wijzigen binnen die map en laat alleen de testopdracht uitvoeren die hierboven staat. Als de agent extra bestanden wijzigt, bespreek waarom.

## Wat je bij de review laat zien

1. Een lege regel veroorzaakt geen foutmelding.
2. De ongeldige datum op fysieke regel 3 geeft precies `Line 3: invalid date '2026-02-30'`.
3. Een ongeldige hoeveelheid op regel 2 geeft een afzonderlijke foutmelding.
4. De bestaande functiehandtekening en het headergedrag zijn behouden.
5. De vijf meegeleverde tests slagen in de referentieversie.

## Reserveaanpak zonder agent of netwerk

Toon eerst de falende tests in `starter`. Open daarna `reference/csv_import.py`, vergelijk de functies en voer de tests in `reference` uit. Daarmee blijft de inhoud van de demo gelijk, ook zonder live agent.
