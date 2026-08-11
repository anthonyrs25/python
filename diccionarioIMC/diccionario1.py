menu = {"1":"Agregar persona", "2":"Agregar datos", "3":"Mostrar IMC", "4":"Salir"}

personas = {
    "0102030405": {"nombre": "Juan Pérez"},
    "0011223344": {"nombre": "Pedro Sánchez"},
}

salir = False 

while True:

    print("="*5, " M E N Ú ", "="*5)
    
    for numero, texto in menu.items():
        print(numero, texto)

    eleccion = input("Marca un número: ")

    if eleccion == "4":
        print("VUELVE PRONTO")
        salir = True

    elif  eleccion == "1": #Agregar persona
            cedula = input("Ingresa el número de cédula de 10 dígitos: ")
            while len(cedula) != 10 or not cedula.isdigit():
                cedula = input("Ingresa una cédula válida: ")
            if cedula in personas:
                print("La persona ya está registrada")
                print("Persona: ", personas[cedula]["nombre"])
            else:
                print("La persona no está registrada")
                registrar = input("Registra el nombre: ")
                personas[cedula] = {"nombre": registrar}
                print(personas)

    elif eleccion == "2":
            cedula = input("Ingresa el número de cédula: ")
            if cedula in personas:
              print(personas[cedula]["nombre"])
              print("Agregue los datos: ")
              peso = float(input("Peso en kilogramos: "))
              estatura = float(input("Estatura en metros: "))
              print(personas[cedula])
              personas[cedula]["Peso"] = peso
              personas[cedula]["Estatura"] = estatura
              print(personas[cedula])
             
            else:
                agregar = input("Registra el nombre: ")
                personas[cedula] = {"nombre": agregar}
                print(personas) 

    else:
        print("Opción no válida")

    print("="*20)

    if salir:
        break