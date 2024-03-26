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
    csv_file = os.path.join(script_dir, 'items.csv')

    if not os.path.exists(csv_file):
        print("Error: items.csv file not found.")
        return

    items = read_items_from_csv(csv_file)

    print("List of items:")
    for item in items:
        print(item.capitalize())

    while True:
        user_input = input("Enter an item name (type 'exit' to quit): ").lower()
        if user_input == 'exit':
            print("Exiting...")
            break
        elif user_input in items:
            print(f"The price of {user_input.capitalize()} is {items[user_input]} gold pieces.")
        else:
            print("Item not found.")


if __name__ == "__main__":
    main()
