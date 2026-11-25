# Oefening 2: Werken met de debugger

> ± 25 minuten · individueel · `debugger_oefening.py`
> **Geen `print()` toegestaan in deze oefening.**

Tot nu debugde je met `print()`. Dat werkt, maar het is traag: je voegt regels toe, voert uit,
leest, voegt nog regels toe. De debugger laat je het programma **stilzetten** en rondkijken.

---

## Wat het programma zou moeten doen

Elke deelnemer krijgt de som van zijn drie rondes, plus 5 bonuspunten als hij in alle drie
de rondes 10 of meer scoorde.

Met de hand nagerekend:

| Deelnemer | Rondes | Som | Bonus? | Verwacht |
|---|---|---|---|---|
| Ali | 12, 15, 15 | 42 | ja | **47** |
| Bo | 9, 8, 10 | 27 | nee (ronde 1 is 9) | **27** |
| Cem | 14, 16, 15 | 45 | ja | **50** |

Voer het uit. Ali klopt. De rest niet.

## Stap 1: Zet een breakpoint

Klik in VS Code **links van het regelnummer** van de regel `totaal = totaal + punt`.
Er verschijnt een rode bol.

## Stap 2: Start de debugger

Druk **F5**, of gebruik de afspeelknop met het kevertje. Het programma start en stopt
bij je breakpoint.

## Stap 3: Kijk rond

Links verschijnt een paneel **Variables**. Daar staan alle variabelen met hun huidige waarde.

Noteer als commentaar wat je ziet bij de allereerste stop: de waarden van `naam`, `punt`,
`totaal` en `alles_minstens_tien`.

## Stap 4: Stap verder

Gebruik deze knoppen bovenaan:

| Knop | Sneltoets | Wat het doet |
|---|---|---|
| Continue | F5 | door tot het volgende breakpoint |
| Step Over | F10 | één regel verder |
| Stop | Shift+F5 | stoppen |

Druk een aantal keer op **Continue** en volg `totaal` in het Variables-paneel.

**De vraag:** wat gebeurt er met `totaal` op het moment dat het programma van Ali naar
Bo overgaat? Noteer als commentaar wat je verwachtte, en wat er echt gebeurde.

## Stap 5: Repareer

Nu je gezien hebt wat er misgaat, is de reparatie één verplaatsing. Voer uit en vergelijk
met de tabel bovenaan.

## Stap 6, Ook `alles_minstens_tien`

Er is een tweede variabele met exact hetzelfde probleem. Welke, en waarom valt die minder op?

> Tip: verwissel Bo en Cem van plaats in de dictionary en voer opnieuw uit. Wat gebeurt er
> nu met Cem?

---

## Achteraf

Deze fout heb je al eerder gezien: `fout_1_som.py` uit les 4 en `fout_2_tellen.py` uit les 5.
Telkens hetzelfde patroon, een accumulator die op de verkeerde plaats staat.

Alleen: in les 4 en 5 zag je het door de code te lezen. Nu zag je het **gebeuren**.
