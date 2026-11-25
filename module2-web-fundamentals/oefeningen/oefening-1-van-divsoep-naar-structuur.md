# Oefening 1: Van divsoep naar structuur

> ± 35 minuten · individueel · je hebt `divsoep_koffiebar.html` nodig

Een pagina die er verzorgd uitziet, en waarin elk element een `div` of een `span` is. Negen
van de tien webpagina's in het wild zien er zo uit. Jij gaat hem ombouwen zonder één letter
tekst te wijzigen.

---

## De opdracht

Open `divsoep_koffiebar.html` in VS Code en in de browser. Bewaar het origineel: maak een
tweede bestand `koffiebar.html` en werk daarin.

**Je mag geen tekst wijzigen, toevoegen of weghalen.** Je vervangt alleen `div` en `span` door
elementen die betekenis hebben.

## Stap 1: Kijken wat er ontbreekt

Open het origineel in de browser en open het Elements-paneel. Beantwoord eerst deze vragen:

| Vraag | Antwoord |
|---|---|
| Hoeveel koppen heeft deze pagina? | |
| Hoeveel `div`-elementen? | |
| Hoeveel landpunten (`header`, `main`, `footer`, `nav`)? | |
| Heeft de afbeelding een alt? | |

Je gaat zo merken dat een pagina die er goed uitziet, voor een screenreader niets anders is
dan een lange rij losse woorden.

## Stap 2: Ombouwen

Vervang stap voor stap. Voer na elke stap uit en kijk of er niets verschoven is: **de pagina
moet er op het scherm bijna hetzelfde uitzien**. Semantiek verandert de structuur, niet de
opmaak.

| Wat er staat | Wat het moet worden |
|---|---|
| `div.header` | `header` |
| `div.brand` met de naam van de zaak | de `h1` van de pagina |
| `div.nav` met drie links | `nav`, met de links in een `ul` met `li` |
| `div.content` | `main` |
| `div.big-title` | de `h1` (verhuist dus naar hierboven, zie volgende stap) |
| `div.sub-title` | `h2` |
| `div.extra` met een titel | `aside`, met de titel als `h2` |
| `div.bottom` | `footer` |
| `span` om een stukje tekst | `strong` of `em` als het echt nadruk is, anders gewoon niets |

!!! warning "Er kan maar één h1 zijn"

    De naam van de zaak is een `h1` in het origineel, maar het is de paginatitel niet. Kies: of
    de naam van de zaak wordt de `h1`, of de titel van de inhoud wordt de `h1` en de zaak staat
    in de `header` als gewone tekst of als `p`. Beide zijn verdedigbaar, en je moet er één kiezen
    en kunnen uitleggen waarom. Dat is precies wat er op het examen gevraagd wordt.

## Stap 3: De afbeelding

De afbeelding onderaan heeft geen `alt`. Beslis zelf:

- Draagt ze iets bij dat je niet uit de tekst kan halen? Geef een beschrijvende `alt`.
- Is ze enkel versiering? Geef `alt=""`.

Schrijf in een commentaarregel boven de `img` waarom je die keuze maakte. Eén zin.

## Stap 4: Controleren met de checklist

Neem `../semantiek-en-a11y-checklist.md` erbij en loop de vijftien punten af. Je hoeft nog niet
alles te halen: punt 13 tot 15 (toetsenbord) komen pas echt aan bod bij formulieren, in les 5.

## Wat je zou moeten hebben

Na het ombouwen:

- **één** `h1`, en de rest `h2`
- een `header`, een `nav`, een `main`, een `aside` en een `footer`
- drie links, in een `ul` met drie `li`
- een `img` met een `alt`-attribuut (leeg of gevuld, jouw keuze met een reden)
- nul `div`-elementen die nog iets betekenen

Controleer met de console:

```javascript
document.querySelectorAll('h1').length          // 1
document.querySelectorAll('div').length         // 0, of alleen wat echt geen betekenis heeft
document.querySelectorAll('img[alt]').length    // gelijk aan het aantal img's
```

## Klaar en tijd over?

Open de pagina met de toetsenbordtest uit de checklist: klik in de adresbalk en druk op Tab.
Je gaat nu door de drie links en kom je onderaan uit. Vraag je af of die volgorde logisch is.
