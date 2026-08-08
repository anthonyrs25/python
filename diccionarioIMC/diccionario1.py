menu = {"1":"Agregar persona", "2":"Agregar datos", "3":"Mostrar IMC", "4":"Salir"}

while True:

    print("="*10, " M E N Ú ", "="*10)

    for numero, texto in menu.items():
        print(numero, texto)

    eleccion = input("Marca un número: ")

    if eleccion == "4":
        print("VUELVE PRONTO")
        break

    elif eleccion in menu:
        print(menu[eleccion])

    else:
        print("Opción no válida")

    print("="*31)
    print("="*31)