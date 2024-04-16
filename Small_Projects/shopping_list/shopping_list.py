import tkinter as tk
from tkinter import messagebox
import csv


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List App")
        self.root.geometry("350x350")

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.items = []

        self.load_items()

        self.create_widgets()

    def load_items(self):
        try:
            with open("shopping_list.csv", "r", newline="") as file:
                reader = csv.reader(file)
                self.items = list(reader)
        except FileNotFoundError:
            pass

    def save_items(self):
        with open("shopping_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.items)

    def create_widgets(self):
        self.item_label = tk.Label(self.frame, text="Enter Item:")
        self.item_label.grid(row=0, column=0)

        self.item_entry = tk.Entry(self.frame)
        self.item_entry.grid(row=0, column=1)

        self.add_button = tk.Button(self.frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=2)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=1, columnspan=3)

        for item in self.items:
            self.listbox.insert(tk.END, item[0])

        self.edit_button = tk.Button(self.frame, text="Edit Item", command=self.edit_item)
        self.edit_button.grid(row=2, column=0)

        self.delete_button = tk.Button(self.frame, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=2, column=1)

    def add_item(self):
        item = self.item_entry.get()
        if item:
            self.items.append([item])
            self.listbox.insert(tk.END, item)
            self.save_items()
            self.item_entry.delete(0, tk.END)
            self.item_entry.focus_set()  # Set focus to the entry field after adding an item
        else:
            messagebox.showwarning("Warning", "Please enter an item.")

    def edit_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            item = self.item_entry.get()
            if item:
                self.items[selected_index[0]][0] = item
                self.listbox.delete(selected_index[0])
                self.listbox.insert(selected_index[0], item)
                self.save_items()
                self.item_entry.delete(0, tk.END)
                self.item_entry.focus_set()  # Set focus to the entry field after editing an item
            else:
                messagebox.showwarning("Warning", "Please enter an item to edit.")
        else:
            messagebox.showwarning("Warning", "Please select an item to edit.")

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index[0])
            del self.items[selected_index[0]]
            self.save_items()
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
