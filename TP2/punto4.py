# 1. Definición de variables de tipo entero (int)
numero1 = 10 
numero2 = 5

# 2. Operación matemática: se multiplican los valores numéricos
resultado = numero1 * numero2

# 3. Salida por pantalla con concatenación
# Es necesario usar str() porque no puedes sumar un texto (string) con un número (int).
# str() convierte el número en "texto" para que se pueda pegar a las otras palabras.
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))

# --- FORMA MODERNA (f-strings) ---
# Al poner una 'f' antes de las comillas, puedes meter las variables 
# directamente entre llaves {}. Python hace la conversión a texto (str) 
# de forma automática y transparente. ¡Mucho más fácil de leer!

print(f"El producto entre {numero1} y {numero2} da {resultado}")