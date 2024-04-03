import csv
import random
import tkinter as tk
from tkinter import messagebox
import os
import sys


class InventoryManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("D&D Price Checker")
        self.geometry("800x600")

        if getattr(sys, 'frozen', False):
            self.base_path = sys._MEIPASS
        else:
            self.base_path = os.path.abspath(os.path.dirname(__file__))

        self.categories = {
            'Armors': os.path.join(self.base_path, 'armors.csv'),
            'Magical Items': os.path.join(self.base_path, 'magical_items.csv'),
            'Potions': os.path.join(self.base_path, 'potions.csv'),
            'Weapons': os.path.join(self.base_path, 'weapons.csv'),
            'Miscellaneous': os.path.join(self.base_path, 'misc.csv')
        }

        self.current_category = tk.StringVar(self)
        self.current_category.set('Armors')

        self.category_label = tk.Label(self, text="Select Category:")
        self.category_label.pack()

        self.category_menu = tk.OptionMenu(self, self.current_category, *list(self.categories.keys()),
                                           command=self.load_items)
        self.category_menu.pack()

        self.search_label = tk.Label(self, text="Search Item:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search_item)
        self.search_button.pack()

        self.item_listbox = tk.Listbox(self, height=20, width=70)
        self.item_listbox.pack()

        self.load_items()

        self.edit_item_button = tk.Button(self, text="Edit Item", command=self.edit_item)
        self.edit_item_button.pack()

        self.delete_item_button = tk.Button(self, text="Delete Item", command=self.delete_item)
        self.delete_item_button.pack()

        self.add_item_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_item_button.pack()

        self.csv_location_button = tk.Button(self, text="CSV File Location", command=self.open_csv_folder)
        self.csv_location_button.pack()

    def load_items(self, event=None):
        filename = self.categories[self.current_category.get()]
        items = self.read_items_from_csv(filename)
        self.display_items(items)

    def read_items_from_csv(self, filename):
        items = {}
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 3:
                        item_id = row[0].strip()
                        item_name = row[1].strip()
                        price = int(row[2].split()[0])
                        items[item_id] = (item_name, price)
                    else:
                        print("Error: Row does not have the expected number of elements.")
        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError:
            print("Error: Unable to convert price to integer.")
        except Exception as e:
            print(f"Error: {e}")
        return items

    def display_items(self, items):
        self.item_listbox.delete(0, tk.END)
        for item_id, (item_name, price) in items.items():
            displayed_name = f"Item ID {item_id}: {item_name.title()} - {price} gold pieces"
            self.item_listbox.insert(tk.END, displayed_name)

    def edit_item(self):
        selected_item = self.get_selected_item()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to edit.")
            return

        filename = self.categories[self.current_category.get()]

        items = self.read_items_from_csv(filename)
        selected_item_id = selected_item[2]
        if selected_item_id not in items:
            messagebox.showerror("Error", "Selected item does not exist.")
            return

        selected_item_name, selected_item_price = selected_item[0], selected_item[1]

        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Item")
        edit_window.geometry("300x200")

        item_name_label = tk.Label(edit_window, text="Item Name:")
        item_name_label.pack()

        selected_item_name = selected_item_name.rstrip('-')

        new_item_name_entry = tk.Entry(edit_window)
        new_item_name_entry.pack()

        price_label = tk.Label(edit_window, text="Price:")
        price_label.pack()

        new_price_entry = tk.Entry(edit_window)
        new_price_entry.pack()

        new_item_name_entry.insert(0, selected_item_name)
        new_price_entry.insert(0, selected_item_price)

        def save_changes():
            new_name = new_item_name_entry.get().strip()
            new_price = new_price_entry.get().strip()
            if new_name and new_price:
                try:
                    new_price = int(new_price)
                except ValueError:
                    messagebox.showerror("Error", "Price must be an integer.")
                    return

                items[selected_item_id] = (new_name, new_price)
                self.write_items_to_csv(filename, items)
                self.load_items()
                edit_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        save_button = tk.Button(edit_window, text="Save", command=save_changes)
        save_button.pack()

    def delete_item(self):
        selected_item = self.get_selected_item()
        if selected_item:
            confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this item?")
            if confirmation:
                filename = self.categories[self.current_category.get()]
                items = self.read_items_from_csv(filename)
                del items[selected_item[2]]
                self.write_items_to_csv(filename, items)
                self.load_items()
        else:
            messagebox.showerror("Error", "Please select an item to delete.")

    def add_item(self):
        add_window = tk.Toplevel(self)
        add_window.title("Add Item")
        add_window.geometry("300x200")

        item_name_label = tk.Label(add_window, text="Item Name:")
        item_name_label.pack()

        new_item_name_entry = tk.Entry(add_window)
        new_item_name_entry.pack()

        price_label = tk.Label(add_window, text="Price:")
        price_label.pack()

        new_price_entry = tk.Entry(add_window)
        new_price_entry.pack()

        def save_item():
            new_name = new_item_name_entry.get().strip()
            new_price = new_price_entry.get().strip()
            if new_name and new_price:
                try:
                    new_price = int(new_price)
                except ValueError:
                    messagebox.showerror("Error", "Price must be an integer.")
                    return

                filename = self.categories[self.current_category.get()]
                items = self.read_items_from_csv(filename)
                new_item_id = self.generate_unique_id(items.keys())
                items[new_item_id] = (new_name, new_price)
                self.write_items_to_csv(filename, items)
                self.load_items()
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        save_button = tk.Button(add_window, text="Save", command=save_item)
        save_button.pack()

    def search_item(self):
        search_text = self.search_entry.get().strip().lower()
        filename = self.categories[self.current_category.get()]
        items = self.read_items_from_csv(filename)
        search_results = {}
        for item_id, (item_name, price) in items.items():
            if search_text in item_name.lower() or search_text == item_id:
                search_results[item_id] = (item_name, price)
        if search_results:
            self.display_items(search_results)
        else:
            messagebox.showinfo("Search Results", "No matching items found.")

    def write_items_to_csv(self, filename, items):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for item_id, (item_name, price) in items.items():
                writer.writerow([item_id, item_name, price])

    def generate_unique_id(self, existing_ids):
        while True:
            new_id = str(random.randint(1000, 9999))
            if new_id not in existing_ids:
                return new_id

    def get_selected_item(self):
        selected_item_index = self.item_listbox.curselection()
        if selected_item_index:
            selected_item_index = selected_item_index[0]
            selected_item_parts = self.item_listbox.get(selected_item_index).split()
            selected_item_id = selected_item_parts[2].rstrip(':')
            selected_item_name = ' '.join(selected_item_parts[3:-3])
            selected_item_price = selected_item_parts[-2]
            return selected_item_name, selected_item_price, selected_item_id
        else:
            return None

    def open_csv_folder(self):
        csv_folder = os.path.dirname(self.categories[self.current_category.get()])
        if sys.platform.startswith('darwin'):
            os.system('open "%s"' % csv_folder)
        elif os.name == 'nt':
            os.startfile(csv_folder)
        elif os.name == 'posix':
            os.system('xdg-open "%s"' % csv_folder)


if __name__ == "__main__":
    app = InventoryManagementApp()
    app.mainloop()
