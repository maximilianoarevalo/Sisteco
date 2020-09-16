# Playfair Cipher

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

def printMatrix(matrix):
	for row in matrix:
		print(*row, sep = " ")

def modifyWord(message):
	size = 2
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


#Funcionamiento original
#key = input("Ingrese la clave para el cifrado playfair: ")
#word = input("Ingrese la palabra a encriptar: ")
#matrix = createMatrix(key)
#modifiedWord= modifyWord(palabra)
key = "monarchy"
matriz = createMatrix(key)
palabra = "maximiliano"
A = modifyWord(palabra)
print(A)