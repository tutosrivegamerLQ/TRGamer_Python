import tkinter
import pyautogui
from pymsgbox import *
root = tkinter.Tk()
root.geometry("500x200")

pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
'OK'
pyautogui.prompt('This lets the user type in a string and press OK.')
'This is what I typed in.'
count = 0

def clicked():
    global count
    count = count + 1
    print("Has clicked", count, "times")
    
a = "Core Gamer"

etiqueta = tkinter.Label(root, text= a)
etiqueta.pack()

root.mainloop()