# Pedir un número entre 0 y 255
numero = int(input("Ingrese un número del 0 al 255: "))

if numero < 0 or numero > 255:
    print("El número ingresado está fuera del rango permitido.")
else:
    binario = bin(numero)[2:]
    print(f"El Binario de {numero} es: {binario}")