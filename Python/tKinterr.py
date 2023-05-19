from tkinter import *

root = Tk()


def button_click():
    label.config(text= "¡Hola " + entry.get() + "!")

label = Label(root, text="¿Cómo te llamas?")
label.pack()


entry = Entry(root)
entry.pack()

button = Button(root, text="Saludar", command=button_click)
button.pack()

root.mainloop()