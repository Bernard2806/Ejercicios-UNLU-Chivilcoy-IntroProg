# Clase: 8/4/2026

# Ejercio: Realizar tabla de multiplicar del 2 al 5

for numero in range(2, 6):
    print(f"=== Tabla del {numero} ===")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} * {multiplicador} = {resultado}")