menu = {"1":"Agregar persona", "2":"Agregar datos", "3":"Mostrar IMC", "4":"Salir"}

personas = {
    "0102030405": {"nombre": "Juan Pérez", "peso": 70.0, "estatura": 1.80},
    "0011223344": {"nombre": "Pedro Sánchez"},
}

def cedulaValida(cedula):
    if len(cedula) == 10 and cedula.isdigit():
        return True
    else:
        return False

def calcularIMC(peso, estatura):
    return round(peso / (estatura ** 2), 2)

salir = False 

while True:

    print("="*5, " M E N Ú ", "="*5)
    
    for numero, texto in menu.items():
        print(numero, texto)

    eleccion = input("Marca un número: ")

    # Opción 4: Salir
    if eleccion == "4":
        print("VUELVE PRONTO")
        salir = True

    # Opción 1: Agregar personas
    elif  eleccion == "1":
            cedula = input("Ingresa el número de cédula de 10 dígitos: ")
            while not cedulaValida(cedula):
                cedula = input("Ingresa una cédula válida: ")
            if cedula in personas:
                print("La persona ya está registrada")
                print("Persona: ", personas[cedula]["nombre"])
            else:
                print("La persona no está registrada")
                registrar = input("Registra el nombre: ")
                personas[cedula] = {"nombre": registrar}
                print(personas)

    # Opción 2: Agregar datos
    elif eleccion == "2":
            cedula = input("Ingresa el número de cédula de 10 dígitos: ")
            while not cedulaValida(cedula):
                cedula = input("Ingresa una cédula válida: ")
            if cedula in personas:
              print(personas[cedula]["nombre"])
              print("Agregue los datos: ")
              peso = float(input("Peso en kilogramos: "))
              estatura = float(input("Estatura en metros: "))
              print(personas[cedula])
              personas[cedula]["peso"] = peso
              personas[cedula]["estatura"] = estatura
              print(personas[cedula])
             
            else:
                print("="*30)
                print("Primero registra a la persona en la Opción 1")

    # Opción 3: Mostrar IMC
    elif eleccion == "3":
        cedula = input("Ingresa el número de cédula de 10 dígitos: ")
        while not cedulaValida(cedula):
            cedula = input("Ingresa una cédula válida: ")
        if cedula in personas:
            if "peso" in personas[cedula] and "estatura" in personas[cedula]:
                print(personas[cedula]["nombre"],personas[cedula]["peso"],personas[cedula]["estatura"])
                print("El Índice de Masa Corporal de ", personas[cedula]["nombre"], " es: ")
                resultado = calcularIMC(personas[cedula]["peso"],personas[cedula]["estatura"])
                print(resultado)
            else:
                print("="*30)
                print("Agrega el peso y estatura en la Opción 2")
        else:
            print("="*30)
            print("La persona no está registrada. Agrega la persona en la Opción 1")

    else:
        print("Opción no válida")

    print("="*20)

    if salir:
        break