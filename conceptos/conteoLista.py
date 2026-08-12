frase = "motor aceite motor freno aceite motor"

palabras = frase.split()

encontradas = []
conteos = []

for palabra in palabras:
    posicion = -1
    for i in range(len(encontradas)):
        if encontradas[i] == palabra:
            posicion = i
    if posicion == -1:
        encontradas.append(palabra)
        conteos.append(1)
    else:
        conteos[posicion] = conteos[posicion] + 1

for i in range(len(encontradas)):
    print(encontradas[i], conteos[i])

print(len(palabras))
print(len(conteos))