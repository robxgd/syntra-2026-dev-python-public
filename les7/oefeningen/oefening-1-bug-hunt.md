# Oefening 1: Bug hunt

> ± 30 minuten · individueel · vijf bestanden `bug_1.py` t/m `bug_5.py`

Vijf programma's, vijf fouten. Twee syntaxfouten, twee runtimefouten, één logische fout.

## Werkwijze: deze keer strikt

Voor elk bestand, in deze volgorde:

1. **Lees** het programma. Schrijf als commentaarregel je hypothese op: wat gaat er mis, en waar?
2. **Voer uit.** Lees de foutmelding **van onder naar boven**.
3. **Noteer als commentaar** wat er echt misging.
4. **Repareer** en voer opnieuw uit.

> Stap 1 overslaan is de gewoonte die je hier moet afleren. Wie meteen dingen begint te
> veranderen tot het werkt, leert niet debuggen. Die gokt.

---

## Per bestand

**`bug_1.py`**: start niet op. Waar onderstreept VS Code?

**`bug_2.py`**: lees de foutmelding letterlijk. Ze zegt exact wat ontbreekt.
Welke gewoonte voorkomt deze fout bij lange regels?

**`bug_3.py`**: crasht bij het uitvoeren. Hoeveel producten zitten er in de lijst,
en welke posities bestaan er dan?

**`bug_4.py`**: de eerste klant lukt, de tweede niet. De traceback heeft twee niveaus.
Welke regel veroorzaakte het, en welke regel riep die aan?

**`bug_5.py`**: **crasht niet.** Er zijn vier leerlingen geslaagd (12 of meer op 20).
Wat telt het programma? Kijk goed naar het vergelijkingsteken.

---

## De vraag achteraf

Vier van deze vijf fouten meldden zichzelf. Eén niet.

Welke was dat, en hoe lang zou die in een echt programma kunnen meedraaien voor iemand
hem opmerkt?

## Klaar en tijd over?

Neem `bug_4.py` na je reparatie. Je hebt de crash weg, maar wat toon je nu voor een klant
zonder bestellingen? Is dat een goede keuze? Er is meer dan één verdedigbaar antwoord,
noteer het jouwe in een commentaarregel.
