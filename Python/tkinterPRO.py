import tkinter as tk

root = tk.Tk()
root.geometry("200x300")
root['bg'] = "lightblue"


etiqueta = tk.Label(root,text="Hello World", bg="greenyellow")
etiqueta.pack()

x = 2
for x in range (1):
	x+=5
print(x)


textArea = tk.Entry(root)
textArea.pack()

def GetTextArea():
	TEXT = textArea.get()
	etiqueta['text'] = TEXT

btn1 = tk.Button(root,text = "CLICK ME!", command = GetTextArea)
btn1.pack()

boton1 = tk.Button(root, text="1")
boton1.pack()

root.mainloop()