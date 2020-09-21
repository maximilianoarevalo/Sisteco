## Playfair Cipher ##

import time
import matplotlib.pyplot as plt

#Entrada: Una palabra que representa la llave para encriptar y desencriptar
#Procesamiento: En base a la llave se crea una matriz de 5x5 donde se ingresan las letras
#Salida: Matriz para el cifrado playfair con la llave ingresada
def createMatrix(key):
	rows = 5
	columns = 5
	playfairMatrix = []
	key = key.replace(" ", "")
	#Define all leters without the j
	allLetters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#Now we remove the repeated letters in the key
	keyNoRepeated = ""
	for letter in key:
		if letter not in keyNoRepeated:
			keyNoRepeated = keyNoRepeated + letter
	#Now we add all the other letters to the keyNoRepeated string
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
	message = message.replace(" ", "")
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

#Entrada: Lista con el mensaje encriptado separado en pares de caracteres y la matriz de cifrado Playfair
#Procesamiento: Desencripta los pares de caracteres en base a las reglas del cifrado Playfair
#Salida: Palabra desencriptada utilizando cifrado Playfair con llave utilizada al crear la matriz
def decrypt(encriptedMessage, key):
	message = [encriptedMessage[i:i+2] for i in range(0, len(encriptedMessage), 2)]
	decrypted = ""
	playfairMatrix = createMatrix(key)
	for pairLetters in message:
		positions = []
		#Get the index
		for letter in pairLetters:
			positions.append(findInMatrix(letter,playfairMatrix))
		#Rules
		#Rule 1: If m1 and m2 are in the same row -> c1 and c2 located on the right (circular)
		if positions[0][0] == positions[1][0]:
			positions[0][1] = positions[0][1] - 1
			positions[1][1] = positions[1][1] - 1
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
			decrypted = decrypted + playfairMatrix[a][b]
			decrypted = decrypted + playfairMatrix[c][d]
			
		#Rule 2: If m1 and m2 are in the same column -> c1 and c2 located under (circular)
		if positions[0][1] == positions[1][1]:
			positions[0][0] = positions[0][0] - 1 
			positions[1][0] = positions[1][0] - 1
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
			decrypted = decrypted + playfairMatrix[a][b]
			decrypted = decrypted + playfairMatrix[c][d]

		#Rule 3: If m1 and m2 are in different row and column -> c1 and c2 opposite diagonal
		if (positions[0][0] != positions[1][0]) and (positions[0][1] != positions[1][1]):
			old = positions[0][1]
			positions[0][1] = positions[1][1] 
			positions[1][1] = old
			a = positions[0][0]
			b = positions[0][1]
			c = positions[1][0]
			d = positions[1][1]
			decrypted = decrypted + playfairMatrix[a][b]
			decrypted = decrypted + playfairMatrix[c][d]
	return decrypted

#Entrada: No tiene entrada directa, se solicitan por consola
#Procesamiento: Encripta una palabra utilizando cifrado Playfair con una determinada llave
#Salida: Palabra encriptada utilizando cifrado Playfair con llave utilizada al crear la matriz
def playfairCrypt():
	encryptKey = input("Ingrese la clave para el cifrado Playfair: ")
	word = input("Ingrese la palabra a encriptar: ")
	matrix = createMatrix(encryptKey)
	modifiedWord= modifyWord(word)
	encryptedText = encrypt(modifiedWord,matrix)
	print("")
	print("La palabra "+word+" encriptada en cifrado Playfair con llave "+encryptKey+" es: "+encryptedText)

#Entrada: No tiene entrada directa, se solicitan por consola
#Procesamiento: Desencripta una palabra utilizando cifrado Playfair con una determinada llave
#Salida: Palabra desencriptada utilizando cifrado Playfair con llave utilizada al crear la matriz
def playfairDecrypt():
	decryptKey = input("Ingrese la clave para desencriptar en cifrado Playfair: ")
	cryptedWord = input("Ingrese la palabra encriptada en cifrado Playfair: ")
	realWord = decrypt(cryptedWord,decryptKey)
	print("")
	print("La palabra "+cryptedWord+" desencriptada en cifrado Playfair con llave "+decryptKey+" es: "+realWord)	

