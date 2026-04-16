numero_1 = int(input("Ingrese el primer numero: "))

numero_2 = int(input("Ingrese el segundo numero: "))

if(numero_1 > numero_2):
    print(f"El primer numero ({numero_1}) es mayor que el segundo numero ({numero_2})")
elif(numero_1 < numero_2):
    print(f"El segundo numero ({numero_2}) es mayor que el primer numero ({numero_1})")
else:
    print(f"El primer numero ({numero_1}) y el segundo numero ({numero_2}) son iguales")