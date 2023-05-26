import tkinter
ventana = tkinter.Tk()
ventana.geometry("900x300")
eti = tkinter.Label(ventana, bg = "#80f20d")
etiqueta = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#ff0000")
text2 = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#ff8000")
text3 = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#0080ff")
text4 = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#8000ff")
text5 = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#ff0040")
text5 = tkinter.Label(ventana, text = "Hello world, By tutos rive gamer", bg = "#00ff00")

eti.pack(fill = tkinter.BOTH, expand = True)
etiqueta.pack(fill = tkinter.Y, expand = True)
text2.pack(fill = tkinter.X)
text3.pack(fill = tkinter.X)
text4.pack(fill = tkinter.Y, expand = True)
text5.pack(fill = tkinter.X)
ventana.mainloop()

