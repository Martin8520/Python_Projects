import csv
import os


def read_items_from_csv(filename):
    items = {}
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            item_name = row[0].strip()
            price = int(row[1])
            items[item_name.lower()] = price
    return items


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    categories = {
        1: 'armors.csv',
        2: 'magical_items.csv',
        3: 'potions.csv',
        4: 'weapons.csv',
        5: 'misc.csv'
    }

    while True:
        print("\nCategories:")
        for category_num, category_file in categories.items():
            print(f"{category_num}: {category_file[:-4].replace('_', ' ').capitalize()}")
        print("0: Exit")
        user_choice = input("Enter the number of the category or '0' to quit: ")

        if user_choice == '0':
            print("Exiting...")
            break

        try:
            user_category = categories[int(user_choice)]
        except (ValueError, KeyError):
            print("Invalid choice. Please enter a valid number.")
            continue

        csv_file = os.path.join(script_dir, user_category)

        if not os.path.exists(csv_file):
            print(f"Error: {user_category} file not found.")
            continue

        items = read_items_from_csv(csv_file)

        print(f"\nList of {user_category[:-4].replace('_', ' ').capitalize()}:")
        for index, item in enumerate(items, start=1):
            print(f"{index}: {item.capitalize()}")

        user_input = input("\nEnter an item name or its number to search or type 'back' to go back: ").lower()

        if user_input == 'back':
            continue

        if user_input.isdigit() and 1 <= int(user_input) <= len(items):
            item_name = list(items.keys())[int(user_input) - 1]
            print(f"The price of {item_name.capitalize()} is {items[item_name]} gold pieces.")
        elif user_input in items:
            print(f"The price of {user_input.capitalize()} is {items[user_input]} gold pieces.")
        else:
            found_in_category = None
            for category_num, category_file in categories.items():
                if category_file != user_category:
                    items = read_items_from_csv(os.path.join(script_dir, category_file))
                    if user_input in items:
                        found_in_category = category_file[:-4].replace('_', ' ').capitalize()
                        break
            if found_in_category:
                print(f"{user_input.capitalize()} is not found in "
                      f"{user_category[:-4].replace('_', ' ').capitalize()}"
                      f", but it's in {found_in_category}.")
            else:
                print(f"{user_input.capitalize()} not found in any category.")


if __name__ == "__main__":
    main()
