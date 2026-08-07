porcentajes = {
    "Consulta" : 0.5,
    "Procedimiento" : 0.3,
    "Imagenología" : 0.4,
}

pvp = 15.00

area = "Ecografía"

porcentaje = porcentajes[area]

honorario = pvp * porcentaje

if area in porcentajes:
    print(honorario)
else: 
    print("Área no econtrada")