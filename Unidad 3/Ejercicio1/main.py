from operacion import *

print("ACTIVIDAD DOS.-")

print("ingrese un elemento")
n=input()

pila=pila(n)
cola=cola(pila.desapilar())
pila.apilar()
print("los datos se han traspasado")
print("la cola tiene los elementos de :", *pila.desapilar())

print("quiere verificar que si es una pila: ")
print("si/no")
opcion=input()

if opcion=="si":
    print("MENU COLA")
    print("1.- Desencolar")
    print("2.-Verificar si es vacia")
    opcion_submenu=input("elige una opcion")
    if opcion_submenu=="1":
        cola.desencolar()
        print("elementos de la cola: ", *cola.mostrar())
    elif opcion_submenu=="2":
        print(cola.es_vacio())
    else:
        print("opcion incorrecta...")


elif opcion=="no":
    print("EL PROGRAMA HA FINALIZADO...")

else:
    print("solo se permite si o no")