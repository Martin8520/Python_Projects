from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_user = email_username_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} || {email_user} || {password}\n")
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(font="Arial", text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(font="Arial", text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(font="Arial", text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "useremail@mail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
