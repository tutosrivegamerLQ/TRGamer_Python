from tkinter import * #imports Tkinter module
import random  #imports random module for choice function
import time #imports time module

l=["Thomas", "Philip", "John", "Adam", "Kate", "Sophie", "Anna"]       #creates a list with 7 items
def pri():  #function that asigns randomly item from l list to     variable a and prints it in CLI
    a = random.choice(l) #HOW CAN I PRINT a variable IN label     textvarible????
    print (a) 
    time.sleep(0.5)


root = Tk()                 #this
frame = Frame(root)         #creates
frame.pack()                #GUI frame
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

#GUI button
redbutton = Button(frame, text="Choose name", fg="red", command = pri)
redbutton.pack( side = LEFT)

#GUI label
var = StringVar()
label = Label(bottomframe, textvariable= var, relief=RAISED )
label.pack( side = BOTTOM)

root.mainloop() 