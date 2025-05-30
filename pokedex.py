import requests
import climage

# Unfinished, but search by name and adding pokemon to favorite list works so far. Need to work on organiazation and other features.


def main():
    # Empty list for favorite pokemons
    favorites_list = []

    quit_pokedex = False

    while quit_pokedex != True:
        print(
            "\n--------------------------------------------------------------------------------------------"
        )
        # ASCII art below from https://patorjk.com/software/taag/#p=display&h=0&v=2&f=ANSI%20Shadow&t=main%20menu
        print("██████╗  ██████╗ ██╗  ██╗███████╗██████╗ ███████╗██╗  ██╗")
        print("██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝")
        print("██████╔╝██║   ██║█████╔╝ █████╗  ██║  ██║█████╗   ╚███╔╝ ")
        print("██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║  ██║██╔══╝   ██╔██╗ ")
        print("██║     ╚██████╔╝██║  ██╗███████╗██████╔╝███████╗██╔╝ ██╗")
        print("╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝")

        print(
            """
            ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
            ████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
            ██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
            ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
            ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝"""
        )
        # print("\nPokedex" + "\nMain Menu")
        print(
            "--------------------------------------------------------------------------------------------"
        )
        choice = input(
            "\nPlease input a key below:\n\n"
            + "N: Search by name\n"
            + "P: Filter by parameters\n"
            + "F: Display favorite Pokemons\n"
            + "Q: Quit\n\n"
            + "Choice: "
        ).upper()

        if choice == "Q":
            print("Closing down...")
            quit_pokedex = True

        elif choice == "N":
            print("\nPokedex" + "\nSearch by Name")
            pokemon_name = input("\nEnter a pokemon name:").lower()

            pokemon_info = get_pokemon_info_by_name(pokemon_name)
            if pokemon_info:
                display_pokemon_info(pokemon_info)

            # Requesting if the user would like to add the searched pokemon to a favorites list.
            favorite_this_pokemon = input(
                "Would you like to add this pokemon to your favorites list? (Y/N): "
            ).upper()
            if favorite_this_pokemon == "Y":
                if pokemon_name in favorites_list:
                    print(
                        "The Pokemon",
                        pokemon_name,
                        "is already in your favorites list."
                    )
                    print("Sending you back to the main menu...")
                else:
                    favorites_list.append(pokemon_name)
                    print("Added", pokemon_name.capitalize(), "to your favorites list!")

                print("Updating your favorites list...")
                print("\nFavorite Pokemons: ")
                for i in range(len(favorites_list)):
                    print(i + 1, ".", favorites_list[i].capitalize())

            elif favorite_this_pokemon == "N":
                print("Sending you back to the main menu...")
            else:
                print("\nInvalid option. Please enter a different key...")

        elif choice == "P":
            print("\nSorry, this has not yet been implemented...")

        elif choice == "F":
            if len(favorites_list) == 0:
                print("\nYour favorites list is empty...")

            else:
                print("\nFavorite Pokemons: ")
                for i in range(len(favorites_list)):
                    print(i + 1, ".", favorites_list[i].capitalize())

                stop_removing = False
                while stop_removing != True:
                    remove_pokemon_from_fav = input(
                        "Would you like to remove pokemons from your favorites list? (Y/N): "
                    ).upper()

                    if remove_pokemon_from_fav == "Y":
                        for i in range(len(favorites_list)):
                            print(i + 1, ".", favorites_list[i].capitalize())

                        remove_num = input(
                            "If you would like to remove a pokemon, please type the pokemon's assigned number to remove them from the favorites list: "
                        )

                        remove_num = int(remove_num)

                        favorites_list.pop(remove_num - 1)

                        print("\nUpdating your favorites list...")

                        if len(favorites_list) == 0:
                            print("\nYour favorites list is empty...")
                            stop_removing = True

                        else:
                            print("\nFavorite Pokemons: ")
                            for i in range(len(favorites_list)):
                                print(i + 1, ".", favorites_list[i].capitalize())

                    elif remove_pokemon_from_fav == "N":
                        stop_removing = True

                    else:
                        print("\nInvalid option. Please enter a different key...")

                print("Sending you back to the main menu...")

        else:
            print("\nInvalid option. Please enter a different key...")


# def continue_on():
#    option = input("Enter 'c' to continue")
#    option.lower()
#    while option == "c":
#        continue


def get_pokemon_info_by_name(pokemon_name):
    # Make a request to the PokeAPI to get information about the specified Pokémon
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name)
    response = requests.get(url)

    if response.status_code != 200:
        print("\nError: Could not retrieve data. Please check the Pokémon name or try again later.")
        return None

    data = response.json()

    name = data["name"].capitalize()
    id = data["id"]
    types = [t["type"]["name"].capitalize() for t in data["types"]]
    abilities = [a["ability"]["name"].capitalize() for a in data["abilities"]]

    # Fix the three move items below, it is listing too many moves and should only filter for pokemon gold and silver.
    # moves = [m["move"]["name"].capitalize() for m in data["moves"]]
    sprite_url = data["sprites"]["front_default"]
    # print(sprite_url)

    stats = {s["stat"]["name"].capitalize(): s["base_stat"] for s in data["stats"]}
    return {
        "name": name,
        "id": id,
        "types": types,
        "abilities": abilities,
        # "moves": moves,
        "sprites": sprite_url,
        "stats": stats,
    }


def display_pokemon_info(pokemon_info):
    if pokemon_info is not None:
        print("\nHere is your requested Pokemon below...")
        print("\n")

        output_sprite_image(pokemon_info["sprites"])
        print("Name: {}".format(pokemon_info["name"]))
        print("ID: {}".format(pokemon_info["id"]))
        print("Types: {}".format(", ".join(pokemon_info["types"])))
        print("Abilities: {}".format(", ".join(pokemon_info["abilities"])))
        # print("Moves: {}".format(", ".join(pokemon_info["moves"])))
        print("Stats:")
        for stat, value in pokemon_info["stats"].items():
            print("  {}: {}".format(stat, value))
    # print(pokemon_info)

def output_sprite_image(sprite_url):
    url = sprite_url
    response = requests.get(url)

    with open("pokemon.png", "wb") as f:
        f.write(response.content)

    output = climage.convert(
        "pokemon.png",
        is_unicode=False,
        is_truecolor=False,
        is_256color=True,
        is_16color=False,
        is_8color=False,
        width=60,
        palette="default",
    )
    print(output)


if __name__ == "__main__":
    main()
