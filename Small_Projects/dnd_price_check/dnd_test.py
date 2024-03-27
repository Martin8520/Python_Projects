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
    global item_number
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
            print(f"{category_num}: {category_file[:-4].replace('_', ' ').title()}")
        print("0: Exit")
        user_choice = input("Enter the number of the category or '0' to quit: ")

        if user_choice == "0":
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

        print(f"\nList of {user_category[:-4].replace('_', ' ').title()}:")
        for index, item in enumerate(items, start=1):
            print(f"{index}: {item.title()} - {items[item]} gold pieces")

        while True:
            print("\nOptions:")
            print("1: Search for an item")
            print("2: Edit item price")
            print("3: Add a new item")
            print("4: Delete an item")
            print("0: Go back to main menu")
            option = input("Enter your choice: ")

            if option == "0":
                break
            elif option == "1":
                user_input = input("Enter an item name or its number to search or type 'back' to go back: ").lower()

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
                        print(f"The price of {found_items[0][0].title()} is {found_items[0][1]} gold pieces.Item Number: {item_number}")
                    else:
                        print("Found items:")
                        for found_item in found_items:
                            print(f"The price of {found_item[0].title()} is {found_item[1]} gold pieces.Item Number: {item_number}")
                else:
                    found_in_other_categories = []
                    for category_num, category_file in categories.items():
                        if category_file != user_category:
                            csv_file = os.path.join(script_dir, category_file)
                            if not os.path.exists(csv_file):
                                print(f"Error: {category_file} file not found.")
                                continue
                            other_category_items = read_items_from_csv(csv_file)
                            for item_name, price in other_category_items.items():
                                if user_input in item_name:
                                    found_in_other_categories.append((category_num, category_file))
                                    break
                    if found_in_other_categories:
                        print("No items found in the selected category. However, found in other categories:")
                        for found_category_num, found_category_file in found_in_other_categories:
                            print(f"{found_category_num}: {found_category_file[:-4].replace('_', ' ').title()}")
                        print("b: Back to main menu")
                        user_choice = input("Enter the number of the category or 'b' to go back: ")

                        if user_choice == "b":
                            break
                        elif user_choice.isdigit() and int(user_choice) in categories:
                            user_category = categories[int(user_choice)]
                            csv_file = os.path.join(script_dir, user_category)
                            if not os.path.exists(csv_file):
                                print(f"Error: {user_category} file not found.")
                                continue
                            items = read_items_from_csv(csv_file)

                            print(f"\nList of {user_category[:-4].replace('_', ' ').title()}:")
                            for index, item in enumerate(items, start=1):
                                print(f"{index}: {item.title()} - {items[item]} gold pieces")
                            continue
                        else:
                            print("Invalid choice. Returning to main menu.")
                    else:
                        print(f"No items found matching '{user_input}' in any category.")
            elif option == "2":
                item_to_edit = input("Enter the name or number of the item you want to edit: ").lower()
                if item_to_edit.isdigit() and 1 <= int(item_to_edit) <= len(items):
                    item_to_edit = list(items.keys())[int(item_to_edit) - 1]
                if item_to_edit in items:
                    original_price = items[item_to_edit]
                    new_price = input("Enter the new price for the item: ")
                    items[item_to_edit] = int(new_price)
                    print(f"Item '{item_to_edit.title()}'.Item Number: {item_number} (Price: {original_price}) updated to Price: {new_price}.")
                else:
                    print("Item not found.")
            elif option == "3":
                new_item_name = input("Enter the name of the new item: ").strip().lower()
                new_item_price = input("Enter the price of the new item: ")
                items[new_item_name] = int(new_item_price)
                item_number = len(items)
                print(f"New item '{new_item_name.title()}' added with price: {new_item_price} (Item Number: {item_number}).")
            elif option == "4":
                item_to_delete = input("Enter the name or number of the item you want to delete: ").lower()
                if item_to_delete.isdigit() and 1 <= int(item_to_delete) <= len(items):
                    item_to_delete = list(items.keys())[int(item_to_delete) - 1]
                if item_to_delete in items:
                    deleted_price = items[item_to_delete]
                    del items[item_to_delete]
                    print(f"Item '{item_to_delete.title()}'.Item Number: {item_number} (Price: {deleted_price}) deleted.")
                else:
                    print("Item not found.")

            with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Item', 'Price'])
                for item_name, price in items.items():
                    writer.writerow([item_name.title(), price])


if __name__ == "__main__":
    main()
