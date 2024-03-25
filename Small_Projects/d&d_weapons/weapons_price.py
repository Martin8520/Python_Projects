import csv


def read_weapons_from_csv(filename):
    weapons = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            weapon_name = ','.join(row[:-1]).strip()
            price = int(row[-1])
            weapons[weapon_name.lower()] = price
    return weapons


def main():
    weapons = read_weapons_from_csv('weapons.csv')

    print("List of weapons:")
    for weapon in weapons:
        print(weapon.capitalize())

    user_input = input("Enter a weapon name: ").lower()
    if user_input in weapons:
        print(f"The price of {user_input.capitalize()} is {weapons[user_input]} gold pieces.")
    else:
        print("Weapon not found.")


if __name__ == "__main__":
    main()
