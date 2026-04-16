import sys


def main(args):
    # Constantes
    cantidad_de_dias = 10
    
    # Indicadores
    primero_que_no_jugo = None
    cantidad_no_jugo = 0
    cantidad_jugo_mas_de_5hs = 0
    horas_pantalla = 0

    for i in range(1, cantidad_de_dias + 1):
        cantidad_horas = int(input("Ingrese la cantidad de hs de juego:"))
        horas_pantalla += cantidad_horas

        if(primero_que_no_jugo == None and cantidad_horas == 0):
            primero_que_no_jugo = i
            cantidad_no_jugo = 1
        elif(cantidad_horas > 5):
            cantidad_jugo_mas_de_5hs += 1
        elif(cantidad_horas == 0):
            cantidad_no_jugo += 1
    
    # Outputs

    if(primero_que_no_jugo != None and primero_que_no_jugo > 0):
        print(f"El primer día que jugo 0 horas fue en el dia {primero_que_no_jugo}")
    
    if(cantidad_jugo_mas_de_5hs > 0): 
        print(f"Jugo más de 5 horas {cantidad_jugo_mas_de_5hs} días")
    
    if(cantidad_horas > 0 and cantidad_de_dias > 0):
        promedio = horas_pantalla / cantidad_de_dias
        print(f"Promedio de horas del niño frente a la pantalla: {promedio}")

    if(promedio < 3 or cantidad_no_jugo > 1):
        print("El niño no se excede en sus horas de juego")
        return False
    else:
        print("Demasiadas horas frente a la pantalla")
        return True

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))