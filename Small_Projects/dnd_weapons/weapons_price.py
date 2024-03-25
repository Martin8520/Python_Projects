import csv
import os
import sys


def read_weapons_from_csv(filename):
    weapons = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            weapon_name = ','.join(row[:-1]).strip()
            price = int(row[-1])
            weapons[weapon_name.lower()] = price
    return weapons


def main():
    exe_dir = os.path.dirname(sys.executable)
    csv_file = os.path.join(exe_dir, r'C:\Users\marti\PycharmProjects\self_prep\Small_Projects\dnd_weapons\weapons.csv')

    if not os.path.exists(csv_file):
        print("Error: weapons.csv file not found.")
        return

    weapons = read_weapons_from_csv(csv_file)

    print("List of weapons:")
    for weapon in weapons:
        print(weapon.capitalize())

    while True:
        user_input = input("Enter a weapon name (type 'exit' to quit): ").lower()
        if user_input == 'exit':
            print("Exiting...")
            break
        elif user_input in weapons:
            print(f"The price of {user_input.capitalize()} is {weapons[user_input]} gold pieces.")
        else:
            print("Weapon not found.")


if __name__ == "__main__":
    main()
