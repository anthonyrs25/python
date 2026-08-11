def cedulaValida(cedula):
    if len(cedula) == 10 and cedula.isdigit():
        return True
    else:
        return False

ejemplo1 = cedulaValida("0102030405")
print(ejemplo1)

ejemplo2 = cedulaValida("abc")
print(ejemplo2)

ejemplo3 = cedulaValida("09876543211234567890")
print(ejemplo3)

ejemplo4 = cedulaValida("0099887766")
print(ejemplo4)