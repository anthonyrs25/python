porcentajes = {"consulta": 0.50, "Laboratorio": 0.30, "imagenologia": 0.40}

pvp = 25.00
area = "consulta"

porcentaje = porcentajes[area]
honorario = pvp * porcentaje

print("PVP:", pvp)
print("Área:", area)
print("Porcentaje:", porcentaje)
print("Le toca al médico:", honorario)