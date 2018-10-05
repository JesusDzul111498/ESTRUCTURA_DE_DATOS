print ("Verificar si la palabra ingresada es un polindromo\n")
palabra= input("Ingresa la palabra a verificar: ")

palabra_sin_espacios = palabra.replace(" ","")

def palindromo(string):
	if len(string)<=1:
		return True
	else:
		return string[0] == string[-1] and palindromo(string[1: -1])

if palindromo(palabra_sin_espacios) == True:
	print("LA FRASE: \""+str(palabra)+"\" SI ES UN PALINDROMO")
else:
	print("LA FRASE: \""+str(palabra)+"\" NO ES UN PALINDROMO")