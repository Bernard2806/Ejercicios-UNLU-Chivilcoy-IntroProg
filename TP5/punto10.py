valor = input("Ingrese un valor: ")

if valor.isdigit():
    print("Es un numero")
elif valor.isalpha():
    print("Es una palabra")
elif valor.isalnum():
    print("Es alfanumerico")
else:
    print("Contiene caracteres especiales")