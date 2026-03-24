print("Ingrese el número del que desea saber el valor absoluto:")
numero = -8

# Solución 1: Usar if/else tradicional
# Si el número es negativo, se multiplica por -1
# Si es positivo o cero, se deja igual
if numero < 0:
    valor_absoluto = -numero
else:
    valor_absoluto = numero

print(f"[Solución 1] El valor absoluto de {numero} es |{valor_absoluto}|")

# ------------------------------------------------------------
# Solución 2: Usar la función integrada abs()
# abs() devuelve directamente el valor absoluto de un número
valor_absoluto = abs(numero)

print(f"[Solución 2] El valor absoluto de {numero} es |{valor_absoluto}|")

# ------------------------------------------------------------
# Solución 3: Usar operador ternario
# En una sola línea: si el número es negativo, se niega; si no, se deja igual
valor_absoluto = -numero if numero < 0 else numero

print(f"[Solución 3] El valor absoluto de {numero} es |{valor_absoluto}|")