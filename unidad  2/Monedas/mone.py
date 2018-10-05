print ("DETERMINAR EL CAMBIO")

costo = int(input("Cuanto es lo que costo lo que compro lo que compro\n"))
pago = int(input("Digite la cantidad de dinero con lo que usted pago\n"))
dinero = pago-costo
def cambio(cam):
	if cam == 0:
		print ("0 pesos")
	else:
		if cam >= 200:
			print ("Un Billete de 200 mas")
			return cambio(cam-200)
		elif cam >= 100:
			print ("Un Billete de 100 mas")
			return cambio(cam-100)
		elif cam >= 50:
			print("Un Billete de 50 mas")
			return cambio(cam-50)
		elif cam >= 20:
				print ("Un Billete de 20 mas")
				return cambio(cam-20)
		elif cam >= 10:
			print ("Una moneda de 10 mas")
			return cambio(cam-10)
		elif cam >= 5:
			print("Una moneda de 5 mas")
			return cambio(cam-5)
		elif cam >= 2:
			print("Una moneda de 2 mas")
			return cambio(cam-2)
		elif cam >= 1:
			print("Una moneda de 1 mas")
			return cambio(cam-1)
	

	

	

print(cambio(dinero))
print ("Su cambio es : "+str(dinero))

"""
Dzul Canul Jesus Geovany 
Coba Kauil Luis Enrique
Camacho Reyes Hector Alejandro
Kauil Dzib Alexis Eliseo
"""





