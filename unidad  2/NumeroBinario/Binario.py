num = int(input("Digital el numero a covertir a binario"))

def binario(bi):
	if bi == 0:
		return ""
	else:
		return str(bi%2) + str (binario(bi//2))

print (binario(num))
