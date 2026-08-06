# ============================================================
# BUCLE FOR
# ============================================================
# PARA QUE SIRVE:
# Repetir una accion sobre cada elemento de una coleccion,
# sin importar cuantos elementos haya.
# Sin for tendrias que escribir una linea por cada elemento,
# y si los datos vienen de una base de datos ni siquiera sabes
# cuantos son.

# SINTAXIS:
#   for <nombre_que_yo_invento> in <coleccion>:
#       <lo que se repite>
#
# - "for" e "in" son palabras fijas del lenguaje
# - el nombre del medio lo invento yo; nace en esa linea,
#   no existe antes. Podria llamarse como sea.
# - los dos puntos ":" y la indentacion marcan el bloque

# COMO FUNCIONA POR DENTRO:
# La variable es UNA sola cajita que se va reemplazando.
#   vuelta 1: p = 10  -> ejecuta el bloque
#   vuelta 2: p = 20  -> ejecuta el bloque
#   vuelta 3: p = 30  -> ejecuta el bloque
#   no quedan mas     -> termina
# El bucle NO necesita condicion: termina cuando se acaban
# los elementos.

# LA INDENTACION DECIDE QUE SE REPITE:
#   dentro del bloque -> se ejecuta en cada vuelta
#   fuera del bloque  -> se ejecuta una sola vez, al final
# Los espacios reemplazan a las llaves { } de Java/C.

# COMPARADO CON JAVA:
#   Java:   for (int i = 0; i < arr.length; i++) { ... }
#   Python: for p in precios:
# En Python NO hay contador, NI condicion, NI incremento,
# NI llaves, NI punto y coma. Es equivalente al for-each de Java.
# En Java dices COMO recorrer; en Python dices QUE recorrer.

# WHILE:
# Existe en Python (con contador y condicion, como en Java).
# do-while NO existe.
# Regla practica: for para recorrer colecciones (99% de los casos),
# while cuando no sabes cuantas vueltas seran.

# RECORRER DICCIONARIOS:
#   for x in dicc:            -> solo las LLAVES
#   for x in dicc.values():   -> solo los VALORES
#   for k, v in dicc.items(): -> ambas (dos nombres, se reparten)
# OJO: values() e items() SIEMPRE llevan parentesis.
# Si usas items() con un solo nombre, recibes la pareja junta:
# ('consulta', 0.5)  <- esto se llama tupla

# TRUCO PARA LEER UN FOR QUE NO ENTIENDO:
# Escribir a mano que pasa en la vuelta 1, reemplazando la
# variable por su valor real. Luego la vuelta 2. Con dos
# vueltas ya se ve el patron.
# ============================================================