# crear una lista vacía y agregar ítems con append. imprimir cuántos hay y cuál es el último

listaVacia = []

# agregar ítems

listaVacia.append(1)
print(listaVacia)

listaVacia.append(4)
print(listaVacia)

print(sum(listaVacia))

listaVacia.append(-10)
print(listaVacia)

print(sum(listaVacia))

# imprimir el último de la lista

print(listaVacia[-1])

# agrega un nuevo ítem que es una lista .append

listaVacia.append([2,7,9])
print(listaVacia)
print(len(listaVacia)) # len = 4 ítems

# agregar nuevos ítems .extend

listaVacia.extend([-4,8,11])
print(listaVacia)
print(len(listaVacia)) # len = 7 ítems