# Pedimos al usuario que ingrese la base y el exponente
base = 2
exponente = 5

# ------------------------------------------------------------
# Opción 1: Usar el operador **
resultado = base ** exponente
print(f"El numero {base} elevado a la potencia {exponente} es {resultado}")

# ------------------------------------------------------------
# Opción 2: Usar la función pow()
resultado = pow(base, exponente)
print(f"El numero {base} elevado a la potencia {exponente} es {resultado}")

# ------------------------------------------------------------
# Opción 3: Calcular manualmente con un bucle for
resultado = 1
for i in range(exponente):
    resultado *= base
print(f"El numero {base} elevado a la potencia {exponente} es {resultado}")

# ------------------------------------------------------------
# Opción 5: Usar recursividad
def potencia(b, e):
    if e == 0:
        return 1
    else:
        return b * potencia(b, e - 1)

resultado = potencia(base, exponente)
print(f"El numero {base} elevado a la potencia {exponente} es {resultado}")