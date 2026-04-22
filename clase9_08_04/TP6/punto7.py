maximo = 0
minimo = 0
pos_max = 0
pos_min = 0

for i in range(1, 11):
    num = int(input(f"Ingrese el numero [{i}/10]: "))

    if num > maximo:
        maximo = num
        pos_max = i

    if num < minimo:
        minimo = num
        pos_min = i

print(f"El mayor numero ingresado es {maximo} y fue ingresado en la posición {pos_max}")
print(f"El menor numero ingresado es {minimo} y fue ingresado en la posición {pos_min}")