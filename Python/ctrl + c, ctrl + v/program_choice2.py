from tkinter import *
import time
import random

l=["Thomas", "Philip", "John", "Adam", "Kate", "Sophie", "Anna"]       #creates a list with 7 items
def pri():  #function that asigns randomly item from l list to     variable a and prints it in CLI
    a = random.choice(l) #HOW CAN I PRINT a variable IN label     textvarible????
    print (a)     #prints in CLI
    return a


root = Tk()
root.geometry("300x100")
var = IntVar() # instantiate the IntVar variable class
var.set("Philip")     # set it to 0 as the initial value

# the button command is a lambda expression that calls the set method on the var,
# with the var value (var.get) increased by 1 as the argument
Button(root, text="Choose name", command=lambda: var.set(pri())).pack()

# the label's textvariable is set to the variable class instance
Label(root, textvariable=var).pack()

mainloop()