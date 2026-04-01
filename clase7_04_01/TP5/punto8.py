lado_1 = float(input("Ingrese el primer lado: "))
lado_2 = float(input("Ingrese el segundo lado: "))
lado_3 = float(input("Ingrese el tercer lado: "))

if(lado_1 == lado_2 and lado_2 == lado_3):
    print("El triangulo es equilatero")
elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")