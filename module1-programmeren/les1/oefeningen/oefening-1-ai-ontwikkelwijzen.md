# Oefening 1: Drie manieren om met AI te ontwikkelen

> Les 1 · ± 20 minuten · werk individueel, overleggen mag

Je hebt net je AI-assistent werkend. Er is niet één manier om hem te gebruiken. In deze
oefening probeer je drie verschillende manieren uit op dezelfde kleine opdracht, en voel je
het verschil.

## De opdracht

Maak een functie `hoogste(getallen)` die het hoogste getal uit een lijst teruggeeft.
Gebruik geen `max()` van Python. Schrijf de logica zelf.

## Manier 1: Copy-paste vanuit een chat-LLM (ChatGPT, Claude, Gemini)

1. Open een chatvenster van je AI-assistent (in de browser of app, niet in VS Code).
2. Typ je vraag: *"Schrijf een Python-functie `hoogste(getallen)` die het hoogste getal uit
   een lijst vindt, zonder `max()` te gebruiken."*
3. Kopieer de code die je krijgt en plak ze in `oefening1.py`.
4. Voeg onderaan een test toe en draai:

```python
print(hoogste([3, 17, 8, 2]))
```

Werkt het? Noteer het antwoord.

> **Kenmerk:** jij stelt de vraag, jij kopieert de code, jij plakt ze in je editor. De AI
> schrijft niet in jouw bestand. Jij bent de brug.

## Manier 2: AI-autocomplete in je editor (Copilot)

1. Maak een nieuw bestand `oefening1b.py`. Typ bovenaan deze regel:

```python
# functie die het hoogste getal uit een lijst teruggeeft, zonder max()
```

2. Wacht tot er grijze tekst verschijnt en aanvaard met **Tab**. Komt er niets, druk dan
   op **Ctrl+Enter** (Copilot Chat) en stel je vraag daar.
3. Voeg een testregel toe en draai.

> **Kenmerk:** de AI vult aan terwijl jij typt. Je hoeft niet te switchen naar een
> chatvenster. Het voelt alsof de editor met je meedenkt, maar jij behoudt de controle:
> elke regel passeert onder jouw vingers.

## Manier 3: Een agentic tool (Claude Code, Codex CLI, GitHub Copilot CLI)

1. Open een terminal in je projectmap.
2. Start je tool (bv. `claude` of `codex` of `gh copilot`).
3. Vraag: *"Maak een bestand oefening1c.py met een functie hoogste(getallen) die het hoogste
   getal uit een lijst vindt zonder max(). Voeg ook een test toe."*
4. De tool maakt het bestand zelf aan, schrijft de code erin, en voegt mogelijk ook de test
   toe. Jij hoeft niet te kopiëren.
5. Open het bestand in VS Code en draai het.

> Niet iedereen heeft zo'n tool geïnstalleerd. Heb je er geen, sla deze stap dan over en
> lees hieronder mee. Komt later in de opleiding terug.

> **Kenmerk:** de tool doet dingen zelf: bestanden aanmaken, code schrijven, soms testen
> draaien. Jij stuurt met je vraag en keurt het resultaat goed. Krachtig, maar je moet
> begrijpen wat er gebeurt.

## Vergelijk de drie manieren

Vul deze tabel in:

| | Chat-LLM (copy-paste) | Editor-autocomplete | Agentic tool |
|---|---|---|---|
| Waar typ je je vraag? | | | |
| Wie plaatst de code in je bestand? | | | |
| Zie je wat de AI doet stap voor stap? | | | |
| Hoeveel controle heb jij? | | | |
| Welke aanpak voelt meest comfortabel? | | | |

Er is geen "beste" manier. Elk project en elke ontwikkelaar heeft een voorkeur. Veel
ontwikkelaars wisselen de hele dag tussen deze manieren.

## Een terzijde: AI verzint soms dingen

Een assistent kan met evenveel overtuiging `lijst.add()` voorstellen als het echte
`lijst.append()`. Die functie bestaat niet, maar de code ziet eruit alsof ze zou moeten
werken. Gelukkig crasht ze meteen zodra je ze uitvoert, dus je merkt het direct.

Erger is code die draait en stilletjes het verkeerde antwoord geeft. Daarom geldt altijd:
**voer uit, reken na, en leg elke regel uit in je eigen woorden.** Code die je niet kan
uitleggen, lever je niet in.

---

## Wat je moet kunnen tonen op het einde

- [ ] `oefening1.py` bestaat en draait (manier 1)
- [ ] Je hebt minstens twee van de drie manieren geprobeerd
- [ ] De vergelijkingstabel is ingevuld

## Waar dit naartoe gaat

De drie manieren die je vandaag probeerde, komen de hele opleiding terug. Vanaf les 2 leer
je bovendien systematisch nadenken over randgevallen (zoals een lege lijst) **voordat** je
code schrijft, in plaats van ze achteraf te ontdekken.
