import random


def roll_d20():
    return random.randint(9, 18)


class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.stats = {}

    def generate_stats(self):
        attributes = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }

        for attr in attributes:
            attributes[attr] = roll_d20()

        self.stats = attributes

    def display_info(self):
        print("Character Information:")
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print("Attributes:")
        for attr, value in self.stats.items():
            print(f"{attr}: {value}")


def create_character():
    print("D&D Character Creator")
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    char_class = input("Enter character class: ")

    character = Character(name, race, char_class)
    character.generate_stats()

    return character


def main():
    character = create_character()
    character.display_info()


main()
