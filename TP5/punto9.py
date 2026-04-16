numero_1 = float(input("Ingrese el numerador: "))
numero_2 = float(input("Ingrese el denominador: "))

if numero_2 == 0:
    print("No se puede dividir por 0!")
else:
    resultado = numero_1 / numero_2
    print(f"Resultado: {resultado}")