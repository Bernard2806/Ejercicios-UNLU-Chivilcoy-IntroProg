parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))

promedio = (parcial1 + parcial2) / 2

if parcial1 >= 4 and parcial2 >= 4:
        if promedio >= 7:
            print("Situación: Promovido")
        else:
            print("Situación: Regular (debe rendir final)")
else:
    print("Situación: Libre")

print("Promedio:", promedio)