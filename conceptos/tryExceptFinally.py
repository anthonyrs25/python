try:
    numero = float(input("Escribe un número: "))
    print("Funcionó: ", numero)
except ValueError:
    print("Eso no es un número")
finally:
    print("Terminé")