import tkinter
import pyautogui

window = tkinter.Tk()
window.geometry("600x200")
window['bg'] = "#ff0000"

count = 0
def clicked():
    global count 
    count = count + 1
    print("Has clicked",count,"times")

button = tkinter.Button(window, text="Click me!", command=clicked, bg = "")
button.pack()

window.mainloop()