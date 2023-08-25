total_alumnos = 0
ciudad_salta = 0
interior = 0
otras_provincias = 0
mayores_25 = 0
entre_21_25 = 0
menores_18 = 0
mayores_21_trabajo = 0

alumno = input("Ingrese el nombre del alumno (o dejar vacío para finalizar): ")

while alumno != "":
    total_alumnos += 1
    
    provincia = input("Ingrese la provincia del alumno (Salta/Interior/Otras provincias): ")
    if provincia == "Salta":
        ciudad_salta += 1
    elif provincia == "Interior":
        interior += 1
    else:
        otras_provincias += 1
    
    edad = int(input("Ingrese la edad del alumno: "))
    if edad > 25:
        mayores_25 += 1
    elif edad >= 21 and edad <= 25:
        entre_21_25 += 1
    else:
        menores_18 += 1
    
    if edad > 21:
        tiene_trabajo = input("¿El alumno tiene trabajo? (Sí/No): ")
        if tiene_trabajo == "Sí":
            mayores_21_trabajo += 1
    
    alumno = input("Ingrese el nombre del alumno (o dejar vacío para finalizar): ")

print("Resultados de la encuesta:")
print("Total de alumnos:", total_alumnos)
print("Cantidad de alumnos de la ciudad de Salta:", ciudad_salta)
print("Cantidad de alumnos del Interior:", interior)
print("Cantidad de alumnos de otras provincias:", otras_provincias)
print("Cantidad de alumnos mayores a 25 años:", mayores_25)
print("Cantidad de alumnos entre 21 y 25 años:", entre_21_25)
print("Cantidad de alumnos menores a 18 años:", menores_18)
print("Cantidad de alumnos mayores a 21 años con trabajo:", mayores_21_trabajo)