import requests, json

def getPokemonInfo(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if not response.json():
        print(f"Failed to retreive data for {pokemon_name}.")
        return None
    else:
        data = response.json()
        pokemon_info = {
            "Name": data["name"].title(),
            "Ability": data["abilities"][0]["ability"]["name"],
            "Base Experience": data["base_experience"],
            "Sprite URL": data["sprites"]["front_shiny"],
            "Attack Base Stat": data["stats"][1]["base_stat"],
            "HP Base Stat": data["stats"][0]["base_stat"],
            "Defense Base Stat": data["stats"][2]["base_stat"]
        }
        return pokemon_info


pokemon_names = [
    "Pikachu", "Bulbasaur", "Ivysaur", "Charmander", "Jigglypuff",
    "Caterpie", "Eevee", "Snorlax", "Gengar", "Dragonite",
    "Machop", "Metapod", "Psyduck", "Kangaskhan", "Beedrill",
    "Vaporeon", "Flareon", "Jolteon", "Lapras", "Gyarados"
]

pokemon_data = []

for pokemon in pokemon_names:
    pokemon_info = getPokemonInfo(pokemon)
    if pokemon_info:
        pokemon_data.append(pokemon_info)

counter = 1
for pokemon in pokemon_data:
    print(f"Pokemon {counter}")
    for key, value in pokemon.items():
        print(f"{key}: {value}")
    counter += 1
    print()