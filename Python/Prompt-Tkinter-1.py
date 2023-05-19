from tkinter import *

ventana = Tk()
ventana.geometry("900x400")
def ejecutar_codigo():
    with open('C:/users/PortGamer/Desktop/Python/tKinterr.py', 'r', encoding='utf-8') as f:
        code = f.read()
        exec(code)
    
entry = Entry(ventana)
entry['bg'] ="red"
Hl = "Hello World"


text1 = Label(ventana, text = Hl, bg = "blue")
col1 = Button(ventana, text = "Click Me!", command=ejecutar_codigo)
text1.pack(fill = X)
entry.pack(fill= X)
col1.pack()


ventana.mainloop()
