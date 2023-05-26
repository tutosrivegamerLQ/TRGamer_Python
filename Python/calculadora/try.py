from tkinter import *

root = Tk()
root.geometry("500x600")
root.resizable(height=FALSE, width=FALSE)
root['bg'] = "greenyellow"
root.title("Things of try in Python")

""" # Functions



def my_function1(*kids):
    print("The youngest child is " + kids[2])


my_function1("Emil", "Tobias", "Linus")
# Functions


# Lambda


def x(number2): return number2 + 10


print(x(9))
# Lambda


# Read file

fIle = open('info.txt')
print(fIle.read())

# Read file
"""

# Functions program


def geText():
    GeText = Input.get()
    lAbel['text'] = GeText


def ChangeColor():
    GeColor = Input2.get()
    Input2['bg'] = GeColor
# Functions program


# Declaración de los widgets
Input = Entry(root, border="3", font="Calibri 20", width=30)
Input2 = Entry(root)
lAbel = Label(root, text="Hola", font="j 20")
btn1 = Button(root, text="Click Me!", command=geText)
btn2 = Button(root, text="Clicl Me! 2", command=ChangeColor)


# Posición de los widgets
Input.grid(row=0, pady=5, padx=30, columnspan=4)
Input2.grid(row=1, column=0)
lAbel.grid(row=1, column=1)
btn1.grid(row=2)
btn2.grid(row=3)
root.mainloop()
