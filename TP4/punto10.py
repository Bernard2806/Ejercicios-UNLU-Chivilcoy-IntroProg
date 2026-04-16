import math

coeficiente_a = float(input("Ingrese el Coeficiente A: "))
coeficiente_b = float(input("Ingrese el Coeficiente B: "))
coeficiente_c = float(input("Ingrese el Coeficiente C: "))

# Para la Raiz Cuadrada: math.sqtr(numero)

# Función Cuadratica
discriminante = coeficiente_b**2 - 4*coeficiente_a*coeficiente_c
    
if discriminante < 0:
    print("No tiene raíces reales.")
    
raiz1 = (-coeficiente_b - math.sqrt(discriminante)) / (2*coeficiente_a)
raiz2 = (-coeficiente_b + math.sqrt(discriminante)) / (2*coeficiente_a)

print("Las dos soluciones son:")
print(f"- Raiz Positiva: {raiz2}")
print(f"- Raiz Negativa: {raiz1}")