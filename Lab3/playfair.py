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

def encrypt(modifyMessage,playfairMatrix):
	encrypted = ""
	for pairLetters in modifyMessage:
		positions = []
		#Get the index
		for letter in pairLetters:
			positions.append(findInMatrix(letter,playfairMatrix))
		print(positions)
		print("New positions:")
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
			#print(positions)
			encrypted = encrypted + playfairMatrix[a][b]
			encrypted = encrypted + playfairMatrix[c][d]
			#print("Encrypted: "+encrypted)
			break;

	return encrypted		
	

	#Rule 2: If m1 and m2 are in the same column -> c1 and c2 located under (circular)

	#Rule 3: If m1 and m2 are in different row and column -> c1 and c2 opposite diagonal

	#Rule 4: If m1 = m2, add caracter between m1 and m2, and then applicate the 1-3 rules


#Funcionamiento original
#key = input("Ingrese la clave para el cifrado playfair: ")
#word = input("Ingrese la palabra a encriptar: ")
#matrix = createMatrix(key)
#modifiedWord= modifyWord(palabra)
key = "monarchy"
matriz = createMatrix(key)
palabra = "mrximiliano"
A = modifyWord(palabra)
#encryptedText = encrypt(modifiedWord,matrix)
#print(A)
#ubicacion = findInMatrix("X",matriz)
printMatrix(matriz)
#print(ubicacion)
encrypt(A,matriz)