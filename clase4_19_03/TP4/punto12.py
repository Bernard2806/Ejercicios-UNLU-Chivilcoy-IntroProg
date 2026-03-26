n1 = int(input("Ingrese el N°1: "))
n2 = int(input("Ingrese el N°2: "))
n3 = int(input("Ingrese el N°3: "))

numero_maximo = max(n1,n2,n3)
numero_minimo = min(n1,n2,n3)
n1_valor_absoluto = abs(n1)

print(f"El numero máximo es: {numero_maximo}")
print(f"El numero minímo es: {numero_minimo}")
print(f"El valor absoluto del N°1 es: {n1_valor_absoluto}")