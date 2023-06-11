import tkinter as tk # For main app (Label, Entry, Button...)
from tkinter import ttk # For tabs (Notebook, Frame)
from tkinter import font
import math
import re

# Main window
root = tk.Tk() # Create a window main
root.iconbitmap("icon.ico")
root.title("Kit TRG")
width_root = 1180
height_root = 360
x = (root.winfo_screenwidth() // 2) - (width_root // 2)
y = (root.winfo_screenheight() // 2) - (height_root // 2)

# Establece la ubicación y el tamaño de la ventana
geometry_string = f"{width_root}x{height_root}+{x}+{y}"
root.geometry(geometry_string)
root.resizable(width=False, height=False)
# End main window

# Main tab (This acumule all list of tabs)
notebook = ttk.Notebook(root) # Create a tab panel in the main window
notebook.pack(fill='both', expand='yes') # Packs the tab panel into the main window
# End main tab 

# Var
index = 0
font_Fixedsys = font.Font(font="Fixedsys", size=62) # Font of tkinter font (Type)
operador_insertado = False
count = 0
pi = math.pi

# Colors 
red_Color = "#ff0000"
white_Color = "#ffffff"
black_Color = "#000000"
# End colors
# End var

# Functions
def calc():
	text = screenTab1.get()
	operation = eval(text)
	screenTab1.delete(0, tk.END)
	screenTab1.insert(0,operation)
	index = tk.END


def move_cursor(event):
    screenTab1.icursor(tk.END)

def CLick(value):
	global index
	index +=1
	inserT = screenTab1.insert(tk.END, value)
	screenTab1.focus_set()

def rootCuadrade():
	global index
	n1 = screenTab1.get()
	n2 = float(n1)
	cuadrade = math.pow(n2, 0.5)
	screenTab1.delete(0, tk.END)
	screenTab1.insert(0, cuadrade)
	index +=1

def deleteAll():
	screenTab1.delete(0, tk.END)

def delete():
	screenTab1.delete(screenTab1.index(tk.END)-1, tk.END)

def pointAdd():
    current_text = screenTab1.get()
    if "." not in current_text:
        screenTab1.insert(tk.END, ".")
    else:
        operator_number_regex = r"[+\-*/]\d+$"
        if re.search(operator_number_regex, current_text):
            screenTab1.insert(tk.END, ".")

def check_entry(event):
    current_text = screenTab1.get()
    operator_number_regex = r"[+\-*/]\d+$"
    btn_Point.config(state=tk.NORMAL if "." not in current_text or re.search(operator_number_regex, current_text) else tk.DISABLED)

def piInsert():
	global pi, index
	index +=1
	screenTab1.insert(tk.END, pi)
	index = 0

def percentCalc():
	global index, count
	text = screenTab1.get()
	try:
		convert = float(text)
		operation = eval(text) / 100
		screenTab1.delete(0, tk.END)
		screenTab1.insert(tk.END, operation)
		index = 0
	except ValueError:
		count +=1
		print("Error", count) 


def key_press(event):
    if event.keysym == 'u' and event.state == 4:  
        colorScheme()

def key_press2(event):
	if event.keysym == "y" and event.state == 4:
		colorScheme2()

def colorScheme():
	tab1.config(style="Style1_Tab1.TFrame")
	button_style_number.configure("Button_number.TButton", background="#ff0000", borderwidth=1, bordercolor="#333333", foreground="#ffffff", font="Helvetica 14", focuscolor="")
	button_style_number.map("Button_number.TButton", background=[('active', '#004d99')], foreground=[('active', '#80ff00')])
	button_style_others.configure("Button_Other.TButton", background="#800000", foreground="#ffffff", font="Helvetica 14", borderwidth=1, bordercolor="#333333", focuscolor="")
	button_style_others.map("Button_Other.TButton", background=[('active', '#004d99')], foreground=[('active', '#ffff00')])

def colorScheme2():
	tab1.config(style="Style2_Tab1.TFrame")
	button_style_number.configure("Button_number.TButton", background="#004d99", borderwidth=1, bordercolor="#ff0000", foreground="#ffffff", focuscolor="")
	button_style_number.map("Button_number.TButton", background=[('active', '#ff0000')], foreground=[('active', '#ffff00')])
	button_style_others.configure("Button_Other.TButton", background="#800000", foreground="#ffffff", font="Helvetica 14", borderwidth=1, bordercolor="#333333", focuscolor="")
	button_style_others.map("Button_Other.TButton", background=[('active', '#004d99')], foreground=[('active', '#80ff00')])

def entryFocus(event):
	if event.widget == notebook:
		current_frame = notebook.nametowidget(notebook.select())
		if current_frame == tab1:
			screenTab1.focus_set()
		elif current_frame == tab2:
			screenTab2.focus_set()

def deleteLabelAlert_1():
	current_tab = notebook.tab(notebook.select(), "text")
	if current_tab == "Calculator":
		labelAlert_1.place_forget()
	else:
		labelAlert_1.place(x=440, y=15)

#End functions

# Tab 1
# Style tab
styleTab1 = ttk.Style() 
styleTab1.theme_use('clam')
styleTab1.configure("Style1_Tab1.TFrame", background="#002266")
style2Tab1 = ttk.Style() 
style2Tab1.configure("Style2_Tab1.TFrame", background="#ff0000")

button_style_number = ttk.Style()
button_style_number.configure("Button_number.TButton", background="#ff0000", borderwidth=1, bordercolor="#333333", foreground="#ffffff", font="Helvetica 14", focuscolor="")
button_style_number.map("Button_number.TButton", background=[('active', '#004d99')], foreground=[('active', '#80ff00')])

button_style_others = ttk.Style()
button_style_others.configure("Button_Other.TButton", background="#800000", foreground="#ffffff", font="Helvetica 14", borderwidth=1, bordercolor="#333333", focuscolor="")
button_style_others.map("Button_Other.TButton", background=[('active', '#004d99')], foreground=[('active', '#ffff00')])
# End style tab

# Create a new tab to side of others
tab1 = ttk.Frame(notebook, style="Style1_Tab1.TFrame")

# Add this tab to list tab
notebook.add(tab1, text="Calculator") 

# Var widgets
labelAlert_1 = ttk.Label(tab1, text="Press (Control + U) for color scheme One \n Press (Control + Y) for return to original color scheme", style="StyleAlert.TLabel")
screenTab1 = tk.Entry(tab1, bg="#004d99", fg="#ccff33", font="Helvetica 14", justify="right")
btn_Delete_One = ttk.Button(tab1, text=chr(9003),  style="Button_Other.TButton", command=delete)
btn_Delete_All = ttk.Button(tab1, text="C", style="Button_Other.TButton", command=deleteAll)
root_cuadrade = ttk.Button(tab1, text="√",  style="Button_Other.TButton", command=rootCuadrade)
pi_number = ttk.Button(tab1, text="π",  style="Button_Other.TButton", command=piInsert)
btn_Division = ttk.Button(tab1, text="÷",  style="Button_Other.TButton", command=lambda: CLick("/"))
percent = ttk.Button(tab1, text="%",  style="Button_Other.TButton", command=percentCalc)
btn_7 = ttk.Button(tab1, text="7", style="Button_number.TButton", command=lambda:CLick("7"))
btn_8 = ttk.Button(tab1, text="8", style="Button_number.TButton", command=lambda:CLick("8"))
btn_9 = ttk.Button(tab1, text="9", style="Button_number.TButton", command=lambda:CLick("9"))
btn_multiply = ttk.Button(tab1, text="X",  style="Button_Other.TButton", command=lambda:CLick("*"))
btn_4 = ttk.Button(tab1, text="4", style="Button_number.TButton", command=lambda:CLick("4"))
btn_5 = ttk.Button(tab1, text="5", style="Button_number.TButton", command=lambda:CLick("5"))
btn_6 = ttk.Button(tab1, text="6", style="Button_number.TButton", command=lambda:CLick("6"))
btn_less = ttk.Button(tab1, text="-",  style="Button_Other.TButton", command=lambda:CLick("-"))
btn_1 = ttk.Button(tab1, text="1", style="Button_number.TButton", command=lambda:CLick("1"))
btn_2 = ttk.Button(tab1, text="2", style="Button_number.TButton", command=lambda:CLick("2"))
btn_3 = ttk.Button(tab1, text="3", style="Button_number.TButton", command=lambda:CLick("3"))
btn_more = ttk.Button(tab1, text="+",  style="Button_Other.TButton", command=lambda:CLick("+"))
btn_0 = ttk.Button(tab1, text="0", style="Button_number.TButton", width=8, command=lambda:CLick("0"))
btn_Point = ttk.Button(tab1, text=",",  style="Button_Other.TButton", command=pointAdd)
btn_equal = ttk.Button(tab1, text="=",  style="Button_Other.TButton", command=calc)
# End var widgets	

root.after(2000, deleteLabelAlert_1)

# Bind
#Vincular el evento <<NotebookTabChanged>> a la función resize_windo

screenTab1.bind("<Return>", lambda event: calc())
screenTab1.bind("<Key>", move_cursor)
root.bind('<Control-u>', key_press)
root.bind("<Control-y>", key_press2)
screenTab1.bind("<KeyRelease>", check_entry)
# End bind


# Widgets config
screenTab1.focus()
screenTab1.config(state="normal", insertbackground='#004d99')
# End widgets config

# Widgets position
labelAlert_1.place(x=440, y=15)
screenTab1.grid(row=0, column=0, pady=12, padx=12, ipady=8, columnspan=4, sticky="nsew")
btn_Delete_One.grid(row=1, column=0, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_Delete_All.grid(row=1, column=1, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
root_cuadrade.grid(row=1, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nse")
pi_number.grid(row=1, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsw")
btn_Division.grid(row=1, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nse")
percent.grid(row=1, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsw")
btn_7.grid(row=2, column=0, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_8.grid(row=2, column=1, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_9.grid(row=2, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_multiply.grid(row=2, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_4.grid(row=3, column=0, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_5.grid(row=3, column=1, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_6.grid(row=3, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_less.grid(row=3, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_1.grid(row=4, column=0, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_2.grid(row=4, column=1, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_3.grid(row=4, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_more.grid(row=4, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_0.grid(row=5, column=0, columnspan=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_Point.grid(row=5, column=2, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
btn_equal.grid(row=5, column=3, padx=3, pady=4, ipady=4, ipadx=4, sticky="nsew")
labelAlert_1.lift()
# End widgets position

# Tab1 configure
tab1.columnconfigure((0,1,2,3), weight=1)
tab1.rowconfigure((0,1,2,3), weight=1)
# End tab 1


# Tab 2
# Functions local
def areaS(event):
	text = screenTab2.get()
	text2 = screen_Measurement.get()
	convert = float(text)
	if convert <= 0:
		screenTab2.insert(0,"Error, zero or number negative. Try again.")
	else:
		operation = convert * convert
		screenTab2.delete(0, tk.END)
		screenTab2.insert(0, operation)
		operation_Convert = str(operation)
		canvasSquare.itemconfig(side_bottom_label, text=text + text2)
		canvasSquare.itemconfig(side_right_label, text=text + text2)
		canvasSquare.itemconfig(side_left_label, text=text + text2)
		canvasSquare.itemconfig(side_top_label, text=text + text2)	
		canvasSquare.itemconfig(area_Side, text=text + text2 + "²")
		canvasSquare.itemconfig(area_Operation, text=operation_Convert + text2 + "²")
		label_Result['text'] = "Area = " + operation_Convert + text2 + "²"
		label_Area['text'] = "Area = " + text + text2
		screenTab2.focus_set()
		zeroSides()

def zeroSides(event=None):
	text = screenTab2.get()
	text2 = screen_Measurement.get()
	if not text or text == "Inf":
		canvasSquare.itemconfig(side_bottom_label, text="Bottom")
		canvasSquare.itemconfig(side_right_label, text="Right")
		canvasSquare.itemconfig(side_left_label, text="Left")
		canvasSquare.itemconfig(side_top_label, text="Top")	
		canvasSquare.itemconfig(area_Side, text="L²")
		canvasSquare.itemconfig(area_Operation, text="L²")
		label_Result['text'] = "Area = L²"
		label_Area['text'] = "Area = L²"
	if text2 == "":
		screen_Measurement.delete(0,tk.END)
		screen_Measurement.insert(0, "Error, null space")

def borrarEntry2(event):
	if screen_Measurement.get() == "Error, null space":
		screen_Measurement.delete(0, tk.END)

def moveSquare(event):
	global square_idl
	if event.keysym == "d" and event.state == 4: 
		canvasSquare.move(square_id, 5, 0)
		canvasSquare.move(side_top_label, 5, 0)
		canvasSquare.move(side_bottom_label, 5, 0)
		canvasSquare.move(side_left_label, 5, 0)
		canvasSquare.move(side_right_label, 5, 0)
		canvasSquare.move(area_Side, 5, 0)
		canvasSquare.move(area_A, 5, 0)
		canvasSquare.move(area_B, 5, 0)
		canvasSquare.move(area_Operation, 5, 0)
	if event.keysym == "a" and event.state == 4:
		canvasSquare.move(square_id, -5, 0)
		canvasSquare.move(side_top_label, -5, 0)
		canvasSquare.move(side_bottom_label, -5, 0)
		canvasSquare.move(side_left_label, -5, 0)
		canvasSquare.move(side_right_label, -5, 0)
		canvasSquare.move(area_Side, -5, 0)
		canvasSquare.move(area_A, -5, 0)
		canvasSquare.move(area_B, -5, 0)
		canvasSquare.move(area_Operation, -5, 0)

def deleteAll():
	screenTab2.delete(0, tk.END)
	screen_Measurement.delete(0, tk.END)
	screenTab2.focus_set()
	zeroSides()

def deleteLabelAlert(event):
	current_tab = notebook.tab(notebook.select(), "text")
	if current_tab == "Area Square":
		root.after(2000, lambda:labelAlert.place_forget())

# End functions local

# Widgets style
styletab2_Frame = ttk.Style()
styletab2_Frame.configure("Frame_Style_dark.TFrame", background="#333333")

label_Style = ttk.Style()
label_Style.configure("Label_Style.TLabel", background="#333333",font=("Arial", 12, "bold"), foreground="#ff0000")

btn_style_tab2 = ttk.Style()
btn_style_tab2.configure("Btn_Style_Tab2.TButton", background="#ff0000", focuscolor="", font=("Consolas", 12, "bold"))

label_ForScreen_style = ttk.Style()
label_ForScreen_style.configure("Label_Screen_Tab2.TLabel", background="#333333",font=("Helvetica", 10, "bold"), foreground="#ffffff")

label_ALert = ttk.Style()
label_ALert.configure("StyleAlert.TLabel", background="#ff0000", foreground="#ffffff", font=("Helvetica", 12, "bold"), highlightcolor="#b3c6ff", highlightthickness=2)
# End widgets style

# Create a new tab to side of others
tab2 = ttk.Frame(notebook, style="Frame_Style_dark.TFrame") 

# Add this tab to main tab
notebook.add(tab2, text="Area Square") 

# Var tab 2
width_ROOT = root.winfo_width()
height_ROOT = root.winfo_height()

rectangulo_Width = 250
rectangulo_Height = 250

rect_X1 = (width_ROOT - rectangulo_Width) // 2 - 60
rect_Y1 = (height_ROOT - rectangulo_Height) // 2 - 15
X2_rect = rect_X1 + rectangulo_Width
Y2_rect = rect_Y1 + rectangulo_Height

canvasSquare = tk.Canvas(tab2, width=width_ROOT, height=height_ROOT, bg="#333333", highlightthickness=0)
square_id = canvasSquare.create_rectangle(rect_X1, rect_Y1, X2_rect, Y2_rect, fill="#000080", outline="#bfff00", width=2, dash=(3,3))
# End var tab 2

# Var widgets
label_ForScreen = ttk.Label(tab2, text="Enter the measurement of the side", style="Label_Screen_Tab2.TLabel")
screenTab2 = tk.Entry(tab2, justify="right", bg="#333333", fg="#bfff00", width=22, highlightthickness=1, borderwidth=2, relief="raised", highlightcolor='red', highlightbackground='red', font=("@Kozuka Mincho Pro EL", 12))
screen_Measurement = tk.Entry(tab2,justify="right", bg="#333333", fg="#bfff00", width=22, highlightthickness=1, borderwidth=2, relief="raised", highlightcolor='red', highlightbackground='red', font=("@Kozuka Mincho Pro EL", 12))
label_Measurement = ttk.Label(tab2, text="Enter measurement type (mm, cm, m, km)", style="Label_Screen_Tab2.TLabel")
btn_Area = ttk.Button(tab2, text="Area", style="Btn_Style_Tab2.TButton", command=lambda event=None :areaS(event))
btn_Delete_All_Tab2 = ttk.Button(tab2, text=chr(9003), style="Btn_Style_Tab2.TButton", command=deleteAll)
label_Result = ttk.Label(tab2, text="Area = L²", style="Label_Style.TLabel")
label_Area = ttk.Label(tab2, text="Area = L²", style="Label_Style.TLabel")
labelAlert = ttk.Label(tab2, text="Press (Control + A) for move to left the square \n Press (Control + D) for move to right the square", style="StyleAlert.TLabel")
side_bottom_label = canvasSquare.create_text(530, 305, text="bottom", fill="#bfff00", font=("Helvetica", 8, "bold"))
side_right_label = canvasSquare.create_text(755, 165, text="right", fill="#bfff00", justify="right", font=("Helvetica", 8, "bold"))
side_left_label = canvasSquare.create_text(298, 165, text="left", fill="#bfff00", justify="left", font=("Helvetica", 8, "bold"))
side_top_label = canvasSquare.create_text(530, 23, text="top", fill="#bfff00", font=("Helvetica", 8, "bold"))

area_A = canvasSquare.create_text(430, 155, text="A =", fill="#ff0000", font=("Helvetica", 12, "bold"))
area_Side = canvasSquare.create_text(550, 155, text="L²",font=("Helvetica", 8, "bold"), fill="#ff0000")
area_B = canvasSquare.create_text(430, 175, text="A =", fill="#ff0000", font=("Helvetica", 12, "bold"))
area_Operation = canvasSquare.create_text(550, 175, text="L²",font=("Helvetica", 8, "bold"), fill="#ff0000")
# End var widgets

# Widgets config
# End config widgets

# Widgets bind
screenTab2.bind("<Return>", areaS)
screen_Measurement.bind("<Return>", areaS)
notebook.bind("<<NotebookTabChanged>>", entryFocus)
root.bind("<Control-d>", moveSquare)
root.bind("<Control-a>", moveSquare)
screenTab2.bind("<KeyRelease>", zeroSides)
screen_Measurement.bind("<KeyRelease>", zeroSides)
screen_Measurement.bind("<FocusIn>", borrarEntry2)
notebook.bind("<<NotebookTabChanged>>", deleteLabelAlert)
notebook.bind("<<NotebookTabChanged2>>", deleteLabelAlert)
#End widgets bind

# Position widgets
label_ForScreen.place(x=45, y=12)
screenTab2.grid(row=3, column=0, columnspan=4, pady=35, padx=42)
label_Measurement.place(x=22, y=90)
screen_Measurement.grid(row=4, column=0, columnspan=4, pady=12, padx=42)
btn_Area.place(x=40, y=150)
btn_Delete_All_Tab2.place(x=170, y=150)
label_Result.place(y=245, x=50)
label_Area.place(y=215, x=50)
canvasSquare.place(y=0, x=351)
labelAlert.place(y=30,x=300)
# End position widgets
# End tab 2
root.mainloop()