def graphPlot(title, x, y, xlabel, ylabel):
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=5)
	plt.show()

#Entrada: Dos mensajes a encriptar, idealmente con un bit de diferencia y la llave de encriptacion
#Procesamiento: Encripta dos mensajes en base a una llave común y muestra los resultados de encriptación como palabra y bits
#Salida: Mensajes encriptados en formato de caracteres y en formato de bits
def avalancheTest(message1,message2,key):
	m1 = message1
	bitsm1 = ' '.join(format(x, 'b') for x in bytearray(m1, 'utf-8'))
	m2 = message2
	bitsm2 = ' '.join(format(x, 'b') for x in bytearray(m2, 'utf-8'))
	#For the first message, example: "hola"
	matrix1 = createMatrix(key)
	modifiedM1 = modifyWord(m1)
	encryptedM1 = encrypt(modifiedM1,matrix1)
	out1 = ' '.join(format(x, 'b') for x in bytearray(m1, 'utf-8'))
	print("La palabra "+m1+" encriptada con llave "+key+" tiene como resultado "+encryptedM1+", cuyos bits son: "+out1)
	#For the second message, example: "hole"
	matrix2 = createMatrix(key)
	modifiedM2 = modifyWord(m2)
	encryptedM2 = encrypt(modifiedM2,matrix2)
	out2 = ' '.join(format(x, 'b') for x in bytearray(m2, 'utf-8'))
	print("La palabra "+m2+" encriptada con llave "+key+" tiene como resultado "+encryptedM2+", cuyos bits son: "+out2)

#Entrada: No tiene entrada directa, se solicitan por consola
#Procesamiento: Encripta o desencripta palabras utilizando cifrado Playfair
#Salida: Palabra encriptada o desencriptada utilizando cifrado Playfair
def menu():
	#Block size is 16 bytes, because the characters of the message are grouped in pairs
	#The thoughput must be in Kilobytes, so the block size is 0.015625 Kilobytes
	print("### Cifrado Playfair ###")
	print("Considere que ni la llave ni el mensaje pueden contener números debido a la naturaleza del encriptado Playfair")
	print("Seleccione una de las siguientes opciones: ")
	print("1. Encriptar")
	print("2. Desencriptar")
	print("3. Salir")
	opcion = input("Ingrese su opción: ")
	off = False
	blockSize = 0.015625
	while not off:
		if opcion == "1":
			#Playfair encrypt
			start_time = time.time()
			playfairCrypt()
			end_time = time.time()
			encryptTime = end_time - start_time
			throughput = blockSize / encryptTime
			print("El tiempo de encriptación es de: "+str(encryptTime)+" segundos y el Throughput es: "+str(throughput))
			graphPlot("Throughput V/S Tamaño de bloque de mensaje para encriptación", throughput, blockSize, "Throughput","Tamaño de bloque [Kilobytes]")
			off = True
		elif opcion == "2":
			#Playfair decrypt
			start_time = time.time()
			playfairDecrypt()
			end_time = time.time()
			decryptTime = end_time - start_time
			throughput = blockSize / decryptTime
			print("El tiempo de desencriptación es de: "+str(decryptTime)+" segundos y el Throughput es: "+str(throughput))
			graphPlot("Throughput V/S Tamaño de bloque de mensaje para desencriptación", throughput, blockSize, "Throughput","Tamaño de bloque [Kilobytes]")
			off = True
		elif opcion == "3":
			off = True
			print("Hasta luego")
		else:
			print("Por favor, ingrese una opción valida")
			print(" ")
			menu()

#Cifrado Playfair
menu()
#Just test for the avalanche effect
#avalancheTest("hola","hole","clave")