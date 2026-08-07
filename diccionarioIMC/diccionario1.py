diccionario = {"1":"Opción 1", "2":"Opción 2", "3":"Opción 3", "4":"Opción 4"}

# print(diccionario)

for opcion in diccionario.values():
    print(opcion)

eleccion = input("Marca un número")

if eleccion == 1:
    print(diccionario.values([eleccion]))

else:
    print("Opción no válida")