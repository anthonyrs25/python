porcentajes = {"consulta": 0.50, "laboratorio": 0.30, "imagenologia": 0.40}

area = "laboratorio"
print(area)                  # ¿qué hay en el papelito?
print(porcentajes[area])     # buscar eso en la guía

area = "consulta"            # cambio el papelito
print(area)
print(porcentajes[area])     # MISMA línea, distinto resultado