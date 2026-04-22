# Ejemplo inicial
a = 10
b = 5

print(f"Valores iniciales: a = {a}, b = {b}")

# ------------------------------------------------------------
# Opción 1: Asignación múltiple
a, b = b, a
print(f"[Opción 1] Después del intercambio: a = {a}, b = {b}")

# ------------------------------------------------------------
# Opción 2: Usar una variable auxiliar
a = 10
b = 5
aux = a
a = b
b = aux
print(f"[Opción 2] Después del intercambio: a = {a}, b = {b}")

# ------------------------------------------------------------
# Opción 3: Usar operaciones aritméticas (sin variable auxiliar)
a = 10
b = 5
a = a + b
b = a - b
a = a - b
print(f"[Opción 3] Después del intercambio: a = {a}, b = {b}")

# ------------------------------------------------------------
# Opción 4: Usar operaciones XOR (bitwise)
a = 10
b = 5
a = a ^ b
b = a ^ b
a = a ^ b
print(f"[Opción 4] Después del intercambio: a = {a}, b = {b}")

# ------------------------------------------------------------
# Opción 5: Usar una función
def intercambiar(x, y):
    return y, x

a, b = intercambiar(10, 5)
print(f"[Opción 5] Después del intercambio: a = {a}, b = {b}")
