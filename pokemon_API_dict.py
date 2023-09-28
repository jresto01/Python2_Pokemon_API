import requests, json

def getPokemonInfo():
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)

    pokemon_data = []

    if not response.json()["results"]:
        print(f"Failed to retreive data.")
        return None
    else:
        data = response.json()["results"]

        for x in range(20):
            pokemon_url = data[x]["url"]
            pokemon_details = requests.get(pokemon_url).json()

            pokemon_info = {
                "Name": data[x]["name"].title(),
                "Ability": pokemon_details["abilities"][0]["ability"]["name"],
                "Base Experience": pokemon_details["base_experience"],
                "Sprite URL": pokemon_details["sprites"]["front_shiny"],
                "Attack Base Stat": pokemon_details["stats"][1]["base_stat"],
                "HP Base Stat": pokemon_details["stats"][0]["base_stat"],
                "Defense Base Stat": pokemon_details["stats"][2]["base_stat"]
            }

            pokemon_data.append(pokemon_info)

    return pokemon_data

        


pokemon_list = getPokemonInfo()
for pokemon in pokemon_list:
    print(pokemon)


