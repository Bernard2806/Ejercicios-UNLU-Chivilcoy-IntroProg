# Clase: 8/4/2026

# Ejercio: Realizar tabla de multiplicar del 3

# Forma rapida

for i in range(1, 11):
    print(f"3 * {i} = {i * 3}")

# Forma entendible

numero = 3

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} * {multiplicador} = {resultado}")

# Forma rara
for i in range(3, 0 , 31):
    print(i)