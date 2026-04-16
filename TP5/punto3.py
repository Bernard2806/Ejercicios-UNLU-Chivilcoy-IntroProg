num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Determinar maximo
if num1 >= num2 and num1 >= num3:
    maximo = num1
elif num2 >= num1 and num2 >= num3:
    maximo = num2
else:
    maximo = num3

# Determinar minimo
if num1 <= num2 and num1 <= num3:
    minimo = num1
elif num2 <= num1 and num2 <= num3:
    minimo = num2
else:
    minimo = num3

print("Numero maximo:", maximo)
print("Numero minimo:", minimo)