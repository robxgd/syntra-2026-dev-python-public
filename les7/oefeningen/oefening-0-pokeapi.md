# Oefening 0: Haal je eigen Pokémon op

> ± 10 minuten · individueel · tijdens het openingsblok

Je maakt een API-call naar [PokéAPI](https://pokeapi.co/), zet de JSON om naar een
Python-dictionary en toont enkele gegevens. Je hebt internet nodig, geen account of API-sleutel.

## Stap 1: Klaarzetten

Installeer in de terminal bij je bestaande module-venv:

```bash
uv pip install requests
```

Gebruik in VS Code dezelfde Python-interpreter als bij de vorige lessen. Bij
`ModuleNotFoundError: No module named 'requests'`: controleer of je het pakket in die
omgeving geïnstalleerd hebt. Maak een bestand `mijn_pokemon.py`.

## Stap 2: Ophalen

Open eerst <https://pokeapi.co/api/v2/pokemon/pikachu/> in je browser. Zoek `name`,
`height`, `weight` en `types`. Haal dezelfde gegevens daarna op met Python:

```python
import requests

naam = input("Welke Pokémon? ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{naam}/"
response = requests.get(url, timeout=10)
print(f"Statuscode: {response.status_code}")
response.raise_for_status()
pokemon = response.json()
```

Gebruik een Engelse naam zoals `pikachu`, `bulbasaur` of `charmander`. Je kan ook een
nummer invoeren, bijvoorbeeld `25`. Geef voor deze eerste versie altijd een naam of nummer in.

## Stap 3: Toon een Pokémon-kaartje

Breid je code uit zodat je dit toont:

- De naam, met een hoofdletter.
- De lengte in meter: `height` is in decimeter, dus deel door 10.
- Het gewicht in kilogram: `weight` is in hectogram, dus deel door 10.
- Alle types, met een `for`-lus over `pokemon["types"]`. Elke entry bevat een dictionary
  `type`, waarin je `name` vindt.

Voor Pikachu verwacht je:

```text
Statuscode: 200
Naam: Pikachu
Lengte: 0.4 m
Gewicht: 6.0 kg
Types:
- electric
```

## Stap 4: Controleer en breek het

| Invoer | Controle |
|---|---|
| `pikachu` | Kloppen naam, lengte en gewicht met de browser? |
| `bulbasaur` | Zie je beide types, `grass` en `poison`? |
| ` PIKACHU ` | Waarom werken de spaties en hoofdletters toch? |
| `bestaatniet` | Welke statuscode verschijnt? Welke regel veroorzaakt de HTTPError? |

Laat de fout bij de onbekende naam voorlopig zichtbaar. We leren zo meteen hoe je die
traceback leest en gericht opvangt. Vraag de gegevens één keer op en hergebruik de dictionary
bij het aanpassen van je uitvoer.

## Kan je het uitleggen?

1. Wat is het verschil tussen `response` en `pokemon`?
2. Waarom staat `raise_for_status()` vóór `json()`?
3. Welke delen van `pokemon["types"]` zijn lijsten en welke zijn dictionaries?

**Klaar?** Zet het ophalen in een functie `haal_pokemon_op(naam)` die de dictionary
teruggeeft. Toon het kaartje buiten die functie.

Bronnen: [PokéAPI: Pokémon en eenheden](https://pokeapi.co/docs/v2#pokemon) en
[Requests: quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/).
