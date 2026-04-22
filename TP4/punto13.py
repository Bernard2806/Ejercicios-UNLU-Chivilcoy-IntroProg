# Pedir cantidad de segundos al usuario
segundos_usuario = int(input("Ingrese la cantidad de segundos: "))

hora = segundos_usuario // 3600
minutos = (segundos_usuario % 3600) // 60
segundos = segundos_usuario % 60

# Mostrar resultado en formato hh:mm:ss
print(f"{hora:02}:{minutos:02}:{segundos:02}")
