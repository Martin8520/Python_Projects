from tkinter import *


def convert():
    converted = my_input.get()
    converted = float(converted) * 1.609
    my_label2.config(text=f"{converted:.2f}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=25)

button = Button(text="Convert", command=convert)
button.grid(column=2, row=3)

my_input = Entry(width=10)
my_input.grid(column=2, row=0)
my_input.get()

my_label = Label(text="is equal to", font=("Arial", 10))
my_label.grid(column=0, row=2)

my_label2 = Label(text="0", font=("Arial", 10))
my_label2.grid(column=2, row=2)

my_label1 = Label(text="Miles", font=("Arial", 10))
my_label1.grid(column=3, row=0)

my_label3 = Label(text="Km", font=("Arial", 10))
my_label3.grid(column=3, row=3)
window.mainloop()
