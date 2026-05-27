# ==================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
#
# Autor: Santiago Velasquez
# Problema 5 - Control de Horas Semanales
# ==================================================


# Matriz:
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 8, 9, 8, 8],
    ["Ana", 10, 9, 8, 9, 10],
    ["Luis", 7, 8, 7, 8, 7],
    ["Marta", 9, 9, 9, 9, 9]
]


# --------------------------------------------------
# Función para calcular horas semanales
# --------------------------------------------------

def calcular_horas(recurso):

    nombre = recurso[0]

    # Suma total de horas
    total_horas = sum(recurso[1:])

    # Clasificación de jornada
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# --------------------------------------------------
# Programa principal
# --------------------------------------------------

print("===== REPORTE DE HORAS SEMANALES =====\n")


for recurso in recursos:

    nombre, total, clasificacion = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total Horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")


input("\nPresiona Enter para salir...")
