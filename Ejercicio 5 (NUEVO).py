N = int(input("Ingrese la cantidad de alumnos:"))

while N > 0:
    C = 1
    P1 = P2 = 101  # Inicializamos ambas peores notas con un valor alto.

    while C <= 5:
        nota = int(input(f"Ingrese el valor de la nota {C}:"))

        if nota < P1:
            P2 = P1
            P1 = nota
        else:
            if nota < P2:
                P2 = nota

        C += 1
    
    print("Las dos peores notas son:")
    print(P1)
    print(P2)

    N -= 1