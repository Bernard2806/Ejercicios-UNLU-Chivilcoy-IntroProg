apellido = input("Ingrese su Apellido: ")
parcial_n1 = float(input("Ingrese la Nota del Primer Parcial: "))
parcial_n2 = float(input("Ingrese la Nota del Segundo Parcial: "))

prom = (parcial_n1 + parcial_n2) / 2

print(f"Alumno [{apellido}]:")
print(f"- Primer Parcial: [{parcial_n1}].")
print(f"- Segundo Parcial: [{parcial_n2}].")
print(f"- Promedio: [{prom}].")