maximo = 0
posicion_max = 0

for i in range(1, 11):
    num = int(input(f"Ingrese un numero [{i}/10]: "))

    if num > maximo:
        maximo = num
        posicion_max = i

print(f"El mayor numero ingresado es {maximo} y fue ingresado en la posicion {posicion_max}")