# Oefening 4: Twee Pokémon, één gevecht

> **Concept** · ± 60–75 minuten · individueel of per twee · maak een bestand `pokemon_gevecht.py`

Haal twee Pokémon op via de PokéAPI, maak er objecten van en laat ze om de beurt aanvallen.
Je schrijft **één klasse `Pokemon`** en maakt daarmee **twee objecten**. Een aparte functie
`vecht(pokemon_1, pokemon_2)` organiseert het gevecht.

**Je oefent:** JSON uitlezen, functies, een klasse met attributen en methoden, en objecten als
argument aan een functie doorgeven. Je hebt internet nodig om de gegevens op te halen.

## A: Haal twee Pokémon op

Gebruik deze adressen om eerst in je browser te bekijken welke gegevens je terugkrijgt:

- https://pokeapi.co/api/v2/pokemon/pikachu
- https://pokeapi.co/api/v2/pokemon/bulbasaur

Schrijf een functie `haal_pokemon_data(naam)` die de gegevens van één Pokémon ophaalt en de
JSON als dictionary teruggeeft. Roep de functie twee keer aan. Gebruik voorlopig vaste namen
in je code; invoer via `input()` mag later.

Met de ingebouwde Python-modules kan je zo een verzoek uitvoeren; je hoeft niets te installeren:

```python
import json
from urllib.request import urlopen

naam = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{naam}"

with urlopen(url, timeout=10) as antwoord:
    data = json.load(antwoord)

print(data["name"])
```

Verwerk dit voorbeeld in je functie. Maak de naam eerst geschikt met `.strip().lower()`.

Zoek in de dictionary:

- `name`: de naam;
- in `stats`: de statistiek `hp` (levenspunten);
- in `stats`: de statistiek `attack` (aanvalskracht).

Elk element van `stats` bevat een `base_stat` en een `stat["name"]`. Loop door de lijst en
zoek op die naam, zodat je niet afhankelijk bent van de volgorde.

**Controle:** voor Pikachu vind je 35 HP en 55 aanval; voor Bulbasaur 45 HP en 49 aanval.

## B: Maak de klasse `Pokemon`

Schrijf een klasse met een `__init__(self, naam, hp, aanval)` die deze drie waarden als
attributen bewaart. De dictionary uit de API gebruik je om het object te maken.

Voeg twee methoden toe:

| Methode | Gedrag |
|---|---|
| `is_bewusteloos()` | Geeft `True` terug als `hp` gelijk is aan 0, anders `False`. |
| `ontvang_schade(schade)` | Vermindert de eigen HP met de schade. HP mag nooit onder 0 zakken. |

Maak nu twee objecten met de opgehaalde gegevens en print van elk de naam, HP en aanval.

**Controle:** laat één object 10 schade ontvangen. Alleen de HP van dat object verandert.
Controleer ook dat 1000 schade de HP op 0 zet. Maak daarna verse objecten voor het gevecht.

> De methode verandert het eigen object via `self.hp`. De twee Pokémon hebben elk hun eigen
> toestand, ook al komen ze uit dezelfde klasse.

## C: Schrijf de functie `vecht(pokemon_1, pokemon_2)`

Deze functie staat **buiten de klasse** en krijgt de twee objecten als argumenten. De functie
regelt de beurten; de methoden regelen wat er met één Pokémon gebeurt.

Gebruik voor deze oefening vereenvoudigde spelregels:

1. Beide Pokémon starten met hun volledige HP. De eerste parameter valt als eerste aan.
2. De schade is `max(1, aanvaller.aanval // 5)`. Zo duurt een gevecht meerdere beurten.
3. Geef die schade door aan `ontvang_schade()` van de tegenstander.
4. Print wie aanvalt, hoeveel schade die doet en hoeveel HP de tegenstander overhoudt.
5. Controleer **meteen na elke aanval** of de tegenstander bewusteloos is. Dan stopt het
   gevecht: een bewusteloze Pokémon mag niet meer terugslaan.
6. Als beide Pokémon nog kunnen vechten, wisselen de aanvaller en de tegenstander van rol.
7. Geef het **winnende object** terug met `return`. Toon de winnaar buiten de functie.

Gebruik een `while`-lus. Je mag aannemen dat beide objecten bij de start meer dan 0 HP en een
positieve aanvalskracht hebben. Types, verdediging, snelheid en toeval spelen nog niet mee.

Zo wil je de functie uiteindelijk kunnen gebruiken:

```python
# pikachu en bulbasaur zijn hier al Pokemon-objecten, gemaakt met API-gegevens.
winnaar = vecht(pikachu, bulbasaur)
print(f"Winnaar: {winnaar.naam}!")
```

> De functie ontvangt de objecten zelf. Als ze een methode aanroept die HP verandert, zie je
> die verandering na het gevecht ook via `pikachu.hp` of `bulbasaur.hp`.

## D: Controleer het volledige gevecht

Met Pikachu als eerste aanvaller moet het begin er zo uitzien:

```text
pikachu valt bulbasaur aan: 11 schade. bulbasaur heeft nog 34 HP.
bulbasaur valt pikachu aan: 9 schade. pikachu heeft nog 26 HP.
```

Na vier aanvallen van elke Pokémon heeft Pikachu 0 HP en Bulbasaur 1 HP. De winnaar is dus
**Bulbasaur**. De precieze opmaak van je uitvoer mag verschillen.

Controleer daarna ook deze situaties:

- Laat een Pokémon met 1 HP starten. Stopt het gevecht meteen na de beslissende aanval?
- Gebruik voor een controle een aanvalskracht van 1. Blijft de schade minstens 1?
- Draai opnieuw met verse objecten en wissel de startvolgorde. Krijg je met deze twee Pokémon
  dezelfde winnaar? Verklaar je resultaat aan de hand van de HP en schade.

> Na een gevecht zijn de objecten veranderd. Haal voor een nieuw gevecht de gegevens opnieuw
> op en maak nieuwe objecten, of voeg als uitbreiding een methode voor herstellen toe.

## Klaar om te bespreken

- [ ] Ik haal twee Pokémon via een functie op en zoek hun statistieken op naam.
- [ ] Ik gebruik één klasse en twee afzonderlijke objecten.
- [ ] Mijn methoden gebruiken `self`; `is_bewusteloos()` geeft een boolean terug.
- [ ] Mijn losse gevechtsfunctie ontvangt twee objecten en geeft het winnende object terug.
- [ ] HP wordt nooit negatief en een bewusteloze Pokémon slaat niet terug.

## Klaar en tijd over?

- Vraag de twee namen met `input()` en handel een onbekende naam (HTTP 404) en een
  verbindingsprobleem netjes af. Laat het gevecht alleen starten als beide verzoeken lukken.
- Bewaar de oorspronkelijke HP in `max_hp` en schrijf een methode `herstel()` voor een revanche.
- Geef het gevecht willekeurige schade. Leg vooraf vast tussen welke grenzen die mag liggen.
- Verplaats de klasse naar `pokemon.py` en importeer ze in je hoofdprogramma.
