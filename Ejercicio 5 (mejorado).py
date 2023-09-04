#Se ingresan 5 notas de n alumnos, calcular y mostrar las dos peores notas de ellos.
n = int(input("Ingresar cantidad de alumnos: "))
i = 1

while i <= n:
    j = 1
    peor_nota1 = 101
    peor_nota2 = 101

    while j <= 5:
        nota = int(input("Ingresar nota: "))

        if nota < peor_nota1:
            peor_nota2 = peor_nota1
            peor_nota1 = nota
        else:
            if nota < peor_nota2:
                peor_nota2=nota
        j += 1

    print(f"Las dos peores notas del alumno {i} son: {peor_nota1} y {peor_nota2}")
    i += 1