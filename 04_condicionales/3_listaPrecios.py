precios = [101, 150, 25, 30, 100]

for precio in precios:
    if precio > 125:
        print("Alto")
    elif precio >= 100:
        print("3/4")
    elif precio >= 25:
        print("Medio")
    else:
        print("Bajo")