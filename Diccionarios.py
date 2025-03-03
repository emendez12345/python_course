# #Ejemplo1
# numbers={1:"uno",2:"dos",3:"tres"}
# print(numbers)
# print(numbers[1])
#Ejemplo2
contacts={"Edwin":{"Apellido":"Mendez",
                   "Edad":"34"},
          "Mariana":{"Apellido":"Piedrahita",
                     "Edad":"20"}}
# del contacts['Edwin']
del contacts["Mariana"]['Edad']
print(contacts)
claves=contacts.keys()
print(claves)