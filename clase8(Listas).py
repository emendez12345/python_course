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
busquedaMayor=("Mayor",max(numbers5))
print(busquedaMayor)
busquedaMenor=("Menor",min(numbers5))
print(busquedaMenor)
