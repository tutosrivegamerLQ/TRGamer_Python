from tkinter import Button, Label, Entry, Tk, StringVar
import files.funcs as funcs

class App:
	def __init__(self):
		# Ventana principal
		self.root = Tk()

		# Variables
		self.screenValue = StringVar()
		self.screenCalc = None

		# Funciones de ventana y pantalla del monitor (instancia)
		self.winFunc = funcs.Window(self.root, self.screenValue, 500, 400, "#00001a", "Calculadora")
		# Dimensiones de ventana
		self.screenW = self.winFunc.size()[0]
		self.screenH = self.winFunc.size()[1]
		self.windowW = self.winFunc.width # Ancho ventana
		self.windowH = self.winFunc.height # Alto ventana
		self.titleWin = self.winFunc.title
		self.bgColorWin = self.winFunc.bgColor
	
		self.centerWinW = (self.screenW - self.windowW) // 2 # Centro horizontal
		self.centerWinH = (self.screenH - self.windowH) // 2 # Centro vertical
		
		

		# Lista de botones
		self.buttons = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [0, '.']]
		self.operators = ['+', '-', '/', '*']

		# Dar opciones de ventana
		self.windowOptions()
		# Crear y poner widgets en ventana
		self.widgets()
		
	def windowOptions(self):
		# geometría de la ventana principal
		self.root.geometry(f"{self.windowW}x{self.windowH}+{self.centerWinW}+{self.centerWinH}")
		self.root.resizable(False, False)
		self.root.title(self.titleWin)
		self.root['bg'] = self.bgColorWin

	def widgets(self):
		# Widgets Creación
		self.screenCalc = Label(self.root, textvariable=self.screenValue, width=self.windowW//8, height=3)
		self.btnDel = Button(self.root, text='C', command=self.winFunc.delOperation)
		self.btnEqual = Button(self.root, text='=', width=12, command=self.winFunc.exeOperation)
		self.copyRight = Label(self.root, text='©Inge. SRM', bg='#00001a', fg='#ffffff')
		
		# Creación de botones automatizada (bucles)
		self.winFunc.createButtons(self.buttons, Button, self.root)
		self.winFunc.createBtn(self.operators, Button, self.root, 3)
		
		# Widgets Posición
		self.screenCalc.grid(row=0, column=0, pady=12, padx=30, columnspan=4)
		self.btnEqual.grid(row=4, column=2, pady=12, ipady=12, sticky='WE', padx=12)
		self.btnDel.grid(row=0, column=3)
		self.copyRight.grid(row=5, column=1, columnspan=2)

# Instancia clase App
app = App()

# Actualizar ventana constantemente
app.root.mainloop()