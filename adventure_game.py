# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_pause("Rumor has it that a terrifying creature is somewhere"
                " around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def fight(enemy, weapon):
    no_fight_or_fight_choice = valid_input("Would you like to (1) fight or"
                                           " (2) run away into the field?",
                                           "1", "2")
    if "1" in no_fight_or_fight_choice:
        if weapon in ["small nife", "old sword", "tiny dagger"]:
            print_pause("You have been defeated!")
            no_restart_or_restart_again()
        elif weapon in ["shotgun", "handgun", "machine gun"]:
            print_pause("You have won the game")
            print_pause("Congradulations!!!")
    if "2" in no_fight_or_fight_choice:
        field()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens")
    enemy = random.choice(["pirate", "trol", "dragon"])
    print_pause(f"Ooooh! This is the {enemy} coming to attack you")
    weapon = random.choice(["small nife", "old sword", "tiny dagger",
                            "shotgun", "handgun", "machine gun"])
    print_pause(f"You found a {weapon} in the nearby to defend youeself")
    fight(enemy, weapon)


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("you are now at the entrance of the cave")
    enemy = random.choice(["monster", "witch", "wicked fairy"])
    print_pause(f"Ooooh! This is the {enemy} coming to attack you")
    weapon = random.choice(["small nife", "old sword", "tiny dagger",
                            "shotgun", "handgun", "machine gun"])
    print_pause(f"You found a {weapon} in the nearby to defend yourself")
    fight(enemy, weapon)


def field():
    print_pause("You run back into the field")
    print_pause("You are now into the field. Luckily, you"
                " don't seem to have been followed.\n\n")
    no_restart_or_restart_again()


def house_cave_choice():
    response = valid_input("\nEnter 1 to knock on the door of the house."
                           "\nEnter 2 to peer into the cave. \nWhat would"
                           " you like to do?"
                           "\n(Please enter 1 or 2).", "1", "2")
    if "1" in response:
        house()
    elif "2" in response:
        cave()


def no_restart_or_restart_again():
    response = valid_input("Would you like to play again? (y/n)", "y", "n")
    if "n" in response:
        print_pause("Thanks for playing! See you next time.")
    elif "y" in response:
        print_pause("Excellent! Restarting the game ...")
        adventure_game()


def adventure_game():
    intro()
    house_cave_choice()


adventure_game()
