porcentajes = {"consulta": 0.50, "Laboratorio": 0.30, "imagenologia": 0.40}

pvp = 25.00
area = "consulta"

porcentaje = porcentajes[area] #porcentajes["consulta"]
honorario = pvp * porcentaje

print("PVP:", pvp)
print("Área:", area)
print("Porcentaje:", porcentaje)
print("Le toca al médico:", honorario)

porcentajes["nuevo"] =0.0
print(porcentajes)