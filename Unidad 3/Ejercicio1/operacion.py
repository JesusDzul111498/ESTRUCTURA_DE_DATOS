class pila:

    def __init__(self,n):
        self.cola=([])
        self.pila=[]
        self.n=n

    def apilar(self):
        while self.n != "":
            self.pila+=[self.n]
            print("otro elemento")
            self.n=input()
        print("La pila tiene valores de: ", *self.pila)


    def desapilar(self):
        for self.n in self.pila[::-1]:
            self.cola+=[self.n]
        return self.cola


class cola():

    def __init__(self,items):
        self.cola=[]
        self.cola = items

    def desencolar(self):
        self.cola.sort()
        if len(self.cola) != 0:
            print(*self.cola)
            print("presionar 1, para eliminar,y un enter mas")
            j=input()
            for i in self.cola:
                if j=="1":
                    self.cola.remove(i)
                    j=input()
            return self.cola
        else:
            print("cola vacia")

    def mostrar(self):
        return self.cola

    def es_vacio(self):
        return self.cola==[]