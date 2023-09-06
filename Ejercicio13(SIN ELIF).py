Bandera = 0
Total_alumnos = 0
Ciudad_salta = 0
Interior = 0
Otras_provincias = 0
Mayores_25 = 0
Entre_25_21 = 0
Entre_18_21 = 0
Menores_18 = 0
Mayores_21_trabajo = 0

while Bandera == 0:
    alumno = input("Ingrese el nombre del alumno (o deje vacío para salir): ")
    
    if alumno == "":
        Bandera = 1
    
    print("Ingresar los números: 1=Ciudad de Salta , 2=Interior , 3=Otras provincias")
    localidad = int(input("Ingrese la localidad del alumno: "))
    
    if localidad == 1:
        Ciudad_salta += 1
    if localidad == 2:
        Interior += 1
    if localidad == 3:
        Otras_provincias += 1
    
    edad = int(input("Ingrese la edad del alumno: "))
    
    if edad > 25:
        Mayores_25 += 1
        tiene_trabajo = int(input("¿Tiene trabajo? 0=no, 1=si: "))
        if tiene_trabajo == 1:
            Mayores_21_trabajo += 1
    if 18 <= edad <= 21:
        Entre_18_21 += 1
    if edad < 18:
        Menores_18 += 1

Total_alumnos = Ciudad_salta + Interior + Otras_provincias
print("Resultados de la encuesta:")
print("Total de alumnos:", Total_alumnos)
print("Ciudad de Salta:", Ciudad_salta)
print("Interior:", Interior)
print("Otras provincias:", Otras_provincias)
print("Mayores de 25:", Mayores_25)
print("Entre 18 y 21:", Entre_18_21)
print("Menores de 18:", Menores_18)
print("Mayores de 21 con trabajo:", Mayores_21_trabajo)