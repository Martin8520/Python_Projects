from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import os
import json
import pyperclip

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "logo.png")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_user = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email_user,
        "password": password,
    }
    }

    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  # Updating old data with new data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # Saving updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="No Data file found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title=f"{website}",
                                message=f"No details for the {website} exists")


def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(title="Password Copied", message="Password copied to clipboard!")
    else:
        messagebox.showinfo(title="No Password", message="No password to copy!")


def copy_email():
    email = email_username_entry.get()
    if email:
        pyperclip.copy(email)
        messagebox.showinfo(title="Email Copied", message="Email copied to clipboard!")
    else:
        messagebox.showinfo(title="No Email", message="No email to copy!")


def copy_website():
    website = website_entry.get()
    if website:
        pyperclip.copy(website)
        messagebox.showinfo(title="Website Copied", message="Website copied to clipboard!")
    else:
        messagebox.showinfo(title="No Website", message="No website to copy!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(font="Arial", text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(font="Arial", text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(font="Arial", text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_username_entry = Entry(width=70)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "useremail@mail.com")
password_entry = Entry(width=50)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=59, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

copy_button_pass = Button(text="Copy Password", command=copy_password, width=11)
copy_button_pass.grid(row=3, column=3)

copy_button_email = Button(text="Copy Email", command=copy_email, width=11)
copy_button_email.grid(row=2, column=3)

copy_button_website = Button(text="Copy Website", command=copy_website, width=11)
copy_button_website.grid(row=1, column=3)
window.mainloop()
