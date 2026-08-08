frase = "motor aceite motor freno aceite motor"

palabras = frase.split()

conteos = {}

for palabra in palabras:
    if palabra in conteos:
        conteos[palabra] = conteos[palabra] + 1
    else:
        conteos[palabra] = 1

for palabra in conteos:
    print(palabra, conteos[palabra])

print(len(palabras))
print(len(conteos))
print(conteos["motor"])