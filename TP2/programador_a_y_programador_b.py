# --- PROGRAMADOR A (Código Descriptivo) ---
# Usa nombres de variables que explican qué contenido almacenan

# almaceno cuántos alumnos asistieron a la clase de hoy
alumnos_presentes = 35

# almaceno el total de inscriptos en la asignatura
alumnos_inscriptos = 54

# El cálculo es claro: (parte * 100) / total
# calculo del porcentaje de alumnos presentes en la clase de hoy
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos

# muestro el porcentaje calculado en pantalla
print('Hoy asistió el ' + str(porcentaje_presentes) + ' porciento del alumnado.')


# --- PROGRAMADOR B (Código Compacto) ---

# Usa letras sueltas que no dan pistas de su significado
p = 35
i = 54

# La fórmula es correcta matemáticamente, pero abstracta
pp = (p * 100) / i

# El resultado es el mismo, pero el código es más críptico
print('Hoy asistió el ' + str(pp) + ' % del alumnado.')

# ==========================================
# CONCLUSIÓN DEL ANÁLISIS
# ==========================================
# 1. ¿Ambas resuelven el problema? Sí, el resultado matemático es el mismo.
# 2. ¿Cuál es más legible? La versión A, por el uso de nombres descriptivos y comentarios.
# 3. ¿Desventajas de la B? Es difícil de entender para otros, difícil de 
#    corregir y propenso a errores por confusión de variables.