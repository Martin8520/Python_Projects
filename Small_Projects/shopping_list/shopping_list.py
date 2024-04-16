import tkinter as tk
from tkinter import messagebox, filedialog
import csv


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List App")
        self.root.geometry("350x350")

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.items = []

        self.create_widgets()

    def load_items(self, filename):
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                self.items = list(reader)
                self.refresh_listbox()
        except FileNotFoundError:
            pass
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_items(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if filename:
                with open(filename, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(self.items)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_widgets(self):
        self.item_label = tk.Label(self.frame, text="Enter Item:")
        self.item_label.grid(row=0, column=0)

        self.item_entry = tk.Entry(self.frame)
        self.item_entry.grid(row=0, column=1)

        self.add_button = tk.Button(self.frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=2)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=1, columnspan=3)

        self.refresh_listbox()

        self.edit_button = tk.Button(self.frame, text="Edit Item", command=self.edit_item)
        self.edit_button.grid(row=2, column=0)

        self.delete_button = tk.Button(self.frame, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=2, column=1)

        self.open_csv_button = tk.Button(self.frame, text="Open CSV", command=self.open_csv)
        self.open_csv_button.grid(row=3, column=0)

        self.save_button = tk.Button(self.frame, text="Save to CSV", command=self.save_items)
        self.save_button.grid(row=3, column=1)

    def add_item(self):
        item = self.item_entry.get()
        if item:
            self.items.append([item])
            self.refresh_listbox()
            self.item_entry.delete(0, tk.END)
            self.item_entry.focus_set()
        else:
            messagebox.showwarning("Warning", "Please enter an item.")

    def edit_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            item = self.item_entry.get()
            if item:
                index = selected_index[0]
                self.items[index][0] = item
                self.refresh_listbox()
                self.item_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an item to edit.")
        else:
            messagebox.showwarning("Warning", "Please select an item to edit.")

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            del self.items[selected_index[0]]
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item[0])

    def open_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.load_items(filename)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
