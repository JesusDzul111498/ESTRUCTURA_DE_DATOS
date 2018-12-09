class operations:

    def __init__(self, reed_file1, reed_file2):
        self.file_1 = reed_file1
        self.file_2 = reed_file2
        self.file_3_array = []
#IMPRESION DE LOS ARCHIVOS
    def print_files(self):
        print("FILE 1:\n", *self.file_1)
        print("FILE 2:\n", *self.file_2)
#SE ORDENAN PREVIAMENTE LOS ARCHIVOS
    def bubble(self):
        for i in range(len(self.file_1)-1,0,-1):
            for j in range(i):
                if self.file_1[j]>self.file_1[j+1]:
                    aux = self.file_1[j]
                    self.file_1[j] = self.file_1[j+1]
                    self.file_1[j+1] = aux
        print("ORDERED FILE 1:\n",self.file_1)

        for i in range(len(self.file_2)-1,0,-1):
            for j in range(i):
                if self.file_2[j]>self.file_2[j+1]:
                    aux = self.file_2[j]
                    self.file_2[j] = self.file_2[j+1]
                    self.file_2[j+1] = aux
        print("ORDERED FILE 2:\n",self.file_2)

#METODO DE INTERCALACION
    def order_method(self):
        mov=0
        com=0
        i=0
        j=0
        while i<len(self.file_1) and j<len(self.file_2):
            com+=1
            if self.file_1[i]<self.file_2[j]:
                self.file_3_array.append(self.file_1[i])
                i+=1
                mov+=1
            else:
                self.file_3_array.append(self.file_2[j])
                j+=1
                mov+=1
        while i<len(self.file_1):
            self.file_3_array.append(self.file_1[i])
            i+=1
            mov+=1
        while j<len(self.file_2):
            self.file_3_array.append(self.file_2[j])
            j+=1
            mov+=1

        print("MOVES: ",mov)
        print("comparisons: ",com)

#IMPRIME EL NUEVO ARRAY
    def new_file(self):
        return  self.file_3_array

