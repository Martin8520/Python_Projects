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
    if not existing_ids:
        return '0001'
    highest_id = max(int(item_id) for item_id in existing_ids)
    new_id = str(highest_id + 1).zfill(4)
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
    existing_ids = {}
    for category_num, category_file in categories.items():
        csv_file = os.path.join(script_dir, category_file)
        if os.path.exists(csv_file):
            items = read_items_from_csv(csv_file)
            all_items[category_num] = items
            existing_ids[category_num] = [item_id for item_id in items.keys() if
                                          item_id.isdigit() and len(item_id) == 4]

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

        items = all_items[user_choice]

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
                print("Returning to main menu...")
                break
            elif option == "1":
                search_term = input("Enter the item name to search for: ").lower()
                found_items = [(item_id, item) for item_id, (item_name, price) in items.items() if
                               search_term in item_name.lower()]
                if found_items:
                    print("Matching items:")
                    for item_id, (item_name, price) in found_items:
                        print(f"Item ID {item_id}: {item_name.title()} - {price} gold pieces")
                else:
                    print("No matching items found.")
            elif option == "2":
                item_id = input("Enter the ID of the item you want to edit: ")
                new_price = input("Enter the new price for the item: ")
                if item_id in items:
                    items[item_id] = (items[item_id][0], int(new_price))
                    write_items_to_csv(csv_file, items)
                    print("Price updated successfully.")
                else:
                    print("Item not found.")
            elif option == "3":
                new_item_name = input("Enter the name of the new item: ")
                new_item_price = input("Enter the price for the new item: ")
                new_item_id = generate_unique_id(existing_ids[user_choice])
                items[new_item_id] = (new_item_name, int(new_item_price))
                existing_ids[user_choice].append(new_item_id)
                write_items_to_csv(csv_file, items)
                print(f"New item {new_item_id}: '{new_item_name.title()}' added with price: {new_item_price}.")
            elif option == "4":
                item_id_or_name = input("Enter the ID or name of the item you want to delete: ")
                delete_item_from_csv(csv_file, item_id_or_name)
                items = read_items_from_csv(csv_file)
            else:
                print("Invalid option. Please enter a number between 0 and 4.")


if __name__ == "__main__":
    main()
