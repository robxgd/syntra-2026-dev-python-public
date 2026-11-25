# Antwoorden: les 2: Structuur en semantiek

Alles nagekeken in een echte browser: de accessibility tree en de DOM zijn uitgelezen via het
DevTools-protocol, niet geschat.

## De cijfers die je klassikaal kan tonen

Voor `demo/01_divsoep.html` tegenover `demo/02_semantisch.html`, met dezelfde tekst en
dezelfde informatie:

| | divsoep | semantisch |
|---|---|---|
| Landpunten in de accessibility tree | **0** | **4** (`banner`, `navigation`, `main`, `contentinfo`) |
| Koppen | **0** | **1** (`h1`) |
| Links die een schermlezer kan opnoemen | 0 | 3 |

Dat is de kern van de avond in één tabel: **dezelfde pagina, nul landmarks of vier**. Wie met
een schermlezer werkt, kan in de tweede versie met één sneltoets naar de inhoud springen, en
in de eerste moet hij door alles heen.

## Oefening 1: Van divsoep naar structuur

Het origineel telt **8 `div`-elementen, 0 `nav`, 0 `main`, 0 `header`, 0 `footer`, 0 koppen**.
De afbeelding heeft geen `alt`.

De bedoelde oplossing:

```html
<header>
  <h1>Koffiebar Zeven</h1>
  <nav>
    <ul>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#locatie">Locatie</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</header>
<main>
  <h2>Onze koffie</h2>
  <p>Wij branden zelf, elke week, in kleine hoeveelheden. Dat ruik je.</p>
  <h2>De bonen</h2>
  <p>Twee soorten: een huisblend met chocolade, en een Ethiopische met citrus.</p>
  <h2>De machines</h2>
  <p>Een espresso-machine van tweedehandse makelij, gerestaureerd in 2024.</p>
  <aside>
    <h2>Wist je dat</h2>
    <p>Koffiebonen na het branden nog twee weken gas blijven afgeven.</p>
  </aside>
</main>
<footer>
  <p>Zevenstraat 7, 2000 Antwerpen. Open van maandag tot zaterdag, 8u tot 17u.</p>
  <img src="img/kop.svg" alt="">
</footer>
```

Waar je op moet letten bij het verbeteren:

- **Twee `h1`-kandidaten.** "Koffiebar Zeven" en "Onze koffie". Beide verdedigbaar, en het
  gesprek erover is meer waard dan het juiste antwoord. De hint in de oefening stuurt naar de
  zaaknaam als `h1`, omdat de pagina één pagina van de zaak is. Wie "Onze koffie" als `h1`
  neemt en de zaaknaam in een `p` zet, is ook juist bezig, zolang hij het kan uitleggen.
- **De `aside`.** "Wist je dat" hoort bij de pagina maar niet bij de hoofdstroom. Een `aside` is
  precies dat. Een `section` is ook verdedigbaar, een `div` niet.
- **De afbeelding.** In de `footer` naast het adres is ze versiering, dus `alt=""` is het goede
  antwoord. Wie een beschrijvende alt schrijft mag dat ook, maar dan moet hij zeggen wat de
  afbeelding toevoegt. Zemelen over de alt van een sierlijke koffiekop is tijdverlies: gebruik
  het als voorbeeld van punt 10.
- **De `span`-elementen** mogen gewoon verdwijnen. Ze deden niets.

## Oefening 2: De checklist toepassen

De zeven overtredingen in `checklist_oefening.html`, geteld in de browser:

| # | Vaststelling | Bewijs |
|---|---|---|
| 1 | Geen duidelijke `h1`: "Loketten" is `h3`, "Openingsuren" is `h1` | `document.querySelectorAll('h1').length` → 1, maar het is de tweede kop van de pagina |
| 2 | Koppen springen `h3` → `h1` → `h5` | de accessibility tree geeft level 3, 1, 5 |
| 3 en 4 | Geen `header`, `main` of `footer` | 0 landmarks in de accessibility tree |
| 5 | Geen `nav`, links niet in een lijst | `document.querySelectorAll('nav').length` → 0 |
| 7 | 8 `div`-elementen waar semantiek past | `document.querySelectorAll('div').length` → 8 |
| 8 | De `img` heeft geen `alt` | `document.querySelectorAll('img[alt]').length` → 0 |
| 12 | "klik hier" als linktekst | de vierde link in de lijst met links |

Twee dingen om klassikaal te benoemen:

- **Punt 8, en wat er precies gebeurt.** Een `img` zonder `alt` verdwijnt niet uit de
  accessibility tree, maar krijgt een **lege naam**. Het element bestaat en is onbruikbaar. Dat
  is precies het verschil met `alt=""`: dan wordt de afbeelding **overgeslagen** (`role=none`,
  `ignored=true`). Laat beide naast elkaar zien, het is een van de weinige plekken waar een leeg
  attribuut het verschil maakt tussen "onzichtbaar" en "kapot".
- **Punt 12.** Laat de lijst met links voorlezen. "Loketten, Openingsuren, Contact, klik hier".
  Dan is de vraag wat de vierde link doet, en niemand weet het.

## Oefening 3: Je eigen pagina

Geen vast antwoord. Deze vier zijn de keuring:

1. `document.querySelectorAll('h1').length` → **1**
2. geen sprongen in de koppen (vraag ze de accessibility tree of `[h1,h2,h3]` op te sommen)
3. `document.querySelectorAll('img[alt]').length` → gelijk aan het aantal `img`
4. de toetsenbordtest: Tab door alle drie de links, focus zichtbaar

Fouten die je bijna altijd ziet:

| Fout | Wat je ziet |
|---|---|
| `id` op de `section` vergeten, wel `href="#iets"` | de link werkt niet, de pagina springt nergens heen |
| `h1` in de header én in de main | twee `h1`, en de screenreader leest de paginanaam dubbel |
| `alt` met "afbeelding van ..." | overbodig, "afbeelding" zegt een screenreader zelf al |
| `nav` met losse links, zonder `ul` | het aantal links wordt niet vooraf gemeld |

## De demo's, met de cijfers erbij

| Demo | Wat je toont |
|---|---|
| `01_divsoep.html` | 0 landmarks, 0 koppen. De pagina ziet er verzorgd uit en is voor een schermlezer een woordenbrij |
| `02_semantisch.html` | 4 landmarks, 1 `h1`, 3 links. Zelfde tekst |
| `03_koppen_hierarchie.html` | levels 3, 1, 4, 2, 5 in de accessibility tree |
| `04_koppen_juist.html` | levels 1, 2, 3, 2, 2. Zelfde tekst, zelfde uitzicht |
| `05_afbeeldingen.html` | vier soorten `img`: met alt, met `alt=""` (overgeslagen), als link, en zonder alt (lege naam) |
| `06_standaardstijl.html` | wat de browser zelf doet met `header`, `nav`, `main` en `footer`, zonder enige CSS |

Demo 3 en 4 zijn de mooiste van de avond, want ze zien er **identiek** uit. Alleen in het
Elements-paneel en in de accessibility tree zie je het verschil. Dat is het hele argument voor
semantiek in één oefening.
