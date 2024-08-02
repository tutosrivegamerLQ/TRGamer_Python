import files.calc as calc
import time as tm

# Funciones de operaciones
class FuncsOperations:
	def __init__(self, screen):
		self.operation = ''
		self.screen = screen

	# Crear una operación con los caracteres ingresados
	def makeOperation(self, number="1+1"):
		print("The number is: ", number)
		self.operation += str(number)
		print("Operation: ", self.operation)
		self.screenDisplay(self.operation)

	# Ejecutar operación y llamar mpetodo encargado de mostrar el resultado
	def exeOperation(self):
		syntaxError = ["SyntaxError (No pueden haber operadores al final)", "SyntaxError (operadores seguidos)"]
		instan = calc.Operations(self.operation)
		result = instan.returnResult()

		self.screenDisplay(result)
		self.operation = str(result)


	# Mostrar resultado en "pantalla" de la calculadora
	def screenDisplay(self, result):
		self.screen.set(result)

	def delOperation(self):
		self.operation = ''
		self.screen.set(self.operation)

# Clase de ventana (crear botones, eventos, etc)
class Window(FuncsOperations):
	def __init__(self, win, screen, width=200, height=200, bgColor="black", title="Srm Program"):
		super().__init__(screen)
		self.window = win # Ventana
		self.width = width # Ancho ventana
		self.height = height # Alto ventana
		self.bgColor = bgColor # Color de fondo ventana
		self.title = title # Título ventana

	# Obtener y retornar tamaño de pantalla (monitor)
	def size(self):
		size = [] # Tamaño ventana [ancho, alto]
		size.append(self.window.winfo_screenwidth())
		size.append(self.window.winfo_screenheight())
		return size

	# Crear varios botones (Cada botón se organiza según la posición en la matriz que está)
	# Ejemplo: buttons = [[1, 2, 3], [4, 5, 6]
	# Estarán así:
	# 1 -> Fila 0, columna 0
	# 2 -> Fila 0, columna 1
	# 3 -> Fila 0, columna 2
	# 4 -> Fila 1, columna 0
	# 5 -> Fila 1, columna 1
	# 6 -> Fila 1, columna 2
	# Así:
	# 1 2 3
	# 4 5 6
	def createButtons(self, buttons: list, Button, root):
		# Por cada elemento en la lista de botones
		for i in range(len(buttons)):
			for j in range(len(buttons[i])):
				btn = Button(root, text=str(buttons[i][j]), width=5, command= lambda digit = buttons[i][j]: self.makeOperation(digit))
				btn.grid(row=i+1, column=j, pady=12, padx=12, sticky='WE', ipady=12)

	# Crear botones, pero, en este caso se debe pasar la columna (por defecto = 0), las filas se asignan según su orden de índice
	def createBtn(self, buttons: list, Button, root, column=0):
		for i in range(len(buttons)):
			for j in range(len(buttons[i])):
				btn = Button(root, text=str(buttons[i][j]), width=5, command= lambda op = buttons[i][j]: self.makeOperation(op))
				btn.grid(row=i+1, column=column, pady=12, padx=12, sticky='WE', ipady=12)