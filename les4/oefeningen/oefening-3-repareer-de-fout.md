# Oefening 3: Repareer de fout

> ± 25 minuten · individueel · vier bestanden in deze map

Vier programma's met een lus. Alle vier zijn ze syntactisch correct. Geen enkele doet wat hij
zou moeten doen.

## Werkwijze per bestand

1. **Lees** het programma en schrijf als commentaarregel op wat je denkt dat er misgaat.
   **Vóór je uitvoert.**
2. **Voer uit** volgens de instructie bovenaan het bestand.
3. **Noteer als commentaar** wat er echt misging, en of je hypothese klopte.
4. **Repareer** het.
5. **Voer opnieuw uit** ter controle.

---

| Bestand | Wat te doen | Zou moeten geven |
|---|---|---|
| `fout_1_som.py` | gewoon uitvoeren | 60 |
| `fout_2_grootste.py` | uitvoeren, dan de wintertemperaturen aanzetten | 24, daarna −1 |
| `fout_3_gemiddelde.py` | uitvoeren, dan een zesde score toevoegen | 15.0, daarna 16.0 |
| `fout_4_aftellen.py` | ⚠️ uitvoeren en **stoppen met Ctrl+C** | 5 4 3 2 1 Start! |

## Twee bestanden zijn extra gemeen

`fout_2` en `fout_3` geven bij de eerste test **het juiste antwoord**. Ze gaan pas onderuit
als je de gegevens verandert.

Dat is het soort fout dat maanden meegaat: het programma is getest, het werkte, en dan komt er
een nieuwe klant of een extra rij bij.

Wat leer je daaruit over hoe je moet testen?

## Klaar en tijd over?

Neem `fout_4_aftellen.py` na je reparatie en laat het aftellen vanaf een getal dat de gebruiker
zelf ingeeft. Wat gebeurt er als iemand `0` intypt? En `-3`?
