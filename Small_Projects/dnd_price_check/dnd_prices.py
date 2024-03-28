import csv
import os
import random


def read_items_from_csv(filename):
    items = {}
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) >= 3:
                item_id = row[0].strip()
                item_name = row[1].strip().lower()
                price = int(row[2])
                items[item_id] = (item_name, price)
            else:
                print(f"Error: Row {reader.line_num} does not have the expected number of elements.")
    return items


def write_items_to_csv(filename, items):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Item', 'Price'])
        for item_id, (item_name, price) in items.items():
            writer.writerow([item_id, item_name, price])


def display_items_with_numbers(items):
    for item_id, (item_name, price) in items.items():
        print(f"Item ID {item_id}: {item_name.title()} - {price} gold pieces")


def delete_item_from_csv(filename, item_id_or_name):
    updated_items = {}
    found = False
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        updated_items[header[0]] = header[1:]
        for row in reader:
            if row[0].strip() == item_id_or_name:
                found = True
            elif row[1].strip().lower() == item_id_or_name.lower():
                found = True
            else:
                updated_items[row[0].strip()] = [row[1], row[2]]

    if not found:
        print(f"Item '{item_id_or_name}' not found.")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Item', 'Price'])
        for item_id, (item_name, price) in updated_items.items():
            writer.writerow([item_id, item_name, price])


def generate_unique_id(existing_ids):
    while True:
        new_id = str(random.randint(1000, 9999))
        if new_id not in existing_ids:
            return new_id


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    categories = {
        1: 'armors.csv',
        2: 'magical_items.csv',
        3: 'potions.csv',
        4: 'weapons.csv',
        5: 'misc.csv'
    }
    all_items = {}
    existing_ids = []
    for category_num, category_file in categories.items():
        csv_file = os.path.join(script_dir, category_file)
        if os.path.exists(csv_file):
            items = read_items_from_csv(csv_file)
            all_items.update(items)
            existing_ids.extend([item_id for item_id in items.keys() if item_id.isdigit() and len(item_id) == 4])

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

            if option == "0":
                break
            elif option == "1":
                user_input = input("Enter an item name or its number to search or type 'back' to go back: ").lower()

                found_items = []
                if user_input.isdigit() and any(int(user_input) == int(item_id) for item_id in items):
                    item_id = user_input
                    found_items.append((item_id, items[item_id]))
                else:
                    for item_id, (item_name, price) in items.items():
                        if user_input in item_name.lower():
                            found_items.append((item_id, (item_name, price)))

                if found_items:
                    if len(found_items) == 1:
                        print(
                            f"Found item: {found_items[0][0]} "
                            f"- {found_items[0][1][0]}: {found_items[0][1][1]} gold pieces.")
                    else:
                        for item_id, (item_name, price) in found_items:
                            print(f"Found item: {item_id} - {item_name}: {price} gold pieces.")
                else:
                    print("Item not found.")

            elif option == "2":
                item_to_edit = input("Enter the name or number of the item you want to edit: ").strip().lower()
                if item_to_edit.isdigit() and 1 <= int(item_to_edit) <= len(items):
                    item_idx = int(item_to_edit)
                    item_to_edit = list(items.keys())[item_idx - 1]
                elif item_to_edit.lower() in [name.lower() for name, _ in items.values()]:
                    item_to_edit = next(
                        item_id for item_id, (name, _) in items.items() if name.lower() == item_to_edit.lower())
                if item_to_edit in items:
                    original_price = items[item_to_edit][1]
                    new_price = input("Enter the new price for the item: ")
                    items[item_to_edit] = (items[item_to_edit][0], int(new_price))
                    print(
                        f"Item {item_to_edit}: '{items[item_to_edit][0].title()}' (Price: {original_price})"
                        f" updated to Price: {new_price}.")
                    write_items_to_csv(csv_file, items)
                else:
                    print("Item not found.")
            elif option == "3":
                new_item_name = input("Enter the name of the new item: ").strip().lower()
                new_item_price = input("Enter the price of the new item: ")
                new_item_id = generate_unique_id(existing_ids)
                items[new_item_id] = (new_item_name, int(new_item_price))
                item_idx = len(items)
                print(f"New item {new_item_id}: '{new_item_name.title()}' added with price: {new_item_price}.")
                write_items_to_csv(csv_file, items)
                items = read_items_from_csv(csv_file)

            elif option == "4":
                item_to_delete = input("Enter the name or number of the item you want to delete: ").strip().lower()
                deleted = False
                for item_id, (name, _) in items.items():
                    if item_to_delete == name.lower() or item_to_delete == str(item_id):
                        del items[item_id]
                        print(f"Item '{item_id}': '{name}' deleted from {csv_file}.")
                        deleted = True
                        break
                if not deleted:
                    print("Item not found.")

                with open(csv_file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Item", "Price"])
                    for item_id, (name, price) in items.items():
                        writer.writerow([item_id, name, price])
            else:
                print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
