"""DEMO 0: data ophalen van een URL met PokéAPI.

Vooraf in de bestaande module-venv: uv pip install requests
Blok 1 tot en met 3 samen uitvoeren. Blok 4 later bij try/except tonen.
Documentatie: https://pokeapi.co/docs/v2#pokemon
"""

import requests


# ---------------------------------------------------------------------------
# 1. Een GET-request: vraag gegevens op bij een API
# ---------------------------------------------------------------------------

url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
response = requests.get(url, timeout=10)
print(f"Statuscode: {response.status_code}")
response.raise_for_status()

# 200: gelukt. Een onbekende naam geeft 404.
# raise_for_status() maakt van een HTTP-fout een exception.
# timeout=10 begrenst het wachten bij netwerkstilte, niet de totale downloadtijd.


# ---------------------------------------------------------------------------
# 2. JSON wordt een Python-dictionary met lijsten en andere dictionaries
# ---------------------------------------------------------------------------

pokemon = response.json()
print(type(pokemon))  # <class 'dict'>
print(pokemon["name"])
print(pokemon["height"])


# ---------------------------------------------------------------------------
# 3. Bekende Python-code op echte gegevens
# ---------------------------------------------------------------------------

print(f"Naam: {pokemon['name'].capitalize()}")
print(f"Lengte: {pokemon['height'] / 10:.1f} m")  # API: decimeter
print(f"Gewicht: {pokemon['weight'] / 10:.1f} kg")  # API: hectogram
print("Types:")
for type_info in pokemon["types"]:
    print(f"- {type_info['type']['name']}")

# Hergebruik pokemon als je alleen de uitvoer aanpast: geen nieuwe call nodig.
# Probeer daarna in de URL: bulbasaur of 25 (het nummer van Pikachu).
# Probeer ten slotte: bestaatniet. Lees de HTTPError van onder naar boven.


# ---------------------------------------------------------------------------
# 4. Later bij try/except: fouten buiten je eigen programma opvangen
#
# Haal het commentaar weg en voer dit blok apart uit.
# De uitvoer staat in else: die draait alleen als de aanvraag gelukt is.
# ---------------------------------------------------------------------------

# try:
#     response = requests.get(
#         "https://pokeapi.co/api/v2/pokemon/bestaatniet/", timeout=10
#     )
#     response.raise_for_status()
# except requests.exceptions.HTTPError:
#     if response.status_code == 404:
#         print("Die Pokémon bestaat niet. Controleer de naam.")
#     else:
#         print(f"De API meldt een HTTP-fout: {response.status_code}.")
# except requests.exceptions.Timeout:
#     print("De API reageert te traag. Probeer later opnieuw.")
# except requests.exceptions.ConnectionError:
#     print("Geen verbinding met PokéAPI. Controleer je internet.")
# else:
#     pokemon = response.json()
#     print(pokemon["name"])

# Een 404 is een HTTP-response. Geen internet geeft geen HTTP-statuscode.
# Een tikfout zoals pokmon blijft zichtbaar als NameError.
