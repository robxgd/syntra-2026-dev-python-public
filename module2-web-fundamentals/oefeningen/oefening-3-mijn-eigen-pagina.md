# Oefening 3: Je eigen pagina, van nul

> ± 30 minuten · individueel · je hebt `mijn_pagina.html` als startpunt

De eerste oefening waarbij je de inhoud zelf kiest. Je bouwt een pagina over jezelf, met de
structuur die je vanavond hebt geleerd. Dit bestand groeit de rest van de module mee: in les 3
krijgt het opmaak, in les 5 een formulier.

---

## De opdracht

Open `mijn_pagina.html`. Je ziet een pagina met alleen `div`-elementen en invultekst. Bouw hem
om tot een echte pagina over jezelf, met deze onderdelen:

| Onderdeel | Eis |
|---|---|
| Een `header` | met je naam als `h1` |
| Een `nav` | met minstens drie links naar onderdelen op de pagina zelf |
| Een `main` | met minstens drie `section`-elementen, elk met een `h2` |
| Eén `article` | iets dat op zichzelf leesbaar is, bijvoorbeeld je motivatie om deze opleiding te volgen |
| Een `footer` | met je naam en het jaar |
| Minstens één afbeelding | met een `alt` die je kan verantwoorden |
| Minstens één lijst | met een `ul` of een `ol` |

De drie links in de `nav` moeten echt werken: gebruik `id`-attributen op de `section`-elementen
en link ernaartoe met `href="#datid"`.

## Eisen waar je op afgerekend wordt

Deze vier zijn niet optioneel:

1. **Exact één `h1`.** Niet twee, niet nul.
2. **Geen sprongen in de koppen.** Na een `h1` komt een `h2`, en pas daarna een `h3`.
3. **Elke `img` heeft een `alt`-attribuut.** Leeg mag, als je er een reden voor hebt.
4. **De pagina werkt met het toetsenbord.** Klik in de adresbalk, druk op Tab, en je moet door
   alle drie de links kunnen gaan en zien waar je staat.

## Controleren

```javascript
document.querySelectorAll('h1').length          // moet 1 zijn
document.querySelectorAll('img[alt]').length    // moet gelijk zijn aan het aantal img's
document.querySelectorAll('main').length        // moet 1 zijn
```

En de belangrijkste controle, die geen code heeft: laat je pagina door iemand anders voorlezen
met een screenreader, of gebruik zelf de voorleesfunctie van je browser. Je hoort meteen of de
structuur klopt.

## Klaar en tijd over?

- Voeg een `aside` toe met een leuk weetje over jezelf, en zorg dat de `h2` erin past bij de
  rest van de koppenstructuur.
- Zoek op wat `figure` en `figcaption` doen, en gebruik ze voor je afbeelding als ze passen.
  Let op: dan mag de `alt` leeg worden, want het onderschrift doet het werk.
