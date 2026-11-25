# Oefening 2: De checklist toepassen

> ± 35 minuten · in duo's · je hebt `checklist_oefening.html` en de checklist nodig

Een echte gemeentepagina, met **acht** fouten erin. Jij gaat ze vinden met de checklist, en dan
verbeteren. Wie de fouten vindt zonder de checklist te gebruiken, heeft de vorige oefening
begrepen maar deze niet: de checklist is het gereedschap dat je op het examen bij de hand hebt.

---

## Stap 1: Vinden

Open `checklist_oefening.html` in de browser. Neem
`../semantiek-en-a11y-checklist.md` erbij en loop alle vijftien punten af. Schrijf elke
overtreding op in deze vorm:

| # uit de checklist | Wat er mis is | Regel in de code |
|---|---|---|
| | | |

Er zijn **zeven** overtredingen. Vind je er minder, dan heb je een punt van de checklist
overgeslagen in plaats van een fout gemist. Ga terug.

## Stap 2: Verbeteren

Maak `gemeentehuis.html` en verbeter alle acht. Je mag niets weghalen dat informatie bevat: de
tekst blijft, alleen de structuur verandert.

Eén verbetering vraagt een keuze die je moet kunnen uitleggen, namelijk de link met de tekst
"klik hier". Los die op zoals een professionele developer het zou doen, en schrijf in een
commentaarregel waarom.

## Stap 3: Opnieuw controleren

Loop de checklist nog een keer helemaal af, nu op je eigen versie. Alles moet groen zijn,
behalve punt 12 tot 14 als je nog geen interactieve elementen hebt.

Doe ook de toetsenbordtest: klik in de adresbalk, druk op Tab, en ga door de pagina.

## Wat je zou moeten vinden

Er zijn zeven overtredingen. Zeven, niet acht: de koppenstructuur is één overtreding (punt 2),
hoeveel koppen er ook fout staan.

| # uit de checklist | Wat er mis is |
|---|---|
| 1 | Er is geen duidelijke `h1`: "Loketten" is een `h3` en "Openingsuren" een `h1`, en die twee vechten om de rol van paginatitel |
| 2 | De koppen springen: `h3` → `h1` → `h5` |
| 3 en 4 | Er is geen `header`, geen `main` en geen `footer`: de pagina heeft geen enkel landpunt |
| 5 | De navigatie is geen `nav`, en de drie links zitten niet in een lijst |
| 7 | De hele pagina is opgebouwd uit `div`-elementen waar een betekenisvol element past |
| 8 | De afbeelding heeft geen `alt`-attribuut |
| 12 | De link met de tekst "klik hier" zegt niets over waar hij naartoe gaat |

Punt 3 en 4 staan op één regel omdat één ingreep ze allebei oplost, niet omdat het één fout is.

## Hoe je punt 12 oplost

"Klik hier" is de bekendste slechte linktekst die er bestaat, en de oplossing is altijd
dezelfde: zet de bestemming in de link zelf en laat de omliggende zin kloppen.

```html
<!-- fout -->
<p>Alle regels staan in <a href="#reglement">klik hier</a>.</p>

<!-- goed -->
<p>Alle regels staan in <a href="#reglement">het reglement van de loketten</a>.</p>
```

Waarom het uitmaakt: een schermlezer kan alle links van een pagina achter elkaar opnoemen. Dan
krijg je "Loketten, Openingsuren, Contact, klik hier". De vierde link is dan onbruikbaar, ook al
werkt hij perfect met een muis.

## Klaar en tijd over?

Zoek een echte gemeentepagina of een pagina van je werk en loop de checklist af. Je gaat meer
dan acht overtredingen vinden. Kies de drie die het meest storend zijn voor iemand die de
pagina met een screenreader leest, en leg uit waarom die drie.
