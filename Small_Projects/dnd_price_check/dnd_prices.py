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
            user_choice = int(user_choice)
            if user_choice not in categories:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        user_category = categories[user_choice]
        csv_file = os.path.join(script_dir, user_category)

        if not os.path.exists(csv_file):
            print(f"Error: {user_category} file not found.")
            continue

        items = read_items_from_csv(csv_file)

        print(f"\nList of {user_category[:-4].replace('_', ' ').capitalize()}:")
        for index, item in enumerate(items, start=1):
            print(f"{index}: {item.capitalize()}")

        while True:  # Loop until a valid input is received
            user_input = input("\nEnter an item name or its number to search or type 'back' to go back: ").lower()

            if user_input == 'back':
                break

            found_items = []
            if user_input.isdigit() and 1 <= int(user_input) <= len(items):
                item_name = list(items.keys())[int(user_input) - 1]
                found_items.append((item_name, items[item_name]))
            else:
                for item_name, price in items.items():
                    if user_input in item_name:
                        found_items.append((item_name, price))

            if found_items:
                if len(found_items) == 1:
                    print(f"The price of {found_items[0][0].capitalize()} is {found_items[0][1]} gold pieces.")
                else:
                    print("Found items:")
                    for found_item in found_items:
                        print(f"The price of {found_item[0].capitalize()} is {found_item[1]} gold pieces.")
            else:
                # No items found in the chosen category, check other categories
                found_in_other_categories = []
                for category_num, category_file in categories.items():
                    if category_file != user_category:  # Avoid searching in the same category
                        csv_file = os.path.join(script_dir, category_file)
                        if not os.path.exists(csv_file):
                            print(f"Error: {category_file} file not found.")
                            continue
                        items = read_items_from_csv(csv_file)
                        for item_name, price in items.items():
                            if user_input in item_name:
                                found_in_other_categories.append((category_num, category_file))
                                break
                if found_in_other_categories:
                    print("No items found in the selected category. However, found in other categories:")
                    for found_category_num, found_category_file in found_in_other_categories:
                        print(f"{found_category_num}: {found_category_file[:-4].replace('_', ' ').capitalize()}")
                    print("b: Back to main menu")
                    user_choice = input("Enter the number of the category or 'b' to go back: ")

                    if user_choice == 'b':
                        break
                    elif user_choice.isdigit() and int(user_choice) in categories:
                        user_category = categories[int(user_choice)]
                        csv_file = os.path.join(script_dir, user_category)
                        if not os.path.exists(csv_file):
                            print(f"Error: {user_category} file not found.")
                            continue
                        items = read_items_from_csv(csv_file)

                        print(f"\nList of {user_category[:-4].replace('_', ' ').capitalize()}:")
                        for index, item in enumerate(items, start=1):
                            print(f"{index}: {item.capitalize()}")
                        continue
                    else:
                        print("Invalid choice. Returning to main menu.")
                else:
                    print(f"No items found matching '{user_input}' in any category.")


if __name__ == "__main__":
    main()
