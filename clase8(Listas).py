# numbers=[1,2,3,4,'cinco']
# print(type(numbers))
# print(len(numbers))
# print("ultimo elemento",numbers[-1])
# print(numbers[-1][2:5])

#Agregar una lista dentro de otra lista
#listas
numbers2=[10,20,30,40,50,60]
numbers3=[100,500,350,'Siuuu']
numbers4=[2500,9800,15000]
numbers5=[10,20,30,40,50,60]
list=[890,5,4,1054,789]
list2=[210,3,2,1,897814]
#procesos
# append:Enlaza la lista 
numbers2.append(numbers3)
listaEnlazada='Lista enlazada:',numbers2
print(listaEnlazada)
# insert: Inserta la lista en la posición que quiera
numbers3.insert(3,numbers4)
insertarEnlista='Inserta la lista en la posición que necesita:',numbers3
print(insertarEnlista)
# index: Busca en la lista
busquedaEnposicion='Busca la posición en la lista:',numbers3.index('Siuuu')
print(busquedaEnposicion)
# max and mix in the numbers
busquedaMayor=("Numero mayor",max(numbers5))
print(busquedaMayor)
busquedaMenor=("Numero menor",min(numbers5))
print(busquedaMenor)
# delete list
del(list[-1])
eliminarList=("Lista con registro eliminado",[list])
print(eliminarList)
del(list[0:3])
eliminarListRango1=("Lista con rango de registro eliminado",[list])
print(eliminarListRango1)
del(list2[3:5])
eliminarListRango2=("Lista con rango de registro eliminado",[list2])
print(eliminarListRango2)


