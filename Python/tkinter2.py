import tkinter

ventana = tkinter.Tk()
ventana.geometry("600x600")
ventana['bg'] = "#ff0000"
def click():
	print("hello")
	ventana['bg'] = "blue"
	if ventana['bg'] == "blue":
		ventana['bg'] = "yellow"

btn1 = tkinter.Button(ventana, text = "Presiona", bg = "#00ff80", command =  click)
btn1.pack()
ventana.mainloop()