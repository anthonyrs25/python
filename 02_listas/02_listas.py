servicios = ["Consulta", "Ecografía", "Hemograma"]

print(servicios[0]) # primero de la lista

print(servicios[-1]) # último de la lista (contar hacia atrás)

print(len(servicios)) # cuántos ítems hay en la lista

# agregar al final
servicios.append("Radiografía")
print(servicios)

# quitar
servicios.remove("Ecografía")
print(servicios)

servicios.remove(servicios[0])
print(servicios)

# ¿Está en la lista? True/False
print("Consulta" in servicios)
print("Hemograma" in servicios)

# reemplazar / sobreescribir
servicios[1] = "Otro"
print(servicios)


### Listas de números ###

precios = [2,5,9,10,1,-3]

# sumar sum()
print(sum(precios))

# el más caro / mayor max()
print(max(precios))

# el más barato / menor
print(min(precios))

# odenados de menor a mayor sorted()
print(sorted(precios))