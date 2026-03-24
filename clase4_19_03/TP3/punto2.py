# Pedimos al usuario que ingrese su nombre de pila
nombre_de_pila = "Bernardo"

# ------------------------------------------------------------
# Opción 1: Usar len() directamente
cantidad_de_letras = len(nombre_de_pila)
print(f"El nombre {nombre_de_pila} tiene {cantidad_de_letras} letras.")

# ------------------------------------------------------------
# Opción 2: Contar manualmente con un bucle for
contador = 0
for letra in nombre_de_pila:
    contador += 1
print(f"El nombre {nombre_de_pila} tiene {contador} letras.")

# ------------------------------------------------------------
# Opción 3: Usar comprensión de listas y sum()
cantidad_de_letras = sum([1 for letra in nombre_de_pila])
print(f"El nombre {nombre_de_pila} tiene {cantidad_de_letras} letras.")

# ------------------------------------------------------------
# Opción 4: Usar map() y sum()
cantidad_de_letras = sum(map(lambda x: 1, nombre_de_pila))
print(f"El nombre {nombre_de_pila} tiene {cantidad_de_letras} letras.")

# ------------------------------------------------------------
# Opción 5: Usar while con slicing
i = 0
while nombre_de_pila[i:i+1] != "":
    i += 1
print(f"El nombre {nombre_de_pila} tiene {i} letras.")