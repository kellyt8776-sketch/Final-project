#Terrill kelly
#12/12/25
#finalProject_KellyTerrill.py

import random



def create_character():
    name = input("Enter your character's name: ")
    Racing_Brand = input("Choose a Racing class (BMW, Ford, Nissan): ")
    ability = input("Choose a ability (Superspeed, telportation, SpeedDemon): ")
    Horsepower = input("Choose your Horsepower (100, 200, 300, 400, 500): ")
    character = {
        "name": name,
        "ability": ability,
        "Racing_class": Racing_Brand,
        "Horsepower": Horsepower
    }
    print(f"Character {name} created successfully 😀")
    return character


def race(character):
    print("🏁 🏁 🏁 The race is starting! 🏁 🏁 🏁")
    for char in range(3):
        print(f"{character['name']} is racing with {character['Racing_class']} and has {character['Horsepower']} HP!")


def Rival(Rival, defender):
    print(f"{Rival['name']} is racing against {defender['name']}!")

    Rival_power = random.randint(1, int(Rival['Horsepower']))
    defender_power = random.randint(1, int(defender['Horsepower']))

    print(f"{Rival['name']} power: {Rival_power}")
    print(f"{defender['name']} power: {defender_power}")

    if Rival_power > defender_power:
        print(f"{Rival['name']} wins the race! 🏆")
    elif defender_power > Rival_power:
        print(f"{defender['name']} wins the race! 🏆")
    else:
        print("It's a tie! ")


# ---------------- MAIN PROGRAM ----------------

print("🏎️ WELCOME TO THE RACING GAME 🏎️")

player = create_character()

print("Create your rival!")
computer = create_character()

race(player)
race(computer)

Rival(player, computer)
