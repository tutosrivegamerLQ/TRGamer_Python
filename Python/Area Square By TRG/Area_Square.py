from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import font

# Window main
root = Tk()
root.title("Area square By TRG")
root['bg'] = "#000080"
root.geometry("900x319")
root.resizable(width=False, height=False)
root.iconbitmap("ico.ico")
# End window main

# Variables 
myFont = font.Font(family="Helvetica", size=12, weight="bold")
# End variables

# Functions
def operationArea(a):
	a = int(a)
	b = a*a
	c = "The area is: "
	areA = unity.get()
	result['text'] = c, b, areA, "²"
	sideRight['text'] = a, areA
	sideBottom['text'] = a, areA
	print(c, b, areA + "²")

def operationPerimeter(a):
	a = int(a)
	b = 4
	c = a*b
	d = "The perimeter is: "
	unitY = unity.get()
	sideTop['text'] = a, unitY
	sideRight['text'] = a, unitY
	sideBottom['text'] = a, unitY
	sideLeft['text'] = a, unitY
	result['text'] =  d, c, unitY + "²"
	print(d, c, unitY + "²")	
# End functions


# Img
img = Image.open("square.png")

new_width = 300
new_height = 300

img = img.convert("RGB")
img = img.resize((new_width,new_height))
imgF1 = ImageTk.PhotoImage(img)
# End img


# Widgets declaration
numberOne = Entry(root, bg="#000066",fg="#00ff00", borderwidth=2, relief="solid", highlightbackground="#ffff99")
unity = Entry(root, bg="#000066",fg="#00ff00", borderwidth=2, relief="solid", highlightbackground="#ffff99")
labelOne = Label(root, text="Side value:")
labelUnity = Label(root, text="unit measurement: \n (mm, cm, m, km)")
btn_Perimeter = Button(root, text="Perimeter", width=12,command= lambda: operationPerimeter(numberOne.get()))
btn_Area = Button(root, text="Area", width=12, command= lambda: operationArea(numberOne.get()))
result = Label(root, fg="#66ff99", bg="#00004d",text="Result",  font=myFont, wraplength=350)
sideTop = Label(root, fg="#ffffff", bg="#000080", wraplength=90)
sideRight = Label(root, fg="#ffffff", bg="#000080", wraplength=90)
sideBottom = Label(root, fg="#ffffff", bg="#000080", wraplength=90, height=2)
sideLeft = Label(root, fg="#ffffff", bg="#000080", wraplength=90)
IMG = Label(root, image=imgF1, width=233, height=233)
# Widgets entry declaration

# Widgets config
labelOne.config(bg="#000080", fg="#ffffff")
labelUnity.config(bg="#000080", fg="#ffffff")
numberOne.config(font=("Helvetica", 14))
unity.config(font=("Helvetica", 14))
btn_Perimeter.config(bg="#3333cc", fg="#ffffff")
btn_Area.config(bg="#2e2eb8", fg="#ffffff")
# End widgets config

# Widget place
sideTop.place(rely=0.05, relx=0.67, anchor=CENTER)
sideRight.place(rely=0.43, relx=0.87, anchor=CENTER)
sideBottom.place(rely=0.93, relx=0.67, anchor=CENTER)
sideLeft.place(rely=0.43, relx=0.49, anchor=CENTER)
IMG.place(rely=0.12, relx=0.55)
# End widget place

# Widgets position
labelOne.grid(row=0,column=0, pady=12, padx=1, ipadx=6)
numberOne.grid(row=0, column=1, padx=12, columnspan=6)
labelUnity.grid(row=1, column=0, pady=12, padx=1)
unity.grid(row=1, column=1, padx=12, columnspan=6)
btn_Perimeter.grid(row=4, column=1, columnspan=2, pady=23)
btn_Area.grid(row=4, column=3, columnspan=2, pady=23)
result.grid(row=5, column=0, columnspan=12, padx=12)
# End widgets position



root.mainloop()