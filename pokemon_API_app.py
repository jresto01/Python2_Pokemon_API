import requests, json

def getPokemonInfo(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
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
        for key, value in pokemon_info.items():
            print(f"{key}: {value}")
    else:
        print(f"\nFailed to retrieve data for {pokemon_name.title()}.")
        if response.status_code == 404:
            print(f"{pokemon_name.title()} does not exist.")
            



def run(): 
    while True:
        print("\nEnter 'quit' to exit at any time.")
        pokemon_name = input("Please enter Pokemon name: ")

        if pokemon_name.lower() == "quit":
            break
        else:
            getPokemonInfo(pokemon_name)

run()
