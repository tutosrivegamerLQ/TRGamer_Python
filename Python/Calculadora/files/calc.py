class Operations:
	def __init__(self, numbers: str):
		self.numbers = numbers
		# Almacenar info de la entrada [cantidad operadores, operadores, error]
		# Tipos de errores: {0: **, 1: number*, 2:NoError}
		self.infoEntry = [] 
		self.check_entry() # Método que analiza entradas

	def check_entry(self):
		typeOperator = []
		err = 2
		for i in range(len(self.numbers)):
			char = self.numbers[i]
			match char:
				case "*":		
					opErr = self.operatorCheck(i, "Es multiplicación", typeOperator, char)			
					if opErr < 2:
						err = opErr
						break
				case "/":
					opErr = self.operatorCheck(i, "Es división", typeOperator, char)			
					if opErr < 2:
						err = opErr
						break
				case "+":
					opErr = self.operatorCheck(i, "Es suma", typeOperator, char)			
					if opErr < 2:
						err = opErr
						break
				case "-":
					opErr = self.operatorCheck(i, "Es resta", typeOperator, char)			
					if opErr < 2:
						err = opErr
						break

		lenOperators = self.lengthArray(typeOperator)
		self.infoEntry.append(lenOperators)
		self.infoEntry.append(typeOperator)
		self.infoEntry.append(err)

		print("Info operation: ", self.infoEntry)

	# Verificar si el operador está repetido o al final (agregar operadores válidos)
	def operatorCheck(self, iterator, message, opType, char):
		err = self.invalidOperator(iterator) 
		if err == 0:
			print( "No pueden haber dos operadores seguidos")
		elif err == 1:
			print( "El operador no puede estar al final")
		else:
			#print(message)
			if char not in opType:
				opType.append(char)
		return err

	# Buscar errores posibles (Syntax de error) en caso contrario llamar método exe
	def exeAction(self):
		# Verificar si no hay errores
		err = self.infoEntry[2]
		# Columna del operador
		operator = self.infoEntry[1]
		if len(operator) == 0:
			print("no hay operador")
		
		if err == 0:
			return "SyntaxError (operadores seguidos)"
		elif err == 1:
			return "SyntaxError (No pueden haber operadores al final)"
		else:
			result = self.exe(operator)
			return result
			
	# Ejecuta la operación correspondiente
	def exe(self, operator):
		if self.infoEntry[0] > 1:

			result = self.evalOperation()
			return result
		else:
			match operator[0]:
				case "+":
					return self.sum()
				case "-":
					return self.rest()
				case "*":
					return self.mult()
				case "/":
					return self.div()
				case '%':
					return self.percent()

	def returnResult(self):
		return self.exeAction()

	def sum(self):
		result = 0
		numbers = self.numbers.split("+")
		numbers = [float(i) for i in numbers]
		for number in numbers:
			result+=number
		return result

	def rest(self):
		numbers = self.numbers.split("-")
		numbers = [float(i) for i in numbers]
		result = numbers[0]
		for number in range(len(numbers)-1):
			result-=numbers[number+1]
		return result

	def mult(self):
		result = 1
		numbers = self.numbers.split("*")
		numbers = [float(i) for i in numbers]
		for number in numbers:
			result*=number
		return result

	def div(self):
		numbers = self.numbers.split("/")
		numbers = [float(i) for i in numbers]
		result = numbers[0]
		count = 1
		for i in range(len(numbers)-1):
			result /= numbers[i+1]			
		return result

	# Método para evaluar entrada compleja (diferentes operadores)
	def evalOperation(self):
		result = eval(self.numbers)
		return result

	# Longitud de un array
	def lengthArray(self, array):
		lenArray = len(array)
		return lenArray

	# Retornar errores (int) de entradas erróneas
	def invalidOperator(self, iterator):
		operators = ["*", "/", "-", "+"]
		err = 2
		if iterator+1 < len(self.numbers):
			if self.numbers[iterator+1] in operators:
				err = 0
		elif iterator+1 >= len(self.numbers):
				err = 1
		return err

def test(operation):
	op1 = Operations(operation)
	op1.returnResult()