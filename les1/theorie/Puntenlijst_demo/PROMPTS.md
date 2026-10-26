# Demonstratieprompts voor vijf werkvormen

Dit zijn docentvoorbeelden. Zij vormen geen opdracht voor studenten.

## 1  Gewone LLM chat

Plak de inhoud van `starter/punten.py` in een gewone chat en voeg toe:

> Deze Python-code verwerkt een puntenlijst. Geldige scores zijn 0 tot en met 20. Vanaf 10 is een student geslaagd. Ongeldige scores horen alleen in `ongeldig`. Leg de fouten uit en stel de kleinste wijziging voor. Gebruik alleen arrays, een lus en voorwaarden.

**Bespreek:** de chat ziet alleen de code die je plakt. Hij kan het bestand niet zelf wijzigen of het programma uitvoeren.

## 2  Suggestie in de editor

Plaats de cursor op de regel `if punt > 10:`. Een mogelijke aanvulling is `if punt >= 10:`.

**Bespreek:** dit corrigeert de grensscore 10, maar nog niet de ongeldige scores -1 en 21.

## 3  Chat met projectcontext

Open de hoofdmap van dit demoarchief in een editor met projectchat en gebruik:

> Lees `starter/punten.py` en `verwachte_uitvoer.txt`. Leg uit waarom de huidige uitvoer verschilt van de verwachte uitvoer. Stel een kleine wijziging voor in `starter/punten.py` en toon de diff. Gebruik alleen lijsten, een lus en voorwaarden.

**Bespreek:** kijk welke bestanden de tool daadwerkelijk heeft gelezen en controleer de voorgestelde diff.

## 4  Lokale coding agent

Open de hoofdmap van dit demoarchief als project en gebruik:

> Pas `starter/punten.py` aan zodat de uitvoer klopt met `verwachte_uitvoer.txt`. Geldige scores liggen tussen 0 en 20; vanaf 10 is een score geslaagd. Ongeldige scores komen alleen in `ongeldig`. Gebruik alleen lijsten, een lus en voorwaarden. Voer `python3 starter/punten.py` uit en toon de diff.

**Bespreek:** de agent kan de code lezen, wijzigen en uitvoeren als zijn rechten dat toelaten. Kijk of hij de eenvoudige structuur behoudt en niet onnodig functies of libraries toevoegt.

## 5  Gedelegeerde agent

Gebruik deze taakomschrijving als je vooraf een aparte agenttaak kunt voorbereiden:

> Verbeter de indeling van de puntenlijst in `starter/punten.py`. Acceptatiecriteria: scores buiten 0 tot en met 20 staan uitsluitend in `ongeldig`; geldige scores van 10 of meer staan in `geslaagd`; andere geldige scores staan in `niet_geslaagd`; de volgorde blijft behouden; de uitvoer komt overeen met `verwachte_uitvoer.txt`. Houd de code op beginnersniveau en gebruik alleen lijsten, een lus en voorwaarden. Lever de gewijzigde code en de uitvoer ter review.

**Review:** bekijk vooral de scores 10, -1 en 21. Controleer ook of de overige scores in dezelfde volgorde blijven staan.
