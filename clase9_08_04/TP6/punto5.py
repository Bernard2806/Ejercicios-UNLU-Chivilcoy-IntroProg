cantidad_numero = 10


for i in range(cantidad_numero):
    num = int(input(f'Ingrese el Numero [{i + 1 }/{cantidad_numero}]: '))

    if num > 0:
        print("Es positivo")
    elif num < 0:
        print("Es negativo")
    else:
        print("Es cero")
