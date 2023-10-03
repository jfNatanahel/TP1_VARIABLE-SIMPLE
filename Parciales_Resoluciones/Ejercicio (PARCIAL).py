"""
cantidad_total_requerimientos = 0
total_notas_resueltas = 0
total_incidentes = 0
horas_va = 0
horas_sl = 0
p1_nota_horas = 0
p2_nota_horas = 0
p3_nota_horas = 0
p1_incidentes_horas = 0
p2_incidentes_horas = 0
p3_incidentes_horas = 0
p1_notas_resueltas = 0
p2_notas_resueltas = 0
p3_notas_resueltas = 0
p1_incidentes = 0
p2_incidentes = 0
p3_incidentes = 0
bandera = 0

while bandera == 0:
    programador = input("Ingresar programador (P1)(P2)(P3): ")
    tipo_requerimiento = input("Ingresar tipo de requerimiento (N) o (I): ")
    if tipo_requerimiento != "N" and tipo_requerimiento != "I":
        bandera = 1
    horas = int(input("Ingresar el tiempo que tardó en finalizar: "))
    municipio = input("Ingresar municipio (SL)(VA): ")
    

    

    # Cantidad total de requerimientos resueltos.
    cantidad_total_requerimientos += 1

    if tipo_requerimiento == "N":
        total_notas_resueltas += 1
        if programador == "P1":
            p1_notas_resueltas += 1
            p1_nota_horas += horas
        elif programador == "P2":
            p2_notas_resueltas += 1
            p2_nota_horas += horas
        elif programador == "P3":
            p3_notas_resueltas += 1
            p3_nota_horas += horas
    elif tipo_requerimiento == "I":
        total_incidentes += 1
        if programador == "P1":
            p1_incidentes += 1
            p1_incidentes_horas += horas
        elif programador == "P2":
            p2_incidentes += 1
            p2_incidentes_horas += horas
        elif programador == "P3":
            p3_incidentes += 1
            p3_incidentes_horas += horas

    # Cantidad de horas de desarrollo asignadas a cada municipio.
    if municipio == "VA":
        horas_va += horas
    elif municipio == "SL":
        horas_sl += horas

# Calcular promedio expresado en porcentaje de notas resueltas por cada programador.
p1_porcentaje_notas = (p1_notas_resueltas / cantidad_total_requerimientos) * 100
p2_porcentaje_notas = (p2_notas_resueltas / cantidad_total_requerimientos) * 100
p3_porcentaje_notas = (p3_notas_resueltas / cantidad_total_requerimientos) * 100

# Calcular promedio expresado en porcentaje de incidentes resueltos por cada programador.
p1_porcentaje_incidentes = (p1_incidentes / cantidad_total_requerimientos) * 100
p2_porcentaje_incidentes = (p2_incidentes / cantidad_total_requerimientos) * 100
p3_porcentaje_incidentes = (p3_incidentes / cantidad_total_requerimientos) * 100

print("1. Cantidad total de requerimientos resueltos:", cantidad_total_requerimientos)
print("2. Cantidad total de notas resueltas:", total_notas_resueltas)
print("3. Cantidad total de incidentes resueltos:", total_incidentes)
print("4. Promedio expresado en porcentaje de notas resueltas por cada programador:")
print("P1:", p1_porcentaje_notas)
print("P2:", p2_porcentaje_notas)
print("P3:", p3_porcentaje_notas)
print("5. Promedio expresado en porcentaje de incidentes resueltos por cada programador:")
print("P1:", p1_porcentaje_incidentes)
print("P2:", p2_porcentaje_incidentes)
print("P3:", p3_porcentaje_incidentes)
print("6. Cantidad de horas de desarrollo asignadas a cada municipio:")
print("Municipio de San Lorenzo (SL):", horas_sl, "horas")
print("Municipio de Vaqueros (VA):", horas_va, "horas")
"""
promedio=(6/10)*100
print(promedio)