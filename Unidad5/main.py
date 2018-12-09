from clas import operations
from io import open
file_array1 = []
file_array2 = []

file1 = open('file1.txt', 'r')#'R' INDICA SOLO LECTURA
for i in file1.readlines():
    #SE EXTRAEN LOS ARCHIVOS Y LOS CONVIERTO  DE STRING A ENTEROS
    file_array1.append(int(i))
file1.close()

file2 = open('file2.txt', 'r')#'R' INDICA SOLO LECTURA
for n in file2.readlines():
    # SE EXTRAEN LOS ARCHIVOS Y LOS CONVIERTO  DE STRING A ENTEROS
    file_array2.append(int(n))
file2.close()

opp = operations(file_array1, file_array2)
opp.print_files()
print("\n**************************************************************")
opp.bubble()
print("\n**************************************************************")
print("----------------------------------------------------------------------------")
print("FILE COLLATION")
opp.order_method()
new_file = open("new_file.txt","w")
new = opp.new_file()

print("ORDERED FILE")
print(new)
print("SIZE FILE")
print(len(new))
print("----------------------------------------------------------------------------")
new_file.write("THE COLLATION HAS BEEN SAVED\n"+ str(new))
new_file.close()

print("THE COLLATION HAS BEEN SAVED")

