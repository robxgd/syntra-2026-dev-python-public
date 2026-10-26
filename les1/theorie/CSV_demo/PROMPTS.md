# Uitgewerkte demonstratieprompts

Gebruik deze voorbeelden als docentdemonstratie. De voorbeeldreacties zijn didactische reconstructies, geen metingen van een specifieke vendor.

## 1  Copy paste uit een gewone LLM chat

Open `starter/csv_import.py` en `starter/test_csv_import.py`. Plak beide bestanden in een gewone chat, gevolgd door:

> Deze functie leest CSV-orders. Drie tests falen: een lege regel wordt als fout geteld, een ongeldige datum noemt het fysieke regelnummer niet en een ongeldig bedrag heeft geen specifieke melding. Stel een kleine wijziging voor. Houd `import_orders(csv_text)` en het retourtype gelijk. Leg uit hoe je het fysieke regelnummer bepaalt. Geef ook aan welke aannames je maakt.

**Wat je verwacht te bespreken:** de chat kan alleen werken met wat je plakte. Een voorstel zoals `if not row: continue` verhelpt de lege regel, maar niet automatisch de foutmeldingen. Een voorstel op basis van `enumerate(reader, start=2)` kan verkeerde fysieke regelnummers geven bij lege regels of CSV-records die meerdere regels innemen. In deze casus biedt `reader.line_num` het relevante fysieke regelnummer.

## 2  Suggestie in de editor

Plaats de cursor direct na `for row in reader:` in de startversie. Een plausibele suggestie is:

```python
if not row:
    continue
```

**Wat je verwacht te bespreken:** dit is een nuttige lokale edit. Zij lost de datum- en bedragmeldingen nog niet op. Laat zien dat een geaccepteerde aanvulling pas één stap in het werk is.

## 3  Chat met projectcontext

Open de map `starter` in een editor met projectchat en gebruik:

> Lees `csv_import.py` en `test_csv_import.py`. Geef eerst in drie zinnen aan waarom de drie tests falen. Stel daarna de kleinste wijziging in `csv_import.py` voor die de eisen vervult. Toon de diff. Wijzig de tests niet.

**Wat je verwacht te bespreken:** controleer in de tool welke bestanden hij echt heeft gelezen. Bekijk daarna of de diff de publieke functie intact laat en of hij fysieke regelnummers gebruikt.

## 4  Lokale coding agent

Open uitsluitend `starter` als project en gebruik:

> Pas `import_orders` aan zodat lege CSV-regels worden genegeerd en fouten het fysieke regelnummer vermelden. Houd de publieke functie gelijk. Draai `python3 -m unittest -v` en toon de diff. Wijzig de tests niet zonder eerst uit te leggen waarom.

**Wat je verwacht te bespreken:** de agent mag de code onderzoeken, wijzigen en tests draaien voor zover jouw configuratie dat toestaat. Beoordeel de acties onderweg. Als hij een test groen maakt door de verwachte uitkomst te versoepelen, wijs dat af als inhoudelijk onjuiste oplossing.

## 5  Gedelegeerde agent of cloudtaak

Gebruik onderstaande taakomschrijving. Start een cloudtaak vooraf, als je toegang hebt. De les werkt ook zonder een werkelijk uitgevoerde cloudtaak: behandel de map `reference` dan als een voorbeeldresultaat ter review.

> Verbeter de bestaande CSV-importer. Acceptatiecriteria: (1) lege CSV-regels worden genegeerd, (2) fouten noemen het fysieke regelnummer, (3) ongeldige datum en ongeldige hoeveelheid krijgen afzonderlijke meldingen, (4) de publieke functie en de bestaande headercontrole blijven gelijk, (5) voer de testset uit en vermeld de uitkomst. Lever een diff of pull request ter review. Voeg geen externe dependency toe.

**Review van het resultaat:** open het gewijzigde bestand, controleer de foutmelding op regel 3, lees de testuitvoer en bekijk of er onverwachte bestanden zijn aangepast. Accepteer de wijziging pas na die controle.

## Twee aanvullende vragen voor klassikale bespreking

- Wat gebeurt er als de CSV een geciteerd veld met een regelovergang bevat? Dan kunnen een recordnummer en een fysiek regelnummer verschillen.
- Wat bewijst een groene testset niet? Zij zegt niets over invoer die niet in de tests voorkomt, zoals een ontbrekende kolom of een afwijkende encoding.
