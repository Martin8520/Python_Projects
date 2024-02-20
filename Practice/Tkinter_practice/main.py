from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="TEST LABEL", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"

my_label.config(text="New Text")


def button_clicked():
    my_label.config(text=my_input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

my_input = Entry(width=10)
my_input.pack()
my_input.get()



window.mainloop()
