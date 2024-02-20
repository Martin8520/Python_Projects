from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="TEST LABEL", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"

my_label.config(text="New Text")


def button_clicked():
    my_label.config(text="Button Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()





window.mainloop()
