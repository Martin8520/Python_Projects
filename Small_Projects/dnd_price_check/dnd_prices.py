import csv
import os


def read_items_from_csv(filename):
    items = {}
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            item_name = row[0].strip().lower()
            price = int(row[1])
            items[item_name] = price
    return items


def write_items_to_csv(filename, items):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Item', 'Price'])
        for item, price in items.items():
            writer.writerow([item, price])


def display_items_with_numbers(items):
    for index, item in enumerate(items, start=1):
        print(f"{index}: {item.title()} - {items[item]} gold pieces")


def delete_item_from_csv(filename, item_name):
    updated_items = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        updated_items.append(header)
        for row in reader:
            if row[0].strip().lower() != item_name:
                updated_items.append(row)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(updated_items)


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
        display_items_with_numbers(items)

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
                    item_idx = int(user_input)
                    item_name = list(items.keys())[item_idx - 1]
                    found_items.append((item_name, items[item_name]))
                else:
                    for idx, (item_name, price) in enumerate(items.items(), start=1):
                        if user_input in item_name:
                            found_items.append((item_name, price))

                if found_items:
                    if len(found_items) == 1:
                        for index, item in enumerate(items, start=1):
                            if item == found_items[0][0]:
                                print(f"Found item: {index} - {found_items[0][0]}: {found_items[0][1]} gold pieces.")
                                break
                    else:
                        for idx, found_item in enumerate(found_items, start=1):
                            for index, item in enumerate(items, start=1):
                                if item == found_item[0]:
                                    print(f"Found item {index}: {found_item[0]} - {found_item[1]} gold pieces.")
                                    break
                else:
                    print("Item not found.")
            elif option == "2":
                item_to_edit = input("Enter the name or number of the item you want to edit: ").lower()
                if item_to_edit.isdigit() and 1 <= int(item_to_edit) <= len(items):
                    item_idx = int(item_to_edit)
                    item_to_edit = list(items.keys())[item_idx - 1]
                if item_to_edit in items:
                    original_price = items[item_to_edit]
                    new_price = input("Enter the new price for the item: ")
                    items[item_to_edit] = int(new_price)
                    print(
                        f"Item {item_idx}: '{item_to_edit.title()}' (Price: {original_price}) updated to Price: {new_price}.")
                else:
                    print("Item not found.")
            elif option == "3":
                new_item_name = input("Enter the name of the new item: ").strip().lower()
                new_item_price = input("Enter the price of the new item: ")
                items[new_item_name] = int(new_item_price)
                item_idx = len(items)
                print(f"New item {item_idx}: '{new_item_name.title()}' added with price: {new_item_price}.")
                write_items_to_csv(csv_file, items)

            elif option == "4":
                item_to_delete = input("Enter the name or number of the item you want to delete: ").lower()
                if item_to_delete.isdigit() and 1 <= int(item_to_delete) <= len(items):
                    item_idx = int(item_to_delete)
                    item_to_delete = list(items.keys())[item_idx - 1]
                if item_to_delete in items:
                    deleted_price = items.pop(item_to_delete)
                    delete_item_from_csv(csv_file, item_to_delete)
                    print(f"Item {item_idx}: '{item_to_delete.title()}' (Price: {deleted_price}) deleted from CSV.")
                else:
                    print("Item not found.")
            else:
                print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
