from operacion import *

regalos=["playera","gorra","camara","reloj","suscripcion de spotify","suscripcion a amazon",
         "tarjetas de google play","memoria usb"," suscripcion a revista play boy :v"]


print("ACTIVIDAD TRES.-")

print("ingrese su nombre: ")
n=input()
print("ingrese su numero: ")
j=input()


pila=pila_ligada(n,j)
pila_r=pila_regalo(regalos)
pila.apilar()

print("MENU")
print("1.-imprimir lista de usuarios")
print("2.-eliminar un elemento de regalo")
print("3.-Asignar relagalo a usuario")
print("elige una opcion")
opcion_submenu=input()

if opcion_submenu =="1":
    pila.imprimir()
    print("\n")
elif opcion_submenu=="2":
    pila_r.desencolar()

elif opcion_submenu=="3":
    prototipo=estructura(pila.apilar(),regalos)
    prototipo.eliminar_repetidos()


