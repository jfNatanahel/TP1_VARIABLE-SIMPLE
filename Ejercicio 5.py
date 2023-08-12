#Se ingresan 5 notas de n alumnos, calcular y mostrar las dos perones notas de ellos.
n=int(input("Ingresar cantidad de alumnos: "))
i=1
while i<=n:
    n1=int(input("Ingresar nota del alumno: "))
    n2=int(input("Ingresar nota del alumno: "))
    if n1>n2:
        n1=n2
    n3=int(input("Ingresar nota del alumno: "))
    if n1>n3:
        n1=n3
    n4=int(input("Ingresar nota del alumno: "))
    if n1>n4:
        n1=n4
    n5=int(input("Ingresar nota del alumno: "))
    if n1>n5:
        n1=n5
    print("Peor nota del alumno es: ",n1)
    i=i+1
