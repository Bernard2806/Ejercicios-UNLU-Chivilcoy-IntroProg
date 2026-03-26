numero_decimal = float(input("Ingrese un numero con decimales: "))

numero_entero_cercano = round(numero_decimal)
numero_redondeado_2decimales = round(numero_decimal, 2)

print(f"Número original: {numero_decimal}")
print(f"Número entero cercano: {numero_entero_cercano}")
print(f"Número redondeado a 2 decimales: {numero_redondeado_2decimales}")