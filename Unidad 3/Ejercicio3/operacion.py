class pila_ligada:

    def __init__(self,n,j):
        self.nombres=[]
        self.contacto=[]
        self.n=n
        self.j=j

    def apilar(self):

        while self.n and self.j != "":
            self.nombres+=[self.n]
            print("otro nombre")
            self.n=input()
            self.contacto+=[self.j]
            print("otro numero: ")
            self.j=input()
        return self.nombres

    def imprimir(self):
        contador=1
        for n, j in zip(self.nombres,self.contacto):
            print("\t ",contador)
            print("nombre:",n)
            print("numero:", j)
            contador=contador+1



class pila_regalo:

    def __init__(self,regalo):
        self.regalos=[]
        self.regalos=regalo

    def mostrar(self):
        for i in self.regalos:
            print(i)

    def desencolar(self):
        if len(self.regalos) != 0:
            print(*self.regalos)
            print("presionar 1, para eliminar,y un enter mas")
            j=input()
            for i in self.regalos:
                if j=="1":
                    self.regalos.remove(i)
                    j=input()
            return self.regalos
        else:
            print("cola vacia")

class estructura:

    def __init__(self,nombre,regalos):
        self.nombre_sin=[]
        self.nombre_sin=nombre
        self.regalos=[]
        self.regalos=regalos
        self.nombre=[]

    def eliminar_repetidos(self):
        for i in self.nombre_sin:
           if i not in self.nombre:
               self.nombre+=[i]

        for i,j in zip(self.nombre,self.regalos):
                print("el usuario: ",i, "le toca el regalo ",j)