# Playfair Cipher

#Entrada: Una palabra que representa la llave para encriptar y desencriptar
#Procesamiento: En base a la llave se crea una matriz de 5x5 donde se ingresan las letras
#Salida: Matriz para el cifrado playfair con la llave ingresada
def createMatrix(key):
	rows = 5
	columns = 5
	playfairMatrix = []
	#Define all leters without the j
	allLetters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#Now we remove the repeated letters in the key
	keyNoRepeated = ""
	for letter in key:
		if letter not in keyNoRepeated:
			keyNoRepeated = keyNoRepeated + letter
	#We add all the other letters to the keyNoRepeated string
	for letters in allLetters:
		if letters not in keyNoRepeated:
			keyNoRepeated = keyNoRepeated + letters
	matrixCharacters = list(keyNoRepeated)
	#Upper to all letters in matrixCharacters
	for i in range(len(matrixCharacters)):
		matrixCharacters[i] = matrixCharacters[i].upper()
	while matrixCharacters != []:
		playfairMatrix.append(matrixCharacters[:5])
		matrixCharacters = matrixCharacters[5:]
	return playfairMatrix

#Entrada: Una matriz de cualquier tamaño
#Procesamiento: Imprime de manera clara los elementos de una matriz
#Salida: Matriz en consola
def printMatrix(matrix):
	for row in matrix:
		print(*row, sep = " ")

#Entrada: Un mensaje a encriptar como texto plano
#Procesamiento: En caso de existir dos palabras iguales seguidas en el mensaje, se agrega una x entre ellas
#Salida: Mensaje con una x entre los caracteres consecutivos repetidos
def separateIdentical(message):
	iterator = 0
	modifiedMessage = ""
	while(iterator < len(message)):
		modifiedMessage = modifiedMessage + message[iterator]
		if (iterator == len(message) - 1):
			break
		elif (message[iterator] == message[iterator+1]):
			modifiedMessage = modifiedMessage + "x"
		iterator = iterator + 1
	return modifiedMessage

#Entrada: Un mensaje a encriptar como texto plano
#Procesamiento: Modifica un mensaje agregando x entre caracteres o agregando una x al final
#para pares de caracteres que queden de largo 1, reemplaza las j por i y separa los caracteres
#en pares
#Salida: Lista con el mensaje separado en pares de caracteres
def modifyWord(message):
	size = 2
	message = separateIdentical(message)
	newMessage = [message[i:i+size] for i in range(0, len(message), size)]
	for letters in newMessage:
	 	#Replace j -> i
		if ("j" in letters):
			newMessage = [letters.replace('j', 'i') for letters in newMessage]
		#Now we add x to single letters 
		if len(letters) < 2:
			old = letters
			new = letters + "x"
			newMessage = [letters.replace(old,new) for letters in newMessage]
	#Upper to all letters in newMessage
	for i in range(len(newMessage)):
		newMessage[i] = newMessage[i].upper()
	return newMessage

#Entrada: Una letra en particular y la matriz para el cifrado Playfair
#Procesamiento: Recorre la matriz buscando la letra y la almacena en una lista
#Salida: Lista con la ubicacion de la letra en la matriz del cifrado Playfair
def findInMatrix(letter,playfairMatrix):
	rowIterator = 0;
	columnIterator = 0;
	rows = 5;
	columns = 5;
	ubication = []
	while(rowIterator < rows):
		while(columnIterator < columns):
			if letter == playfairMatrix[rowIterator][columnIterator]:
				ubication.append(rowIterator);
				ubication.append(columnIterator);
			columnIterator = columnIterator + 1
		columnIterator = 0
		rowIterator = rowIterator + 1
	return ubication

#Entrada: Lista con el mensaje separado en pares de caracteres y la matriz de cifrado Playfair
#Procesamiento: Encripta los pares de caracteres en base a las reglas del cifrado Playfair
#Salida: Palabra encriptada utilizando cifrado Playfair con llave utilizada al crear la matriz
def encrypt(modifyMessage,playfairMatrix):
	encrypted = ""
	for pairLetters in modifyMessage:
		positions = []
		#Get the index
		for letter in pairLetters:
			positions.append(findInMatrix(letter,playfairMatrix))
		#Rules
		#Rule 1: If m1 and m2 are in the same row -> c1 and c2 located on the right (circular)
		if positions[0][0] == positions[1][0]:
			positions[0][1] = positions[0][1] + 1
			positions[1][1] = positions[1][1] + 1
			a = positions[0][0]
			b = positions[0][1]
			c = positions[1][0]
			d = positions[1][1]
			#Index validation
			if a == 5:
				a = 0
			elif b == 5:
				b = 0
			elif c == 5:
				c = 0
			elif d == 5:
				d = 0
			encrypted = encrypted + playfairMatrix[a][b]
			encrypted = encrypted + playfairMatrix[c][d]
			
		#Rule 2: If m1 and m2 are in the same column -> c1 and c2 located under (circular)
		if positions[0][1] == positions[1][1]:
			positions[0][0] = positions[0][0] + 1 
			positions[1][0] = positions[1][0] + 1
			a = positions[0][0]
			b = positions[0][1]
			c = positions[1][0]
			d = positions[1][1]
			#Index validation
			if a == 5:
				a = 0
			elif b == 5:
				b = 0
			elif c == 5:
				c = 0
			elif d == 5:
				d = 0
			encrypted = encrypted + playfairMatrix[a][b]
			encrypted = encrypted + playfairMatrix[c][d]

		#Rule 3: If m1 and m2 are in different row and column -> c1 and c2 opposite diagonal
		if (positions[0][0] != positions[1][0]) and (positions[0][1] != positions[1][1]):
			old = positions[0][1]
			positions[0][1] = positions[1][1] 
			positions[1][1] = old
			a = positions[0][0]
			b = positions[0][1]
			c = positions[1][0]
			d = positions[1][1]
			encrypted = encrypted + playfairMatrix[a][b]
			encrypted = encrypted + playfairMatrix[c][d]
	return encrypted	


#Funcionamiento original
key = input("Ingrese la clave para el cifrado playfair: ")
word = input("Ingrese la palabra a encriptar: ")
matrix = createMatrix(key)
modifiedWord= modifyWord(word)
encryptedText = encrypt(modifiedWord,matrix)
print("La palabra "+word+" encriptada en cifrado Playfair con llave "+key+" es: "+encryptedText)

#Funcionamiento de pruebas
#key = "monarchy"
#matriz = createMatrix(key)
#palabra = "maximiliano"
#A = modifyWord(palabra)
#encryptedText = encrypt(modifiedWord,matrix)
#print(A)
#ubicacion = findInMatrix("X",matriz)
#printMatrix(matriz)
#print(ubicacion)
#encrypt(A,matriz)