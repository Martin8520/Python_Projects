from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="TEST LABEL", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New text"

my_label.config(text="New Text")


def button_clicked():
    my_label.config(text=my_input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="BUTTON", command=button_clicked)
button2.grid(column=2, row=0)

my_input = Entry(width=10)
my_input.grid(column=3, row=3)
my_input.get()



window.mainloop()
